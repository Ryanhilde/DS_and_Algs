class StackArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return
        return self._data.pop()

    def top(self):
        if self.isempty():
            print("Stack is empty")
            return
        return self._data[-1]


S = StackArray()
print(S.isempty())
S.push(5)
S.push(3)
print(S._data)
print("Size:", len(S))
print(S.pop())
print(S.isempty())
