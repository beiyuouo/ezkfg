from charset_normalizer import from_fp


from typing import Dict, List, Tuple, Any, Union, Optional, Iterable

from .base_handler import BaseHandler


class PyHandler(BaseHandler):
    support_extensions = [".py"]

    @staticmethod
    def load(path: str, *args, **kwargs):
        import importlib

        spec = importlib.util.spec_from_file_location("config", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return {k: v for k, v in module.config.__dict__.items() if not k.startswith("__")}

    @staticmethod
    def dump(path: str, data: Dict, *args, **kwargs):
        with open(path, "w") as f:
            f.write(f"class config:\n")
            for k, v in data.items():
                f.write(f"    {k} = {v}\n")
