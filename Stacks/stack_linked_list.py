class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next


class StackLinkedList:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def push(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size += 1

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return
        e = self._top._element
        self._top = self._top._next
        return e

    def top(self):
        if self.isempty():
            print("Stack is empty")
            return
        return self._top._element

    def display(self):
        p = self._top
        while p:
            print(p._element,end='-->')
            p = p._next
        print()

S = StackLinkedList()
S.push(5)
S.push(3)
print('Length', len(S))
S.display()
print(S.pop())
print(S.isempty())
S.display()
S.pop()
S.push(7)
S.push(9)
S.push(12)
S.display()
print(S.top())
S.display()
