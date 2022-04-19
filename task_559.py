"""
559. Дано натуральное число n. Найти все меньшие n числа
Мерсена. (Простое число называется числом Мерсена, если оно может
быть представлено в виде 2^p – 1, где р – тоже простое число.)
"""
import sys


# Sieve of Eratosthenes Algorithm
def sieve_of_eratosthenes(target: int) -> list[int]:

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


# get (limited) Mersen sequence with simple indexes
def get_mersen_sequence_limited_by_natural_number(limit: int) -> list[int]:

    result = []

    sieve = sieve_of_eratosthenes(limit)

    for natural_number in sieve:
        mermen_candidate = pow(2, natural_number) - 1
        if mermen_candidate >= limit:
            break
        else:
            result.append(mermen_candidate)

    return result


"""
to run from console try: python3 task_559.py n
where n is natural number
"""
if __name__ == "__main__":

    try:
        # Get console arguments
        args = [int(arg) for arg in sys.argv[1:] if (arg.isnumeric() and (int(arg) > 0))]

        # show the result
        print(get_mersen_sequence_limited_by_natural_number(*args))

    except TypeError:
        print("Wrong input. You need to enter natural number")

