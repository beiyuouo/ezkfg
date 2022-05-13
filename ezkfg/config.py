import os
import copy

from .handler import build_handler, get_handler


class Config(object):
    def __init__(self, *args, **kwargs):
        for arg in args:
            if not arg:
                continue
            elif isinstance(arg, dict):
                for key, val in arg.items():
                    setattr(self, key, self._hook(val))
            elif isinstance(arg, tuple) and (not isinstance(arg[0], tuple)):
                setattr(self, arg[0], self._hook(arg[1]))
            else:
                for key, val in iter(arg):
                    setattr(self, key, self._hook(val))

        for key, val in kwargs.items():
            setattr(self, key, self._hook(val))

    def _hook(self, value):
        if isinstance(value, dict):
            return Config(value)
        elif isinstance(value, list):
            return type(value)(self._hook(elem) for elem in value)
        return value

    def load(self, obj):
        if isinstance(obj, dict):
            self.update(obj)
        elif isinstance(obj, list):
            pass
        elif isinstance(obj, Config):
            self.update(obj)
        elif isinstance(obj, str):
            self.load_from_file(obj)
        else:
            raise TypeError(f"{type(obj)} is not supported")

    def load_from_file(self, path: str):
        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} not found")

        file_ext = os.path.splitext(path)[1]
        handler = get_handler(file_ext)

    def dump(self, path: str):
        pass

    def merge(self, other: dict):
        pass

    def update(self, other):
        pass

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

    def __repr__(self):
        type_name = type(self).__name__
        arg_strings = []
        star_args = {}
        for arg in self._get_args():
            arg_strings.append(repr(arg))
        for name, value in self._get_kwargs():
            if name.isidentifier():
                arg_strings.append("%s=%r" % (name, value))
            else:
                star_args[name] = value
        if star_args:
            arg_strings.append("**%s" % repr(star_args))
        return "%s(%s)" % (type_name, ", ".join(arg_strings))

    def _get_kwargs(self):
        return sorted(self.__dict__.items())

    def _get_args(self):
        return []

    def __eq__(self, other):
        if not isinstance(other, Config):
            return NotImplemented
        return vars(self) == vars(other)

    def __contains__(self, key):
        return key in self.__dict__
