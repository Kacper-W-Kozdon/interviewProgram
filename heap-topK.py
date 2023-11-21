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
    lst_copy = lst.copy()

    assert lst_len - K >= 0, f"K = {K} is greater than the length of the list = {lst_len}."
    
    print("Success!")
    heapq.heapify(lst_copy)
    
    for i in range(lst_len - K):
        heapq.heappush(min_heap, heapq.heappop(lst_copy))

    print(f"Top {K} elements of the input list: {lst_copy}")
    return(lst_copy)

@assert_types
def find_Kth_smallest(lst, K):
    lst_len = len(lst)
    min_heap = []
    th = ""
    lst_copy = lst.copy()
    assert lst_len - K >= 0, f"K = {K} is greater than the length of the list = {lst_len}."
    
    heapq.heapify(lst_copy)
    
    print("Success!")
    
    for i in range(K - 1):
        heapq.heappush(min_heap, heapq.heappop(lst_copy))
        
    heapq.heapify(lst_copy)
    
    Kth_smallest = lst_copy[0]
    th = str(K)[-1]

    if th == "1":
        th = "st"
    elif th == "2":
        th = "nd"
    elif th == "3":
        th = "rd"
    else:
        th = "th"
    

    print(f"The {K}{th} smallest element is {Kth_smallest}")
    
    return(Kth_smallest)
    
    

def main():
    lst = [5, 1, -2, 2, -3, 4, 4]
    try:
        find_top_K(lst, 2)
    except AssertionError as msg:
        print(msg)  
        
    try:
        find_Kth_smallest(lst, 3)
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