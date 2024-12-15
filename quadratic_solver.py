from math import sqrt
from typing import Tuple, Union, List

def get_float(prompt: str) -> float:
    """Prompt the user for input until a valid float is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def solve_quadratic(a: float, b: float, c: float) -> Union[List[float], List[complex]]:
    """
    Solve the quadratic equation ax^2 + bx + c = 0 and return solutions.
    Returns a list of either:
        - Two float solutions if the discriminant is positive
        - One float solution if the discriminant is zero
        - Two complex solutions if the discriminant is negative
    """
    delta = b**2 - 4*a*c
    
    if delta > 0:
        # Two distinct real solutions
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        return [x1, x2]
    elif delta == 0:
        # One real solution
        x0 = -b / (2 * a)
        return [x0]
    else:
        # Complex solutions
        real_part = -b / (2 * a)
        imag_part = sqrt(-delta) / (2 * a)
        return [real_part + imag_part*1j, real_part - imag_part*1j]

def main():
    a = get_float("Enter a: ")
    while a == 0:
        print("Coefficient 'a' cannot be zero for a quadratic equation.")
        a = get_float("Enter coefficient a (non-zero): ")
    
    b = get_float("Enter b: ")
    c = get_float("Enter c: ")

    solutions = solve_quadratic(a, b, c)
    
    # Print results
    delta = b**2 - 4*a*c
    print(f"Δ = {delta}")
    
    if len(solutions) == 2 and isinstance(solutions[0], complex):
        # Complex solutions
        print(f"Two complex solutions: \n x1 = {solutions[0]} \n x2 = {solutions[1]}")
    elif len(solutions) == 2:
        # Two real solutions
        print(f"Two real solutions: \n x1 = {solutions[0]:.5f} \n x2 = {solutions[1]:.5f}")
    else:
        # One real solution
        print(f"One real solution: x0 = {solutions[0]:.5f}")

if __name__ == "__main__":
    main()