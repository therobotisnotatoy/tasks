"""559. Given a natural number n. Find all Mersenne numbers less than n .
(A prime number is called a Mersenne number if it can
be represented as 2^p - 1, where p is also a prime number.)
"""


def sieve_of_eratosthenes(target: int) -> list[int]:
    """Returns list of prime numbers (Eratosthenes Algorithm), less than target argument

    :param target: int
    :return: list[int]
    """

    # an list of Bool vales to index numbers 2 to n (0 to n-2)
    sieve = [True]*(target-1)
    # limit for loop
    limit = round(pow(target, 1/2))

    # sieve numbers
    for number in range(2, limit+1):
        if sieve[number-2]:
            for suspect in range(pow(number, 2), target+1, number):
                sieve[suspect-2] = False

    # get list of natural numbers
    result = [1]
    for pos, cell in enumerate(sieve):
        if cell:
            result.append(pos+2)

    return result


def get_mersenne_sequence_limited_by_natural_number(limit: int) -> list[int]:
    """Returns list of Mersenne numbers, less than limit argument

    :param limit: int
    :return: list[int]
    """
    result = []

    # get natural numbers list
    sieve = sieve_of_eratosthenes(limit)

    # form list of Mersenne numbers limited by given argument
    for natural_number in sieve:
        mersenne_candidate = pow(2, natural_number) - 1
        if mersenne_candidate >= limit:
            break
        else:
            result.append(mersenne_candidate)

    return result


def info() -> str:
    """Task & arguments description

    :return: str
    """

    info_string = ("Task 226. Function returns list of Mersenne numbers, less than argument n.\n"
                   "Please enter n (or 'R' to return to main menu): "
                   )

    return info_string


def run(n) -> list[int]:
    """Implementation of the task #559.

    :return: list[int]
    """

    return get_mersenne_sequence_limited_by_natural_number(n)
