def get_value(prompt):
    value = input(prompt).strip().lower()
    return 'x' if value == 'x' else float(value)

def solve_proportion(a1, a2, b1, b2):
    if a1 == 'x':
        return (b1 * a2) / b2
    if a2 == 'x':
        return (a1 * b2) / b1
    if b1 == 'x':
        return (a1 * b2) / a2
    if b2 == 'x':
        return (b1 * a2) / a1

def main():
    print("Solving a1/a2 = b1/b2")
    a1 = get_value("a1: ")
    a2 = get_value("a2: ")
    b1 = get_value("b1: ")
    b2 = get_value("b2: ")

    values = [a1, a2, b1, b2]
    if values.count('x') != 1:
        print("Exactly one value must be 'x'.")
        return

    try:
        result = solve_proportion(a1, a2, b1, b2)
        print("x=", result)
    except ZeroDivisionError:
        print("Cannot divide by 0.")

main()