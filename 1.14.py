#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/4/25


def bool_ji(data):
    ji_num = 0
    tup = ()
    for i in data:
        if i % 2 != 0:
            tup += (i,)
    if len(tup) >= 2:
        return True
    else:
        return False


print(bool_ji([2, 5, 8, 223]))
print(bool_ji([3, 2, 6]))
