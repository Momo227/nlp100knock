#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

sys.path.append("../../")
from src.chapter01 import q08


def test_re_value():
    assert q08.cipher('Oh, I have had such a curious dream!') == "Os, I szev szw hfxs z xfirlfh wivzn!"
    assert q08.cipher('Wake up, Alice dear! Why, what a long sleep you have had!') == "Wzpv fk, Aorxv wvzi! Wsb, dszg z olmt hovvk blf szev szw!"