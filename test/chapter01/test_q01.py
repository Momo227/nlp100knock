#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

sys.path.append("../../")
from src.chapter01 import q01


def test_re_value():
    assert q01.add_char("パタトクカシーー") == "パトカー"
    assert q01.add_char("リミンカゴン") == "リンゴ"