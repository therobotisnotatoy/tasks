"""
559. Дано натуральное число n. Найти все меньшие n числа
Мерсена. (Простое число называется числом Мерсена, если оно может
быть представлено в виде 2^p – 1, где р – тоже простое число.)
"""


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


# get all natural numbers less than given position of "basic" Mersen sequence
def get_natural_numbers_limited_by_mersen_number(position: int) -> list[int]:

    target = pow(2, position) - 1

    return sieve_of_eratosthenes(target)


# get (limited) "basic" Mersen sequence
def get_mersen_number_limited_by_natural_number_1(limit: int):
    position = 1
    mersen = 1
    result = []

    while mersen < limit:
        position += 1
        result.append(mersen)
        mersen = pow(2, position) - 1

    return result


# get (limited) Mersen sequence with simple indexes
def get_mersen_number_limited_by_natural_number_2(limit: int) -> list[int]:

    result = []

    sieve = sieve_of_eratosthenes(limit)

    for natural_number in sieve:
        mermen_candidate = pow(2, natural_number) - 1
        if mermen_candidate >= limit:
            break
        else:
            result.append(mermen_candidate)

    return result


if __name__ == "__main__":

    print(get_mersen_number_limited_by_natural_number_1(8388608))
    print(get_mersen_number_limited_by_natural_number_2(8388608))

    print(get_natural_numbers_limited_by_mersen_number(1))
    print(get_natural_numbers_limited_by_mersen_number(2))
    print(get_natural_numbers_limited_by_mersen_number(3))
    print(get_natural_numbers_limited_by_mersen_number(4))
    print(get_natural_numbers_limited_by_mersen_number(5))
    print(get_natural_numbers_limited_by_mersen_number(6))
    print(get_natural_numbers_limited_by_mersen_number(7))
