#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author: yzw
@CreateTime: 2017-06-16, 16:05:59 CST+0800
@File: softmax.py
"""
import math

z = [1.0,2.0,3.0,4.0,1.0,1.0,2.0,3.0]
z_exp = [math.exp(i) for i in z]
sum_z_exp = sum(z_exp)
softmax = [round(i/sum_z_exp,3) for i in z_exp ]
print softmax
