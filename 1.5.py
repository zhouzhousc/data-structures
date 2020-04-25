#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/4/25


def sqrt_sum(n):
    return sum((i + 1) * (i + 1) for i in range(n))


print(sqrt_sum(5))
