"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   ---Static implementation: If a queue is implemented using arrays, the exact number of elements we want to store in the queue must be assured prior, because the size of the array has to be declared at design time or before the processing starts.
   In this case, the beginning of the array will become the front of the queue, and the last location of the array will act as the rear of the queue. The following relation gives the whole elements    exist in the queue when implemented using arrays:
   front – rear + 1
   If “rear < front” then there will be no element in the queue or queue will always be empty.
   ---Dynamic implementation: Implementing queues using pointers, the main disadvantage is that a node in a linked representation consumes more memory space than a corresponding element in the array    representation.
   Since there are at least two fields in each node one for the data field and other to store the address of the next node whereas in linked representation only data field is there.The merit of using    the linked representation becomes obvious when it is required to insert or delete an element in the middle of a group of other elements.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from singly_linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size >= 1:
            value = self.storage.remove_head()
            self.size -= 1
            return value
