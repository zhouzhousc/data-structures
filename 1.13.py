#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/4/25


def s_list(list0):
    list1 = []
    for i in list0:
        list1.insert(0, i)
    return list1


list_test = [23, 432, 12, 53, 90]
print(s_list(list_test))
# list.reverse()
# 反向列表中元素
list_test.reverse()
print(list_test)

# list.sort( key=None, reverse=False)
# 对原列表进行排序(降序或升序)

