from .base_handler import BaseHandler


class YAMLHandler(BaseHandler):
    support_extensions = [".yaml", ".yml"]

    @staticmethod
    def load(path: str):
        pass

    @staticmethod
    def dump(path: str):
        pass
