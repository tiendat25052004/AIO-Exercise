class MyQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def enqueue(self, value):
        if not self.is_full():
            self.queue.append(value)
        else:
            print("Queue is full. Cannot enqueue more elements.")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty. Cannot dequeue element.")
            return None

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty. No front element.")
            return None


# Test the implementation
queue1 = MyQueue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())
# Output: False

print(queue1.front())
# Output: 1

print(queue1.dequeue())
# Output: 1

print(queue1.front())
# Output: 2

print(queue1.dequeue())
# Output: 2

print(queue1.is_empty())
# Output: True
