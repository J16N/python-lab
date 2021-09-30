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
print("-" * 10, "STACK OPERATIONS", "-" * 10)
print("-" * 25)
print("<1> To Insert Data.")
print("<2> To Pop Data.")
print("<3> Display the top element.")
print("<0> Exit")

while ((op := int(input())) != 0):
    if (op == 1):
        data = int(input("Enter the data: "))
        my_stack.push(data)
    
    elif (op == 2):
        try:
            print("Popped element is: ", my_stack.pop())
        except:
            print("!!! Stack Underflow !!!")

    elif (op == 3):
        print("Top element is: ", my_stack.peek())
    
    else:
        print("Invalid Option")
