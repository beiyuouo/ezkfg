import os
from .handler import build_handler, get_handler


class Config(dict):
    def __init__(self):
        pass

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
