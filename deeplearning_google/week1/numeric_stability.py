#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 12:12:32 2018

@author: gilson
@fileoverview: Checking Numerical stability
"""


def check_stability(x):
    t = x
    for i in range (1000000):
        x+= 0.000001
    x-=t
    print(x)


x=1000000000
check_stability(x)
"""
    Answers 0.95367431640625
"""
x=1
check_stability(x)
"""
    Answers 0.9999999999177334
"""
