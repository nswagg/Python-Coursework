"""
    Homework 5, Exercise 2
    Nick Waggoner
    11-7-2021
    Description: This program uses a generator expression to calculate Pythagorean triples.
    Using the take() function, our program will run until it creates "n" yields. Thus, as is,
    the program will create a list of 10 tuples, which contain values for pythagorean triples
"""


def genrange(stop, start=0, step=1):
    """Implemented from part three for memory efficiency"""
    # stop is not included in the range
    x = start
    if step == 0:
        print("Step may not be 0")
    elif stop < start and step < 0:
        # Deals with negative case
        while x > stop:
            yield x
            x = x + step
    elif start < stop and step > 0:
        # Deals with working positive case
        while x < stop:
            yield x
            x = x + step
    else:
        print("Invalid input arguments")

def integers():
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1


def take(n, seq):
    """Returns first n values from the given sequence."""
    # Just in case it is an iterable object,
    # not a generator or iterator
    seq = iter(seq)

    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

""" #This is our generator prototype for pyt2. How to condense this into one line?
def pyt():
    c, m = 0, 2
    limits = 100
    # Limiting c would limit
    # all a, b and c
    while c < limits:

        # Now loop on n from 1 to m-1
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n

            # if c is greater than
            # limit then break it
            if c > limits:
                break

            print(a, b, c)

        m = m + 1
"""
pyt = ((x,y,z) for x in genrange(1000) for y in genrange(1000) for z in genrange(1000) if x*x + y*y == z*z and z != y and x != y and x > 0 and y > x)

'''
#Other prototype 
pyt2 = ((m * m - n * n, 2 * m * n, m * m + n * n) for m in integers() for n in range(1, m))
'''

print(take(10, pyt))
