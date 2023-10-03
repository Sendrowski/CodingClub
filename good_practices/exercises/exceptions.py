import os


def read_file_without_exceptions(filename: str) -> str | None:
    """
    Read a file and return its contents as a string.

    :param filename: The name of the file to read.
    :return: The contents of the file as a string or None if the file does not exist.
    """
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()


# TODO: Reimplement the function above using a try-except block.
#   Raise a RuntimeError if the file does not exist.
def read_file_without_exceptions2(filename: str) -> str:
    """
    Read a file and return its contents as a string.

    :param filename: The name of the file to read.
    :return: The contents of the file as a string
    :raises RuntimeError: If the file does not exist.
    """
    pass


# Check that the functions work as expected by reading this file
assert read_file_without_exceptions(__file__) == read_file_without_exceptions2(__file__)

# Make sure an exception is thrown if the file does not exist.
# Note that we would normally use pytest.raises() for this, but we haven't learned about pytest yet.
# Also note that open() normally throws a FileNotFoundError by default
exception_thrown = False

try:
    read_file_without_exceptions2('does_not_exist.txt')
except RuntimeError:
    exception_thrown = True
except Exception:
    raise AssertionError("Expected a RuntimeError to be thrown, but got a different exception.")

assert exception_thrown, "Expected a RuntimeError to be thrown, but nothing happened."

print("Exercise completed successfully!")
