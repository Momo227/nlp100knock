#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

sys.path.append("../../")
from src.chapter01 import q02


def test_re_value():
    assert q02.add_char("パトカー", "タクシー") == "パタトクカシーー"
    assert q02.add_char("リンゴ", "ミカン") == "リミンカゴン"