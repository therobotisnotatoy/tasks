"""
87. Даны натуральное n, m. Получить сумму m последних цифр
числа n.
"""
import sys


# cut & sum the digit from tail of target number a given number of times
def get_sum_of_lasts_few(target: int, tail_size: int) -> int:

    if tail_size == 1:
        return target % 10
    else:
        tail_size -= 1
        return target % 10 + get_sum_of_lasts_few(target // 10, tail_size)


"""
to run from console try: python3 task_87.py n m
where n is natural number, 
m - number of digits to count the sum (from the end)
"""
if __name__ == "__main__":

    # Get console arguments
    args = [int(arg) for arg in sys.argv[1:] if (arg.isnumeric() and (int(arg) > 0))]

    # show the result
    print(get_sum_of_lasts_few(*args))
