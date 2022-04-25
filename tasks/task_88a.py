
def is_3_in_square_of_number(number: int) -> bool:
    """Returns True if 3 is in square of number

    Keyword arguments:
    number -- integer, given number
    """
    assert isinstance(number, int), "Number should be integer"
    assert number > 0, "Number should be greater than 0"

    return '3' in str(number*number)


def task_88a() -> None:
    """Implementation of the task #88a."""
    try:
        # User input
        n = int(input("Enter n: "))

        # Check if 3 is in number squared
        if is_3_in_square_of_number(n):
            print(f"There is 3 in squared {n} ({n*n})")
        else:
            print(f"There isn't 3 in squared {n} ({n*n})")

    # If user's input is invalid
    except ValueError:
        print("Wrong input!")
