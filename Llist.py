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
        
    def reset_head_decorator(fun):
        def reset_wrapper(self):
            self.reset_head(self)
        return reset_wrapper
        
    def reverse(self):
        
        if not self.head:
            return self
        
        pointer = self.head
        
        while(pointer.next):
            aux = Node(pointer.value).value
            Node(pointer.value).value = Node(pointer.value).next 
            Node(pointer.value).next = aux
        
        return self
    
    @reset_head_decorator
    def find_cycle(self):
        slow_pointer = self.head
        fast_pointer = self.head
        cycle = False
        while fast_pointer.next != None and not cycle:
            pass
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer.value == fast_pointer.value:
                cycle = True
        print("Cycle: ", cycle)
        return slow_pointer, fast_pointer if cycle else cycle
        
    def find_cycle_decorator(fun):
        def find_cycle_wrapper(self):
            pointers = self.find_cycle
            return self.fun(*pointers) if pointers != False else "There is no cycle."
        return find_cycle_wrapper
    
    @find_cycle_decorator
    def find_cycle_length(self, slow_pointer, fast_pointer):
        cycle_length = 0
        fast_pointer = fast_pointer.next
        while fast_pointer != slow_pointer:
            cycle_length += 1
            fast_pointer = fast_pointer.next
        print("Cycle length is: ", cycle_length)
        return cycle_length
    
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
    
    print(iterllist.node.value, iterllist.node.next.value) 
    next(iterllist)
    next(iterllist)
    next(iterllist)
    pass

if __name__ == "__main__":
    main()
    

        