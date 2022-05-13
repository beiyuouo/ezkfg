from .base_handler import BaseHandler


class PyHandler(BaseHandler):
    support_extensions = [".py"]

    @staticmethod
    def load(path: str):
        pass

    @staticmethod
    def dump(path: str):
        pass
