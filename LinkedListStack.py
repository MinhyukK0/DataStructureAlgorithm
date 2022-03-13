from typing import Any


class ListNode:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item: Any):
        self.last = ListNode(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

adt = Stack()
for i in range(5):
    adt.push(i)

for i in range(5):
    print(adt.pop())

