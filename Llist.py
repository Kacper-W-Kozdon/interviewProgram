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
        return self
    
    def append_list(fun):
        def inner_append_list(self, value):
            if type(value) == list:
                
                value.reverse()
                while(value[-1]):
                    value_to_append = value.pop()
                    fun(self, value_to_append)
                    try:
                        value[-1]
                    except:
                        print("Index out of the list.")
                        break
            else:
                fun(self, value)
        return inner_append_list
            
            
    
    @append_list
    def append(self, value):
        self.node.next = Node(value)
        
        self.node = self.node.next
        
        
    def reset_head(self):
        self.node = self.head
        
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
            try:
                print(self.node.value, self.node.next.value)
            except:
                pass
        else: 
            raise StopIteration
            
        return self
    
def main():
    head = Node(1)
    llist = Llist(head)
    print(type(llist))
    llist.append([2, 3, 4])
    llist.reset_head()
    iterllist = iter(llist)   
    print()
    
    next(iterllist)
    next(iterllist)
    next(iterllist)
    pass

if __name__ == "__main__":
    main()
    

        