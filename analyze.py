# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:05:48 2021

@author: Hacha
"""

from contextlib import contextmanager
from typing import List
import numpy as np
import time
import math


@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"Elapsed Time: {(end - start)}s")

def float_bin(number, places = 10):
    temp = number
    if number < 0:
        number = - number
    whole, dec = str(number).split(".")
    whole = int(whole)
    dec = int (dec)
    res = bin(whole).lstrip("0b") + "."
    title = len(res)
    for x in range(places -title):
        whole, dec = str((decimal_converter(dec)) * 2).split(".")
        dec = int(dec)
        res += whole
    lst = [c for c in res]
    return lst

def decimal_converter(num): 
    while num > 1:
        num /= 10
    return num


def bin_to_float(str):
    barrier = str.index('.')
    integer = str[:barrier]
    point = str[barrier+1:]
    len_int = len(integer)
    num_int = 0
    for i in range(len_int):
        num_int = num_int + int(integer[len_int - i - 1]) * math.pow(2, i)
    
    len_float = len(point)
    num_float = 0.0
    for i in range(len_float):
        num_float = num_float + int(point[i]) * pow(2, - (i +1))
    #print(integer)
    #print("num = {}".format(num_int))
    #print(point)
    #print("float = {}".format(num_float))
    return num_int + num_float
    

def unit_vector(vector):
    return vector / np.linalg.norm(vector)

def angle(v1, v2):
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))