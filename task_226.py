"""
226. Даны натуральные числа m, n. Получить все их
натуральные общие кратные, меньшие mn.
"""
import sys


# return all natural common multiples less than first_arg * second_arg
def get_natural_common_multiples(first_arg: int, second_arg: int) -> list[int]:

    limit = first_arg * second_arg
    suspect = second_arg
    result = []
    while suspect < limit:
        if suspect % first_arg == 0:
            result.append(suspect)
        suspect += second_arg

    return result


"""
to run from console try: python3 task_226.py n m
where n and m are natural numbers
"""
if __name__ == "__main__":

    try:
        # Get console arguments
        args = [int(arg) for arg in sys.argv[1:] if (arg.isnumeric() and (int(arg) > 0))]

        # show the result
        print(get_natural_common_multiples(*args))

    except TypeError:
        print("Wrong input. You need to enter natural numbers")
