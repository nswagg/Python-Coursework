"""
 Nick Waggoner
 Final Question 6
 Description: This program uses a decorator to convert a string to all uppercase
"""
import functools

value = "Hello World!"
test2 = "You only live once, but if you do it right, once is enough. - Mae West "

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        upper = str(func(*args, **kwargs)).upper()
        return upper
    return wrapper


@uppercase
def stringUp(val):
    return val

print(stringUp(value))
print(stringUp(test2))
