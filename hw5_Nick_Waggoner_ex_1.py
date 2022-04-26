"""
    Homework 5, Exercise 1
    Nick Waggoner
    11-7-2021
    Description: This is an iterator class that iterates backwards through a list
"""


class ReverseIter:
    def __init__(self, val):
        self.list = val
        self.count = len(val) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= 0:
            result = self.list[self.count]
            self.count -= 1
            # print(result) #Used for testing results
            return result
        else:
            StopIteration()


it = ReverseIter([1, 2, 3, 4])
next(it)
next(it)
next(it)
next(it)
