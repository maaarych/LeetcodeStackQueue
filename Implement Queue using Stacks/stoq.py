class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        pop_el = self.head.data
        self.head = self.head.next
        return pop_el

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def empty(self):
        return self.head is None


class MyQueue:
    def __init__(self):
        self.stack = Stack()
        self.stack2 = Stack()

    def push(self, x: int) -> None:
        self.stack.push(x)

    def pop(self) -> int:
        if self.stack2.empty():
            while not self.stack.empty():
                self.stack2.push(self.stack.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2.empty():
            while not self.stack.empty():
                self.stack2.push(self.stack.pop())
        return self.stack2.peek()

    def empty(self) -> bool:
        return self.stack.empty() and self.stack2.empty()
