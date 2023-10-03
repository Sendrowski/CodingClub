# import the Callable type hint for functions
from typing import Callable


# Function without type hints
def add(a, b):
    """
    Add two integers together.
    """
    return a + b


# TODO: Write same function with integer type hints for arguments and return value
def add2(a, b):
    pass


def assert_has_valid_type_hints(func: Callable) -> None:
    """
    Check that a function has integer type hints for all arguments and the return value.

    :param func: The function to check.
    """
    annotations = func.__annotations__

    # Check for arguments' type hints
    for arg in func.__code__.co_varnames:
        assert arg in annotations, f"Argument '{arg}' lacks type hint."
        assert annotations[arg] == int, f"Argument '{arg}' has wrong type hint."

    # Check for return type hint
    assert 'return' in annotations, f"Function '{func.__name__}' lacks return type hint."
    assert annotations['return'] == int, f"Function '{func.__name__}' has wrong return type hint."


# check that add2 has valid type hints
assert_has_valid_type_hints(add2)

# make sure that add2 works as expected
assert add2(1, 2) == 3, f"Expected 3, but got {add2(1, 2)}"

print("Exercise completed successfully!")
