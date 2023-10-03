import numpy as np

# Initialize the list of numbers
numbers = [1, 2, 3, 4, 5]

# Initialize an empty list to store the results
result = []

# Loop over each number in the list
for num in numbers:
    # If the number is even, square it
    if num % 2 == 0:
        result.append(num ** 2)
    # If the number is odd, leave it as is
    else:
        result.append(num)

# TODO: Do the same using a list comprehension
result2 = None

# Check that the results are the same
np.testing.assert_array_equal(result, result2)

print("Exercise completed successfully!")
