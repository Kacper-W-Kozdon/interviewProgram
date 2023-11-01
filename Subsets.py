# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 17:09:45 2023

@author: xBubblex
"""

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

@assert_types
@assert_is_set
def main(lst: list,/ ) -> list:
    global depth
    global subset
    global lst_of_subsets
    
    for sequence_len in range(len(lst) + 1):
        for depth in range(sequence_len - 1, -1, -1):
            pass
    pass

if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    main()4