"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
  ---Static implementation uses arrays to create a stack. Static implementation is though an effortless technique but is not a flexible way of creation, as the declaration of the size of the stack has to be done during program design, after that the size cannot be varied. Additionally, static implementation is not very efficient regarding memory utilization. Since an array (for implementing stack) is declared before the start of the operation (at program design time).
  Now if the number of elements to be sorted is very less in the stack the statically allocated memory will be wasted. On the other hand, if there are more number of elements to be stored in the stack then, we can’t be able to change the size of the array to increase its capacity, so that it can accommodate new elements.
  ---Dynamic implementation is also called linked list representation and uses pointers to implement the stack type of data structure.
"""

from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size >= 1:
            value = self.storage.remove_tail()
            self.size -= 1
            return value
