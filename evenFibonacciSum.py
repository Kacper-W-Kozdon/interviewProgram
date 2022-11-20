# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:25:45 2022

@author: xBubblex
"""

import numpy as np
import time

def initialize():
    return []

def storage(m = 0, tab = initialize()):
    n = m
    if n == 0:
        return tab.append(1)
    if n == 1:
        return tab.append(1)
    if n >= 2:
        tab.append(tab[n - 1] + tab[n - 2])
    return tab[n]
    
def fib_fun(m = 0, nlimit = 20, floatLim = np.finfo(np.single).max):
    tab = initialize()
    limit = lambda m: m < nlimit if type(nlimit) is int else True
    while limit(m):
        storage(m, tab)
        if tab[m] > floatLim:
            break
        m = m + 1
    return tab if type(nlimit) is int else tab[:-1]
        
def is_even(tab):
    tabEven = (np.array(tab) % 2 == 0).astype(int)
    valEven = tabEven * tab
    idxEven = np.where(valEven != 0)[0]
    idxAndVal = np.array([idxEven[:], np.array(tab)[idxEven]]).reshape((2, -1)).transpose()
    return(idxAndVal)

def recursion_fib():
    limit = 30
    tab = initialize()
    tab = np.array(fib_fun(nlimit = limit))
    tab2 = np.array([[idx, tab[idx]] for (idx, tab[idx]) in enumerate(tab)])
    idxAndVal = is_even(tab)
    evenIdx = idxAndVal[:, 0]
    preEvenIdx = np.array([evenIdx[:] - 2, evenIdx[:] - 1]).reshape((1, -1), order = "F").flatten().astype(int).tolist()
    preEvenValue = np.array(tab[preEvenIdx])
    preIdxAndVal = np.array([preEvenIdx, preEvenValue])
    idxAndVal2 = np.concatenate((np.array([[0, 1], [1, 1]]), idxAndVal), axis = 0)
    return(tab2)

def rec_even_fib(fib = (1, 2), tab = initialize()):
    (a, b) = (fib[0], fib[1])
    tab.append(b)
    rec_even_fib((a + 2 * b, 2 * a + 3 * b)) if b < np.finfo(np.single).max else 0
    return tab[:-1]

def sum_if_even(tab):
    return np.sum(tab)

def run():
    limit = True
    tab = initialize()
    tab = fib_fun(nlimit = limit)
    idxAndVal = is_even(tab)
    evenValTab = idxAndVal[:, 1]
    sumFibEven = sum_if_even(evenValTab)
    return sumFibEven

def run2():
    tab = rec_even_fib()
    sumEven = sum_if_even(tab)
    return sumEven

def run3():
    pass

tab = fib_fun()
t1 = time.time()
print(run())
t2 = time.time()
print(run2())
t3 = time.time()
print(t2 - t1, t3 - t2)
print(np.single(run()) == np.single(run2()))