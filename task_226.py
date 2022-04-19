"""
226. Даны натуральные числа m, n. Получить все их
натуральные общие кратные, меньшие mn.
"""


def get_natural_common_multiples(first_arg: int, second_arg: int) -> list[int]:

    limit = first_arg * second_arg
    suspect = second_arg
    result = []
    while suspect < limit:
        if suspect % first_arg == 0:
            result.append(suspect)
        suspect += second_arg

    return result


if __name__ == "__main__":

    print(get_natural_common_multiples(11, 22))
    print(get_natural_common_multiples(22, 11))
    print(get_natural_common_multiples(2, 6))
    print(get_natural_common_multiples(6, 2))
    print(get_natural_common_multiples(17, 13))
    print(get_natural_common_multiples(13, 17))
