import numpy as np


def fibonacci(max_value):
    fibonacciSequence = [1, 2]

    while fibonacciSequence[-1] < max_value:
        x = fibonacciSequence[-2]
        y = fibonacciSequence[-1]
        fibonacciSequence.append(x + y)

    return fibonacciSequence


fibonacciResutl = np.array(fibonacci(4e6))
fibonacciResutl = fibonacciResutl[fibonacciResutl % 2 == 0]

print(fibonacciResutl.sum())