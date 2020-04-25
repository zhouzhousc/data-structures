#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/4/25


def bool_dic(data):
    list0 = []
    for i in data:
        if i in list0:
            return "there is the same num"
        else:
            list0.append(i)
    return "there is not the same num"


def bool2dic(data):
    for i in data:
        if data.count(i) != 1:
            return "there is the same num"
    return "there is not the same num"


list_test = [1, 2, 3, 2, 6, 7]
print(bool2dic(list_test))
