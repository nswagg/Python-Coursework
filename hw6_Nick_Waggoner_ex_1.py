"""
Homework 6, Exercise 1
Nick Waggoner
11-23-2021
Description: a modification of the slowDown function: uses another
external decorator to set the amount of time the system sleeps before
counting down in the function. Will accept 1 or 0 arguments to the
@sleepTimer decorator
"""
import functools
import time

def sleepTimer(timer=1):
    def slowDown(func):
        """Sleep 1 second before calling the function by default """
        @functools.wraps(func)
        def wrapperSlowDown(*args, **kwargs):
            time.sleep(timer)
            return func(*args, **kwargs)
        return wrapperSlowDown
    return slowDown


@sleepTimer(timer=4) #How long the program pauses in seconds for the decorator
def countdown(fromNumber):
    if fromNumber < 1:
        print("Liftoff!")
    else:
        print(fromNumber)
        countdown(fromNumber - 1)


countdown(5)
# 5
# 4
# 3
# 2
# 1
# Liftoff!
