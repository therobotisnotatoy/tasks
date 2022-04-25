
def reverse_number(number: int) -> int:
    """Returns reversed number
    Keyword arguments:
    number -- integer, given number"""
    assert isinstance(number, int), "Number should be integer"
    assert number > 0, "Number should be greater than 0"

    return int(str(number)[::-1])


def task_88b() -> None:
    """Implementation of the task #88b."""
    try:
        # User's input
        n = int(input("Enter n: "))

        # Prints result
        print(f"Reversed {n} is {reverse_number(n)}")

    # If user's input is invalid
    except ValueError:
        print("Wrong input!")
        