from typing import Generator

import numpy as np


def is_prime(num: int) -> bool:
    """
    Check if a number is prime.

    :param num: The number to check.
    :return: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        # check for divisibility
        if num % i == 0:
            return False

    return True


def prime_generator() -> Generator[int, None, None]:
    """
    Yield prime numbers indefinitely by returning a generator.

    :return: A generator of prime numbers.
    """
    # TODO: Implement this function
    pass


# Get generator of prime numbers
generator = prime_generator()

# Check that we have a generator
assert isinstance(generator, Generator), "prime_generator() should return a generator"

# Assert 10 first prime numbers
np.testing.assert_array_equal([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], [next(generator) for _ in range(10)])

print("Exercise completed successfully!")
