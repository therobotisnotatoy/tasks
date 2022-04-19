"""
87. Даны натуральное n, m. Получить сумму m последних цифр
числа n.
"""


def get_sum_of_lasts_few_by_recursion(target: int, tail_size: int) -> int:

    if tail_size == 1:
        return target % 10
    else:
        tail_size -= 1
        return target % 10 + get_sum_of_lasts_few_by_recursion(target // 10, tail_size)


def get_sum_of_lasts_few(target: int, tail_size: int) -> int:

    tail = target % pow(10, tail_size)
    result = 0

    while tail > 0:
        result += tail % 10
        tail //= 10
    return result


if __name__ == "__main__":

    print(get_sum_of_lasts_few_by_recursion(1111111, 11))
    print(get_sum_of_lasts_few(1111111, 11))
    print(get_sum_of_lasts_few_by_recursion(1111151, 4))
    print(get_sum_of_lasts_few(1111151, 4))
    print(get_sum_of_lasts_few_by_recursion(9911771, 3))
    print(get_sum_of_lasts_few(9911771, 3))
    print(get_sum_of_lasts_few_by_recursion(1113451, 5))
    print(get_sum_of_lasts_few(1113451, 5))
    print(get_sum_of_lasts_few_by_recursion(1113451, 1))
    print(get_sum_of_lasts_few(1113451, 1))
