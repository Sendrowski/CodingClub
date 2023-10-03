# TODO: Improve the function below by using pythonic comparisons,
#  f-strings and more streamlined logic.
def get_status_string(status: bool | None, name: str) -> str:
    """
    Print the status of a variable.

    :param status: Status of the variable
    :param name: Name of the variable
    :return: String with the status of the variable
    """
    if status == None:
        return "Unknown status"

    elif status == True:
        return name + " is True"

    elif status == False:
        return name + " is False"


assert get_status_string(True, "test") == "test is True"
assert get_status_string(False, "test") == "test is False"
assert get_status_string(None, "test") == "Unknown status"
