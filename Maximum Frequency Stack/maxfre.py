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


class FreqStack:
    def __init__(self):
        self.stack = Stack()
        self.freq = {}

    def push(self, val: int) -> None:
        self.stack.push(val)
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1

    def pop(self) -> int:
        max_freq = max(self.freq.values())
        current = self.stack.head
        prev = None
        while current:
            if self.freq[current.data] == max_freq:
                if prev:
                    prev.next = current.next
                else:
                    self.stack.head = current.next
                self.freq[current.data] -= 1
                if self.freq[current.data] == 0:
                    del self.freq[current.data]
                return current.data
            prev = current
            current = current.next
