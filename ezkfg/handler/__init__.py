from .base_handler import BaseHandler

handler_factories = {}

__build_in_handlers = []


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
