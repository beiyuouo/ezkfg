from .base_handler import BaseHandler


class JSONHandler(BaseHandler):
    support_extensions = [".json"]

    @staticmethod
    def load(path: str):
        pass

    @staticmethod
    def dump(path: str):
        pass
