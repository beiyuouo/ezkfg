from matplotlib.pyplot import cla


class BaseHandler(object):

    support_extensions = []

    @staticmethod
    def load(path: str):
        pass

    @staticmethod
    def dump(path: str, data: dict):
        pass
