"""
Homework 6, Exercise 2
Nick Waggoner
11-23-2021
Description: The program uses a decorator to store the results of the fibonacci
function call in order to save storage and improve runtime.

The countCalls decorator demonstrates how the cache decorator reduces the number of
function calls required to run the fibonnaci function. Even to run fibonacci
for the first 5 values, the cache reduces the number of calls almost in half.
"""
import functools

def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)

    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls

def cache(func):
    """Stores previous calls in a dictionary to reduce compute time"""
    cache = {}

    @functools.wraps(func)
    def wrapperCache(*args, **kwargs):
        #need to append values to a cache
        if args not in cache: #if our value does not exist in the cache, append and move on
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return wrapperCache

@countCalls
@cache
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num-1) + fibonacci(num-2)

@countCalls
def fibNoCache(num):
    if num < 2:
        return num
    return fibNoCache(num-1) + fibNoCache(num-2)

print("Calling with the dictionary cache:")
fibonacci(5)
print()
print("Calling without the cache:")
fibNoCache(5)