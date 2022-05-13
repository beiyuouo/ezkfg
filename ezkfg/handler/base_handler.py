#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   ezkfg\handler\base_handler.py
# @Time    :   2022-05-13 21:29:32
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0


class BaseHandler(object):

    support_extensions = []

    @staticmethod
    def load(path: str):
        pass

    @staticmethod
    def dump(path: str, data: dict):
        pass
