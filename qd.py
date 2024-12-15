from sympy import symbols, Eq, sympify, solve, simplify

def solve_equation(equation_str):
    """
    Parse and solve a given equation for x.
    
    This function takes an equation string, which may be of the form:
    - "2x^2 + 4x + 2 = 0"
    - "x^2 + 2x + 1"
    - "sin(x) = 1/2"
    - "exp(x) - 5 = 0"
    - "x^3 - 2*x + 1 = 0"
    And many other forms that Sympy can understand.
    
    If no '=' is found, it's assumed the equation is equal to zero.
    Example: "x^2+2x+1" is treated as "x^2+2x+1=0".
    
    Parameters
    ----------
    equation_str : str
        The equation as a string.
    
    Returns
    -------
    dict
        A dictionary containing:
        - "equation": The Sympy Eq object.
        - "solutions": A list of solutions found by Sympy.
    
    Raises
    ------
    ValueError
        If the equation is invalid or cannot be parsed.
    """
    
    # Define the variable:
    x = symbols('x', complex=True)
    
    # Clean the input string (remove extra spaces):
    equation_str = equation_str.replace(" ", "")
    
    # If no '=' sign is present, assume "=0"
    if '=' not in equation_str:
        equation_str = equation_str + "=0"
    
    # Split into left and right parts
    left_part, right_part = equation_str.split('=')
    
    # Attempt to parse with sympify
    try:
        left_expr = sympify(left_part)
        right_expr = sympify(right_part)
    except Exception as e:
        raise ValueError(f"Invalid equation. Could not parse. Details: {e}")
    
    # Create the equation Eq(...)
    eq = Eq(left_expr, right_expr)
    
    # Attempt to solve the equation for x
    solutions = solve(eq, x, dict=True)
    
    # 'solve' can return a list of solution mappings. If so, extract the values for x.
    # If solve returns a direct list of solutions (not a dict), handle that too.
    extracted_solutions = []
    if all(isinstance(sol, dict) for sol in solutions):
        # If solutions are in the form [{x: value}, ...]
        for sol_dict in solutions:
            extracted_solutions.append(sol_dict[x])
    else:
        # If solutions are direct expressions
        extracted_solutions = solutions
    
    # Simplify the solutions if possible
    simplified_solutions = [simplify(s) for s in extracted_solutions]

    return {
        "equation": eq,
        "solutions": simplified_solutions
    }

if __name__ == "__main__":
    # Example usage:
    test_equation = "2x^2 + 4x + 2 = 0"
    result = solve_equation(test_equation)
    print("Equation:", result["equation"])
    print("Solutions:", result["solutions"])
    
    # Another example: "sin(x) = 1/2"
    test_equation_2 = "sin(x) = 1/2"
    result2 = solve_equation(test_equation_2)
    print("Equation:", result2["equation"])
    print("Solutions:", result2["solutions"])
