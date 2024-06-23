class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def push(self, value):
        if not self.is_full():
            self.stack.append(value)
        else:
            print("Stack is full. Cannot push more elements.")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty. Cannot pop element.")
            return None

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty. No top element.")
            return None


stack1 = MyStack(capacity=5)

stack1.push(1)

stack1.push(2)

print(stack1.is_full())
# Output: False

print(stack1.top())
# Output: 2

print(stack1.pop())
# Output: 2

print(stack1.top())
# Output: 1

print(stack1.pop())
# Output: 1

print(stack1.is_empty())
# Output: True
