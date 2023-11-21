# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:01:17 2023

@author: xBubblex
"""

import heapq

def assert_types(fun):
    def assert_wrap(*args):
        arguments = args[0]
        assert type(arguments) == list, "The first argument has to be a list."
        assert all(list(map(lambda x: type(x) == float or type(x) == int, arguments))) == True, "The list has to contain numbers."
        return fun(*args)
    return assert_wrap

@assert_types
def find_top_K(lst, K):
    
    lst_len = len(lst)
    min_heap = []
    heapq.heapify(lst)
    
    assert lst_len - K >= 0, "K is greater than the length of the list."
    
    print("Success!")
    
    for i in range(lst_len - K):
        heapq.heappush(min_heap, heapq.heappop(lst))
    print(lst)
    return(lst)

def main():
    lst = [5, 1, -2, 2, -3, 4, 4]
    try:
        find_top_K(lst, 2)
    except AssertionError as msg:
        print(msg)  
    try:
        find_top_K(lst, 8)
    except AssertionError as msg:
        print(msg)  
    lst = ["a", 1]
    try:
        find_top_K(lst, 2)
    except AssertionError as msg:
        print(msg)
    

if __name__ == "__main__":
    main()