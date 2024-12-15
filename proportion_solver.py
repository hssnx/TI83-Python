from typing import Union

def get_value(prompt: str) -> Union[float, str]:
    """
    Prompt the user for input.
    Return 'x' if the user enters 'x', otherwise convert the input to a float.
    """
    while True:
        value = input(prompt).strip()
        if value.lower() == 'x':
            return 'x'
        try:
            return float(value)
        except ValueError:
            print("Invalid input! Please enter a number or 'x'.")

def solve_proportion(a1, a2, b1, b2):
    """
    Solve for the unknown in the proportion a1 / a2 = b1 / b2.
    """
    if a1 == 'x':
        return (b1 * a2) / b2
    elif a2 == 'x':
        return (a1 * b2) / b1
    elif b1 == 'x':
        return (a1 * b2) / a2
    elif b2 == 'x':
        return (b1 * a2) / a1
    else:
        raise ValueError("One value must be 'x'.")

def main():
    print("Solving the proportion a1/a2 = b1/b2")
    a1 = get_value("Enter a1: ")
    a2 = get_value("Enter a2: ")
    b1 = get_value("Enter b1: ")
    b2 = get_value("Enter b2: ")

    # Ensure exactly one value is 'x'
    values = [a1, a2, b1, b2]
    if values.count('x') != 1:
        print("Error: Exactly one value must be 'x'.")
        return

    try:
        result = solve_proportion(a1, a2, b1, b2)
        print(f"The value of the unknown is: {result:.5f}")
    except ZeroDivisionError:
        print("Error: Division by zero occurred.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()