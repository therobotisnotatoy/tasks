
def get_number_with_largest_sum_of_divisors(a: int, b: int) -> int:
    """Returns number with the largest sum of divisors within range (a, b)
    Keyword arguments:
    a -- integers, start point of the loop
    b -- integers, end point of the loop
    """
    assert isinstance(a, int) and isinstance(b, int), "Boundaries (a and b) should be integers"
    assert b >= a, "Second (b) argument should be bigger than first (a)"

    # List of all sums of divisors
    list_of_sums = [sum(get_divisors_list(number)) for number in range(a, b)]
    # Get the largest sum in list
    max_sum = max(list_of_sums)

    # Get number with the largest sum of divisors
    # Works, while a = 1, b => a
    number_with_max_sum = list_of_sums.index(max_sum) + 1

    return number_with_max_sum


def get_divisors_list(number: int) -> list:
    """Returns list of number divisors
    Keyword arguments:
    number -- integer, given number
    """
    assert isinstance(number, int), "Number should be integer"
    assert number > 0, "Number should be greater than 0"

    return [i for i in range(1, int(number/2) + 1) if number % i == 0] + [number]


def task_322() -> None:
    """Implementation of the task #322"""
    # Set boundaries
    a = 1
    b = 10000

    # Get number with the largest sum of divisors
    # and its divisors list
    number = get_number_with_largest_sum_of_divisors(a, b)
    div_list = get_divisors_list(number)

    # Print solution
    print(f"Number {number} has largest sum of dividers")
    print(f"Sum: {sum(div_list)}")
    print(f"Dividers: {div_list}")
