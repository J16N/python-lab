class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print("Size of Stack:", my_stack.size())
print("Top element of Stack:", my_stack.peek())
print("Popped element of Stack:", my_stack.pop())
print("Size of Stack:", my_stack.size())