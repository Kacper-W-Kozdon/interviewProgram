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
        print("Asserting types.")
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

def no_repetitions(fun):
    def no_repetition_wrapper(lst):
        lst_of_subsets = fun(lst)
        lst_of_subsets = list(map(sorted, lst_of_subsets))
        lst_of_subsets_len = len(lst_of_subsets)
        for index in range(lst_of_subsets_len):
            elem_to_inspect = lst_of_subsets.pop(0)
            if elem_to_inspect not in lst_of_subsets:
                lst_of_subsets.append(elem_to_inspect)
        print(lst_of_subsets)
        return lst_of_subsets
    return no_repetition_wrapper
    
def reset_global(fun):
    def wrapper_reset_global(lst):
        global depth
        global subset
        global lst_of_subsets
        depth = 0
        subset = []
        lst_of_subsets = []  
        print("Resetting globals.")
        return fun(lst)
    return wrapper_reset_global      
    
    
@reset_global
@assert_types
#@assert_is_set
@no_repetitions
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
    
    return lst_of_subsets

if __name__ == "__main__":
    lst = [1, 2, 3, 4, 5]
    main(lst)
    print()
    print()
    lst = [1, 1, 2, 2, 3]
    main(lst)
    