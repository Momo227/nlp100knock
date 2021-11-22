#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

sys.path.append("../../")
from src.chapter01 import q07


def test_re_value():
    assert q07.make_sentence(12, "気温", 22.4) == "12時の気温は22.4"
    assert q07.make_sentence(15, "おやつ", "大学芋") == "15時のおやつは大学芋"