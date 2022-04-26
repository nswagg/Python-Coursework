# Nick Waggoner
# Final Question 5
import random

n = random.randint(1,10)


def negOdd(n):
    """Generator to return first n negative numbers"""
    i = 1
    count = 0
    while count < n:
        yield i * (-1)
        count += 1
        i += 2


print(f"The first {n} negative numbers are: ", end="")

for i in negOdd(n):
    print(i, end=" ")
