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
    '''

    Parameters
    ----------
    m : int, optional
        Index of the current element. The default is 0.
    tab : list, optional
        A list of all previous elements.. The default is initialize().

    Returns
    -------
    list
        Returns a list filled in with the Fibonacci sequence.

    '''
    n = m
    if n == 0:
        return tab.append(1)
    if n == 1:
        return tab.append(1)
    if n >= 2:
        tab.append(tab[n - 1] + tab[n - 2])
    return tab[n]
    
def fib_fun(m = 0, nlimit = 20, floatLim = np.finfo(np.single).max):  
    '''

    Parameters
    ----------
    m : int, optional
        Index of the current element. The default is 0.
    nlimit : TYPE, optional
        If int, stops the sequence at the n-th element, 
        else- breaks upon reaching the floatLim. The default is 20.
    floatLim : float32, optional
        By default maximum value of a signed single precision float (float32)
        used in the numpy library.. The default is np.finfo(np.single).max.

    Returns
    -------
    list
        A list filled in with the Fibonacci sequence.

    '''
    tab = initialize()
    limit = lambda m: m < nlimit if type(nlimit) is int else True  #
    while limit(m):
        storage(m, tab)
        if tab[m] > floatLim:
            break
        m = m + 1
    return tab if type(nlimit) is int else tab[:-1]
        
def is_even(tab):
    '''

    Parameters
    ----------
    tab : list
        A list of Fibonacci numbers..

    Returns
    -------
    numpy array.
        Returns a numpy array of indices and values of even elements of 
        the Fibonacci sequence.

    '''
    tabEven = (np.array(tab) % 2 == 0).astype(int)
    valEven = tabEven * tab
    idxEven = np.where(valEven != 0)[0]
    idxAndVal = np.array([idxEven[:], np.array(tab)[idxEven]]).reshape((2, -1)).transpose()
    return(idxAndVal)

def rec_even_fib(fib = (1, 2), tab = initialize()):
    '''

    Parameters
    ----------
    fib : a tuple, optional
        First pair consisting of the first even element and the preceeding 
        element. The default is (1, 2).
    tab : list, optional
        A list of even Fibonacci numbers. The default is initialize().

    Returns
    -------
    list
        A list of even Fibonacci numbers.

    '''
    (a, b) = (fib[0], fib[1])
    tab.append(b)
    rec_even_fib((a + 2 * b, 2 * a + 3 * b)) if b < np.finfo(np.single).max else 0
    return tab[:-1]

def sum_if_even(tab):
    '''

    Parameters
    ----------
    tab : list
        A list of all even Fibonacci numbers meeting the criteria.

    Returns
    -------
    float32 (np.single)
        A sum of all values within the provided list.

    '''
    return np.sum(tab)

def run():
    '''

    Returns
    -------
    sumFibEven : float32 (np.single)
        A sum of all even Fibonacci numbers meeting the criteria. Brute force 
        approach (each number checked individually).

    '''
    limit = True
    tab = initialize()
    tab = fib_fun(nlimit = limit)
    idxAndVal = is_even(tab)
    evenValTab = idxAndVal[:, 1]
    sumFibEven = sum_if_even(evenValTab)
    return sumFibEven

def run2():
    '''

    Returns
    -------
    sumEven : float32 (np.single)
        A sum of all even Fibonacci numbers meeting the criteria. 
        The smart approach.

    '''
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