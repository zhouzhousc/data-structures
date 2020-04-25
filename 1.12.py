#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author: Carl time:2020/4/25


import random

print(random.randrange(5, 10))


def own_choice(data):
    if data:
        return data[random.randrange(0, len(data))]


print(own_choice([34, 56, 421, 1, 3, 4]))
