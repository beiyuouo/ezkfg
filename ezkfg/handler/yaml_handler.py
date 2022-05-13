#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   ezkfg\handler\yaml_handler.py
# @Time    :   2022-05-13 21:30:05
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0


from .base_handler import BaseHandler


class YAMLHandler(BaseHandler):
    support_extensions = [".yaml", ".yml"]

    @staticmethod
    def load(path: str):
        pass

    @staticmethod
    def dump(path: str):
        pass
