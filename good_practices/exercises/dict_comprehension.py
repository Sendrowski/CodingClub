# Initialize the list of numbers
data = dict(a=1, b=2, c=3, d=4, e=5)

# Initialize an empty dictionary to store the results
result = dict()

# Loop over keys and values in the dictionary
for key, value in data.items():
    # If the value is not 1, square it and add it to the result
    if value != 1:
        result['_' + key] = value ** 2
    # If the value is 1, leave it as is
    else:
        result[key] = value

# TODO: Do the same using a dictionary comprehension
result2 = None

# Check that the results are the same
assert result == result2, f"Expected {result}, but got {result2}"

print("Exercise completed successfully!")
