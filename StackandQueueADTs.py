from collections import deque

class MyQueue:
    '''Basic Queue implementation, enqueue adds item to end of queue, dequeue removes and returns the item from the front of the queue, emtpy returns True
    if queue is empty, False otherwise, front returns the value at the front of the queue.'''
    def __init__(self, datatype):
        #initializes empty list 'items'
        self.queue = deque()
        self.datatype = datatype

    def enqueue(self, item):
        #adds items to the end of 'items' queue
        self.queue.append(item)

    def dequeue(self):
        #removes and returns first 'items' from front of queue
        return self.queue.popleft()

    def empty(self):
        #retuns true if empty and false otherwise
        return len(self.queue) == 0

    def front(self):
        return self.queue[0]


class MyStack:
    '''Basic Stack implementation, push adds item to top of stack, pop removes and returns the item from the top of stack, emtpy returns True
        if queue is empty, False otherwise, top returns the value at the top of the stack.'''
    def __init__(self, datatype):
        self.stack = []
        self.datatype = datatype

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        return self.stack.pop(0)

    def top(self):
        return self.stack[0]

    def empty(self):
        return len(self.stack) == 0

# Testing code for stack
s = MyStack(int)
print(s.empty())
s.push(5)
s.push(8)
print(s.pop())
s.push(3)
print(s.empty())
print(s.top())
print(s.pop())
print(s.pop())
print(s.pop())

# Testing code for Queue
s = MyStack(int)
print(s.empty())
s.push(5)
s.push(8)
print(s.pop())
s.push(3)
print(s.empty())
print(s.top())
print(s.pop())
print(s.pop())
print(s.pop())