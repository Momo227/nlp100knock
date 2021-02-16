#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

sys.path.append("../../")
from src.chapter01 import q00


def test_re_value():
    assert q00.re_value("software") == "erawtfos"
    assert q00.re_value("stressed") == "desserts"
