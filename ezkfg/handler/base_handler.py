#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    :   ezkfg\handler\base_handler.py
# @Time    :   2022-05-13 21:29:32
# @Author  :   Bingjie Yan
# @Email   :   bj.yan.pa@qq.com
# @License :   Apache License 2.0

from pathlib import Path


class BaseHandler(object):

    support_extensions = []

    @staticmethod
    def load(path: str or Path):
        pass

    @staticmethod
    def dump(path: str or Path, data: dict):
        pass
