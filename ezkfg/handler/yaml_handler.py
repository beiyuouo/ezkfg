#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   ezkfg\handler\yaml_handler.py
# @Time    :   2022-05-13 21:30:05
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from typing import Dict, Any

from .base_handler import BaseHandler


class YAMLHandler(BaseHandler):
    support_extensions = [".yaml", ".yml"]

    @staticmethod
    def load(path: str, *args, **kwargs):
        import yaml

        with open(path, "r") as f:
            return yaml.safe_load(f, *args, **kwargs)

    @staticmethod
    def dump(path: str, data: Dict, *args, **kwargs):
        import yaml

        with open(path, "w") as f:
            yaml.safe_dump(data, f, *args, **kwargs)
