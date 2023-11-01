# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:09:45 2023

@author: xBubblex
"""
depth = 0
subset = []
lst_of_subsets = []

def assert_types(fun):
    def wrapper(lst):
        assert type(lst) == list
        return fun(lst)
    return wrapper

def assert_is_set(fun):
    def wrapper(lst):
        assert lst == list(set(lst))
        return fun(lst)
    return wrapper

def helper_fun(lst):
    global subset
    global lst_of_subsets
    subset += ["end"]
    subsetcopy = subset[ : ]
    for elem in lst:
        #print(elem)
        subsetcopy[-1] = elem
        print(subsetcopy)
        lst_of_subsets += [subsetcopy]
    #print(lst_of_subsets)

@assert_types
@assert_is_set
def main(lst: list,/ ) -> list:
    global depth
    global subset
    global lst_of_subsets
    helper_lst = lst
    
    for sequence_len in range(len(lst) + 1):
        subset = []
        for depth in range(sequence_len):
            
            for idx in range(depth, len(lst) - sequence_len + depth):
                helper_lst = lst[idx : ]
                helper_fun(helper_lst)
    pass

if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    main(lst)