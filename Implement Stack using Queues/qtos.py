class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

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


class MyStack:
    def __init__(self):
        self.queue = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.queue.push(x)
        while not self.queue2.empty():
            self.queue.push(self.queue2.pop())
        self.queue, self.queue2 = self.queue2, self.queue

    def pop(self) -> int:
        return self.queue2.pop()

    def top(self) -> int:
        return self.queue2.peek()

    def empty(self) -> bool:
        return self.queue2.empty()
