import configparser
from typing import Dict, Any
from .base_handler import BaseHandler


class INIHandler(BaseHandler):
    support_extensions = [".ini"]

    @staticmethod
    def load(path: str, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read(path, *args, **kwargs)
        config = dict(config.items("DEFAULT" if not "section" in kwargs else kwargs["section"]))
        return config

    @staticmethod
    def dump(path: str, data: Dict, *args, **kwargs):
        config = configparser.ConfigParser()
        config.read_dict({"DEFAULT": data}, *args, **kwargs)
        with open(path, "w") as f:
            config.write(f, *args, **kwargs)
