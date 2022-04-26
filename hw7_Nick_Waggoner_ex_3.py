"""
    Homework 7, Exercise 3
    Nick Waggoner
    12-8-2021
    Description: The program creates an arbitrary number of threads defined by the
    user and executes a function and running DEBUG logging with each thread before
    pausing and terminating.

"""

import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(lineno)s - %(message)s')

threads = []  # list of thread objects

# Function called by each thread as they are running
def someFunc(i):
    i = int(i)
    logging.debug(f'Welcome thread {i}')
    if i % 2 == 0:
        logging.debug(f'Number {i} is even')
    else:
        logging.debug(f'Number {i} is odd')

    time.sleep(3)  # sleep for three seconds
    logging.debug(f'Goodbye thread {i}')


# Request an integer from the user for the number of threads
while True:
    numThreads = int(input('Please provide the number of threads to run:'))

    # Validate user input
    if type(numThreads) == int and numThreads >= 2:
        break
    else:
        print('Input is not valid. Please insert a number greater than 2')
        #could raise exception, but it will be easier not to right now.

# For loop to have each thread call someFunc
for x in range(0, numThreads):
    threader = threading.Thread(target=someFunc, args=[x])
    threads.append(threader)
    threader.start()

# Wait for each thread to finish
for threader in threads:
    threader.join()
print('Done.')  # Prints after all threads have halted
