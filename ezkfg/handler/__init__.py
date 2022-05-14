#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   ezkfg\handler\__init__.py
# @Time    :   2022-05-13 21:29:25
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0


from .base_handler import BaseHandler
from .json_handler import JSONHandler
from .yaml_handler import YAMLHandler
from .ini_handler import INIHandler
from .py_handler import PyHandler

handler_factories = {}

__build_in_handlers = [JSONHandler, YAMLHandler, INIHandler, PyHandler]


def register_handler_factory(name: str, handler: BaseHandler):
    handler_factories[name] = handler


def build_handler(name: str, *args, **kwargs):
    if name in handler_factories:
        return handler_factories[name](*args, **kwargs)
    else:
        raise NotImplementedError(f"{name} file is not supported")


def get_handler(name: str):
    if name in handler_factories:
        return handler_factories[name]
    else:
        raise NotImplementedError(f"{name} file is not supported")


for handler in __build_in_handlers:
    for ext in handler.support_extensions:
        register_handler_factory(ext, handler)
