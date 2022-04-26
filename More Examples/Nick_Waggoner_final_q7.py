# Nick Waggoner
# Final Question 7

import threading
import random
import time

numThreads = 2
threads = []  # list of thread objects
n = random.randint(10,20)

def printCube(number):
    """Prints the first n cubes"""
    startTime = time.perf_counter()
    print(f'\nThe first {number} cubes:', end=" ")
    for x in range(number):
        out = x * x * x
        print(out, end=" ")
    endTime = time.perf_counter()
    print("\nprintCube({}) took {:.4f} to finish".format(number, endTime-startTime))


def printSquare(number):
    """Prints the first n squares"""
    startTime = time.perf_counter()
    print(f'\nThe first {number} squares:', end=" ")
    for x in range(number):
        out = x * x
        print(out, end=" ")
    endTime = time.perf_counter()
    print("\nprintSquare({}) took {:.4f} to finish".format(number, endTime-startTime))

thread1 = threading.Thread(printCube(n))
threads.append(thread1)
thread1.start()

thread2 = threading.Thread(printSquare(n))
threads.append(thread2)
thread2.start()

# Wait for each thread to finish
for threader in threads:
    threader.join()
print('\nDone.')  # Prints after all threads have halted
