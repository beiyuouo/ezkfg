#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   ezkfg\config.py
# @Time    :   2022-05-13 21:30:17
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0


from argparse import Namespace
import argparse
import os
import sys
import copy
from typing import Dict, List, Tuple, Any, Union, Optional, Iterable
from ezkfg.handler import build_handler, get_handler


class Config(object):
    __delimiter__ = "."

    def __init__(self, *args, **kwargs):
        if "__parent__" in kwargs:
            setattr(self, "__parent__", kwargs["__parent__"])
        if "__key__" in kwargs:
            setattr(self, "__key__", kwargs["__key__"])

        self.load_args_kwargs(*args, **kwargs)
        # self.args_parse([])  # load sys.argv

    def load_args_kwargs(self, *args, **kwargs):
        # self.load_from_args(Namespace(*args, **kwargs))
        for arg in args:
            if not arg:
                continue
            elif isinstance(arg, Dict):
                for key, val in arg.items():
                    setattr(self, key, self._hook(val))
            elif isinstance(arg, Tuple) and (not isinstance(arg[0], tuple)):
                setattr(self, arg[0], self._hook(arg[1]))
            elif isinstance(arg, List):
                self.args_parse(arg)
            else:
                for key, val in iter(arg):
                    setattr(self, key, self._hook(val))

        for key, val in kwargs.items():
            setattr(self, key, self._hook(val))

    def _hook(self, value):
        if isinstance(value, Dict):
            return Config(value)
        elif isinstance(value, List):
            return type(value)(self._hook(elem) for elem in value)
        return value

    def load(self, obj):
        if isinstance(obj, Dict):
            self.update(obj)
        elif isinstance(obj, List):
            self.args_parse(obj)
        elif isinstance(obj, Config):
            self.update(obj)
        elif isinstance(obj, str):
            self.load_from_file(obj)
        elif isinstance(obj, Namespace):
            self.update(obj.__dict__)
        else:
            raise TypeError(f"{type(obj)} is not supported")

    def load_from_file(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} not found")

        file_ext = os.path.splitext(path)[1]
        handler = get_handler(file_ext)

        self.update(Config(handler.load(path)))

    def dump(self, path: str):
        file_ext = os.path.splitext(path)[1]
        handler = get_handler(file_ext)
        handler.dump(path, self.dict())

    def update(self, other):
        for key, val in other.items():
            setattr(self, key, val)

    merge = update

    def copy(self):
        return copy.copy(self)

    def deepcopy(self):
        return copy.deepcopy(self)

    def __deepcopy__(self, memo):
        other = self.__class__()
        memo[id(self)] = other
        for key, value in self.__dict__.items():
            setattr(other, key, copy.deepcopy(value))
        return other

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any) -> None:
        setattr(self, key, self._hook(value))

    def __delitem__(self, key: str) -> None:
        delattr(self, key)

    def __iter__(self) -> Iterable:
        return iter(self.__dict__)

    def keys(self) -> Iterable:
        return self.__dict__.keys()

    def values(self) -> Iterable:
        return self.__dict__.values()

    def items(self) -> Iterable:
        return self.__dict__.items()

    def __getattr__(self, __name: str) -> Any:
        if self.__delimiter__ in __name:
            __name, __rest = __name.split(self.__delimiter__, 1)
            return getattr(self[__name], __rest)

        if __name in self.__dict__.keys():
            return self.__dict__[__name]
        else:
            return self.__missing__(__name)

    def __missing__(self, __name: str) -> Any:
        return self.__class__(__parent__=self, __key__=__name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        if self.__delimiter__ in __name:
            __name, __rest = __name.split(self.__delimiter__, 1)
            self.__dict__[__name] = Config()
            setattr(self[__name], __rest, __value)
        else:
            self.__dict__[__name] = self._hook(__value)

        try:
            _par = object.__getattribute__(self, "__parent__")
            _key = object.__getattribute__(self, "__key__")
        except:
            _par = None

        if _par is not None:
            _par[_key] = self
            object.__delattr__(self, "__parent__")
            object.__delattr__(self, "__key__")

    def __repr__(self):
        arg_strings = []
        star_args = {}
        for arg in self._get_args():
            arg_strings.append(repr(arg))
        for name, value in self._get_kwargs():
            # if name.startswith("_"):
            #     continue
            if name.isidentifier():
                arg_strings.append(f"'{name}': {repr(value)}")
            else:
                star_args[name] = value
        if star_args:
            arg_strings.append(f"**{repr(star_args)}")

        return f"{{{', '.join(arg_strings)}}}"

    def _get_kwargs(self):
        return sorted(self.__dict__.items())

    def _get_args(self):
        return []

    def dict(self):
        base = {}
        for key, value in self._get_kwargs():
            if not key.isidentifier() or key.startswith("_"):
                continue
            if isinstance(value, type(self)):
                base[key] = value.dict()
            elif isinstance(value, (list, tuple)):
                base[key] = type(value)(item.dict() if isinstance(item, type(self)) else item for item in value)
            else:
                base[key] = value
        return base

    def __eq__(self, other):
        if not isinstance(other, Config):
            return NotImplemented
        return vars(self) == vars(other)

    def __contains__(self, key):
        return key in self.__dict__

    def __str__(self) -> str:
        return str(self.dict())

    def get(self, key, default=None):
        try:
            ret = self[key]
        except AttributeError:
            ret = default
        return ret

    def __getstate__(self):
        return self.dict()

    def __setstate__(self, state):
        self.update(state)

    def args_parse(self, args: List):
        if len(args) == 0:
            args = sys.argv[1:]
        for arg in args:
            if arg.startswith("--"):
                key, value = arg[2:].split("=", 1)
                key = key.replace("-", "_")
                setattr(self, key, value)
            elif arg.startswith("-"):
                key, value = arg[1:].split("=", 1)
                key = key.replace("-", "_")
                setattr(self, key, value)
            else:
                setattr(self, arg, True)
