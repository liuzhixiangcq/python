# @author page
# @date 2017/11/24

# coding:utf-8
# !/usr/bin/python

import math

def triangleArea(a,b,c):
    h = (a + b + c) / 2.0
    s = math.sqrt(h * (h - a) * (h - b) * (h - c))
    print s

triangleArea(3,4,5)
