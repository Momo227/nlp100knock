#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

sys.path.append("../../")
from src.chapter01 import q09


def test_re_value():
    assert q09.typoglycemia("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind.") == ['I', 'the', 'couldn’t', 'phenomenal', 'what', 'was', 'actually', 'human', 'understand', ':', 'that', 'could', 'believe', 'power', 'I', 'reading', 'I', 'of', 'the', 'mind.']
    assert q09.typoglycemia('I like dogs.') == ["I", "like", "dogs."]