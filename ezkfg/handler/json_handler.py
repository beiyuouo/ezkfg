#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   ezkfg\handler\json_handler.py
# @Time    :   2022-05-13 21:29:53
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0


from typing import Dict, Any

from .base_handler import BaseHandler


class JSONHandler(BaseHandler):
    support_extensions = [".json"]

    @staticmethod
    def load(path: str, *args, **kwargs):
        import json

        with open(path, "r") as f:
            return json.load(f, *args, **kwargs)

    @staticmethod
    def dump(path: str, data: Dict, *args, **kwargs):
        import json

        with open(path, "w") as f:
            json.dump(data, f, *args, **kwargs)
