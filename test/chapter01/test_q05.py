#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

sys.path.append("../../")
from src.chapter01 import q05


def test_re_value():
    assert q05.word_bi_gram("I am an NLPer") == [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
    assert q05.char_bi_gram("I am an NLPer") ==  [['I', ' '], [' ', 'a'], ['a', 'm'], ['m', ' '], ['a', 'n'], ['n', ' '], [' ', 'N'], ['N', 'L'], ['L', 'P'], ['P', 'e'], ['e', 'r']]
    assert q05.word_bi_gram("He was a NLPer") == [['He', 'was'], ['was', 'a'], ['a', 'NLPer']]
    assert q05.char_bi_gram("He was a NLPer") == [['H', 'e'], ['e', ' '], [' ', 'w'], ['w', 'a'], ['a', 's'], ['s', ' '], ['a', ' '], [' ', 'N'], ['N', 'L'], ['L', 'P'], ['P', 'e'], ['e', 'r']]