from custom_exceptions import EmptyStackException, FullStackException

class Stack:
    def __init__(self, limit):
        self.storage = []
        self.limit = limit

    def push(self, item):
        if len(self.storage) >= self.limit:
            raise FullStackException('The stack is full!')
        self.storage.append(item)

    def getitems(self):
        return self.storage

    def pop(self):
        if len(self.storage) <= 0:
            raise EmptyStackException('You cannot pop from an empty stack!')

        return_value = self.storage[-1]
        self.storage.remove(return_value)

        return return_value

    def __len__(self):
        return len(self.storage)
