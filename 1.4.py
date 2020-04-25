#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/4/25

def sqrt_sum(n):
    asum = 0
    for i in range(n):
        asum += (i + 1) * (i + 1)
    return asum


print(sqrt_sum(3))
