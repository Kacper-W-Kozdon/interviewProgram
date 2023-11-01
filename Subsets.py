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

def helper_fun(lst, depth):
    global subset
    global lst_of_subsets
    #print(lst)
    for idx, elem in enumerate(lst):
        if depth > 0:           
            subset[depth] = elem           
            helper_fun(lst[idx + 1 : ], depth - 1)
        elif depth == 0 and len(subset) > 0:
            subset[depth] = elem
            #print(subset)
            lst_of_subsets += [subset.copy()]
        elif len(subset) == 0:
            lst_of_subsets += [[]]
            break

        
    
        
    
    

@assert_types
@assert_is_set
def main(lst: list,/ ) -> list:
    global depth
    global subset
    global lst_of_subsets
    helper_lst = lst
    
    for sequence_len in range(len(lst) + 1):
        subset = [0 for i in range(sequence_len)]
        depth = sequence_len - 1

        helper_lst = lst.copy()
        helper_fun(helper_lst, depth)
    pass
    print(lst_of_subsets)

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    main(lst)