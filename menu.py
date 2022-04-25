"""Menu implementation"""
from inspect import signature

from tasks import (task_87, task_226, task_559, task_test)


def main():
    """
    Menu implementation
    """
    # Dictionary of tasks. Key - task number, value - function of that task
    tasks_dict = {
        "Enter 'E' to exit": exit,
        "87": task_87,
        "226": task_226,
        "559": task_559,
        "T": task_test,
    }

    # Main loop
    while True:

        # Print available tasks
        print("*" * 24, "MAIN MENU", "*" * 25)
        print("Available tasks: ")
        print(", ".join(list(tasks_dict.keys())))
        print("*" * 60)

        try:
            task_number = input("Input task`s number: ").upper()

            # Exit from main loop
            if task_number == "E":
                break

            # Get the module by input
            func = tasks_dict[task_number]

        except KeyError as ex:
            print(f"Input correct task`s number, task {ex} does not exist: ")
            continue

        # Task loop
        while True:
            try:
                # Get number of arguments needed for task run() function
                expected_args_count = len(signature(func.run).parameters)
                if expected_args_count < 1:
                    # Show module info & call function without arguments
                    print("-" * 60)
                    print(func.info())
                    print("-" * 60)
                    print("Result: ", func.run())
                    break
                else:
                    # Show module info & get arguments (or "exit" key)
                    print("-" * 60)
                    user_input = input(func.info()).upper()
                    # Exit from task loop
                    if user_input == "R":
                        break
                    # Get arguments (you validation function could be here)
                    args = [int(arg) for arg in user_input.split(" ") if (arg.isnumeric() and (int(arg) > 0))]
                    # Validate number of parameters
                    assert(expected_args_count == len(args))

                    print("-" * 60)

                    # Get the result
                    print("Result: ", func.run(*args))

            except (TypeError, AssertionError):
                print("-" * 60)
                print(f"The type or number of arguments is not suitable for this task. Pleas try again.")
                continue


if __name__ == "__main__":
    main()
