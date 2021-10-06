#!/usr/bin/python
# -*- Coding: utf-8 -*-
import sys

sys.path.append("../../")
from src.chapter01 import q04


def test_re_value():
    assert q04.add_char("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.") == {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
    assert q04.add_char("You Have Plenty Of Sweets Right Now Because It's Summer, But Once Winter Comes, There Will Be No Food To Eat Here.") == {'Y': 1, 'Ha': 2, 'Pl': 3, 'Of': 4, 'S': 5, 'R': 6, 'N': 7, 'B': 8, 'I': 9, 'Su': 10, 'Bu': 11, 'On': 12, 'Wi': 13, 'Co': 14, 'T': 15, 'W': 16, 'Be': 17, 'No': 18, 'F': 19, 'To': 20, 'Ea': 21, 'He': 22}
