#!/usr/local/bin/python3.7

class Stack:
    """Stack implementation using list"""
    def __init__(self, size = 10):
        self.__mStack = []
        self.__mSize = size
        print("Created stack with size: ", self.__mSize)

    def __del__(self):
        print("Stack destroyed")

    def isFull(self):
        return True if len(self.__mStack) == self.__mSize else False

    def isEmpty(self):
        return True if len(self.__mStack) == 0 else False

    def push(self, val):
        if not self.isFull():
            self.__mStack.append(val)
            return True
        return False

    def pop(self):
        if self.isEmpty():
            return False
        return self.__mStack.pop()

    def top(self):
        if self.isEmpty():
            return False
        return self.__mStack[-1]

    #def __bool__(self):
        #print("caling bool")
        #return True if len(self.__mStack) else False

    def __len__(self):
        print("caling len")
        return len(self.__mStack)

    def __repr__(self):
        return "Expected to return storable/reusable representation"

    def __str__(self):
        return "Expected to return string format"

    def __iter__(self):
        print("__iter__")
        self.index = len(self.__mStack) - 1
        print("Index ", self.index)
        return self

    def __next__(self):
        print("__next__ ", self.index)
        if self.index == -1:
            raise StopIteration
        i = self.index
        self.index -= 1
        return self.__mStack[i]

    """def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.__mStack):
            raise StopIteration
        self.index += 1
        return self.index"""

    def __getitem__(self, index):
        if index < 0 or index > (len(self.__mStack) - 1):
            raise IndexError
        return self.__mStack[index]

    def display(self):
        for i in self.__mStack:
            print("{} ".format(i), end="")
        print()

if __name__ == "__main__":
    s = Stack(10)
    print("Type of s is: ", type(s))
    #print(s.__mSize)   # This line will throw an error as we are trying to access private attribute
    print("Push numbers from 1 to 10 in stack")
    for i in range(1, 13):
        if not s.push(i):
            print("Failed to push {} in stack. Stack seems to be full", i)
    s.display()
    print("Top of stack: ", s.top())
    print("Pop 5 elements from stack")
    for _ in range(5):
        s.pop()
    s.display()
