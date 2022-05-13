#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   ezkfg\handler\json_handler.py
# @Time    :   2022-05-13 21:29:53
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0


from .base_handler import BaseHandler


class JSONHandler(BaseHandler):
    support_extensions = [".json"]

    @staticmethod
    def load(path: str):
        pass

    @staticmethod
    def dump(path: str):
        pass
