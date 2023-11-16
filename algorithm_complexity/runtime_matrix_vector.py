import time

import matplotlib.pyplot as plt
import numpy as np


def run(n: int) -> float:
    """
    Return the time taken to perform random matrix-vector multiplication.

    :param n: Size of the matrix and vector
    :return: Time taken to perform matrix-vector multiplication
    """
    # generate a random n x n matrix and a random vector of size n
    M = np.random.rand(n, n)
    v = np.random.rand(n)

    # record the start time
    start_time = time.time()

    # perform matrix-vector multiplication
    _ = M @ v

    # calculate the time taken
    return time.time() - start_time


# Choose a range of matrix sizes
matrix_sizes = range(1, 1000, 5)

# Measure runtime for each matrix size
runtimes = np.array([run(n) for n in matrix_sizes])

# Remove outliers
runtimes[runtimes > 0.001] = np.nan

# Plotting
plt.plot(matrix_sizes, runtimes, marker='o')

plt.xlabel('matrix size (n x n)')
plt.ylabel('runtime (seconds)')
plt.title('runtime')
plt.grid(True)

plt.show()

pass
