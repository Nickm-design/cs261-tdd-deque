# Deque: A deque.
# Your implementation should pass the tests in test_deque.py.
# Nick Morris

# Hint: pip3 install llist
from llist import dllist

class Deque:

    def __init__(self):
        self.data = dllist()

    def enqueue_left(self, value):
        self.data.appendleft(value)
    
    def enqueue_right(self, value):
        self.data.appendright(value)

    def dequeue_left(self):
        return self.data.popleft()