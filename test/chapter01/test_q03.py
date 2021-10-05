#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

sys.path.append("../../")
from src.chapter01 import q03


def test_re_value():
    assert q03.add_char("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.") == [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    assert q03.add_char("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.") == [2, 2, 4, 7, 5, 5, 3, 7, 8, 3, 7, 5, 4, 4, 5, 8, 6, 6, 4, 3]