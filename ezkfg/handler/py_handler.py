#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   ezkfg\handler\py_handler.py
# @Time    :   2022-05-15 02:34:26
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from typing import Dict

from .base_handler import BaseHandler


class PyHandler(BaseHandler):
    support_extensions = [".py"]

    @staticmethod
    def load(path: str, *args, **kwargs):
        import importlib

        spec = importlib.util.spec_from_file_location("config", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return {
            k: v for k, v in module.config.__dict__.items() if not k.startswith("__")
        }

    @staticmethod
    def dump(path: str, data: Dict, *args, **kwargs):
        with open(path, "w") as f:
            f.write(f"class config:\n")
            for k, v in data.items():
                f.write(f"    {k} = {v}\n")
