# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 18:15:26 2023

@author: xBubblex
"""

class Node():
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class Llist():
    
    def __init__(self, head):
        self.head = head
        self.node = head
    
    def __iter__(self):
        if not self.node == self.head:
            self.node = self.head
       
        return self
    
    def append_list(fun):
        def inner_append_list(self, value):
            if type(value) == list:
                print("yes")
                value.reverse()
                while(value[-1]):
                    value_to_append = value.pop()
                    fun(self, value_to_append)
                    try:
                        value[-1]
                    except:
                        break
            else:
                fun(self, value)
        return inner_append_list
            
            
    
    @append_list
    def append(self, value):
        self.node.next = value
        self.node = Node(value)
        
    def reverse(self):
        
        if not self.head:
            return self
        
        pointer = self.head
        
        while(pointer.next):
            aux = Node(pointer.value).value
            Node(pointer.value).value = Node(pointer.value).next 
            Node(pointer.value).next = aux
        
        return self
    
    def __next__(self):
         
        if self.node.next:
            self.node = self.node.next
            print(self.node.value)
        else: 
            raise StopIteration
        return self
    
def main():
    head = Node(1)
    llist = Llist(head)
    print(type(llist))
    llist.append([2, 3, 4])
    iterllist = iter(llist)
    print(next(iterllist))
    print(next(iterllist))
    print(next(iterllist))
    pass

if __name__ == "__main__":
    main()
    

        