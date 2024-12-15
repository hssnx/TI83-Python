def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a numeric value.")

def solve_quadratic(a,b,c):
    d=b*b-4*a*c
    if d>0:
        x1=(-b+(d**0.5))/(2*a)
        x2=(-b-(d**0.5))/(2*a)
        return [x1,x2]
    elif d==0:
        return [-b/(2*a)]
    else:
        r=-b/(2*a)
        i=((-d)**0.5)/(2*a)
        return [r+i*1j,r-i*1j]

def main():
    a=get_float("Enter a: ")
    while a==0:
        print("Coefficient 'a' cannot be zero for a quadratic equation.")
        a=get_float("Enter a: ")
    b=get_float("Enter b: ")
    c=get_float("Enter c: ")
    s=solve_quadratic(a,b,c)
    d=b*b-4*a*c
    print("Delta = "+str(d))
    if len(s)==2 and isinstance(s[0],complex):
        print("Two complex solutions: \n x1 = "+str(s[0])+" \n x2 = "+str(s[1]))
    elif len(s)==2:
        print("Two real solutions: \n x1 = "+"{:.5f}".format(s[0])+" \n x2 = "+"{:.5f}".format(s[1]))
    else:
        print("One real solution: x0 = "+"{:.5f}".format(s[0]))

main()