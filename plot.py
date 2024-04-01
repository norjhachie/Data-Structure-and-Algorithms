import matplotlib.pyplot as plt
import numpy as np

# Define the mathematical functions 
def f1(x):
    return x**2 + 7*x + 2

def f2(x):
    return 3*x + 2

def f3(x):
    return x**2

def f4(x):
    return x**3

def f5(x):
    return x**5

def f6(x):
    return x**3 + 2*x**2 + x + 10

def f7(x):
    return x**4 - 3*x**3 + 2*x**2 - x + 11

def f8(x):
    return np.sin(x)

def f9(x):
    return np.cos(x)

def f10(x):
    return x**5 + 4*x**4 + x**3 - 2*x**2 + 100

while True:
    # Load the input values from a file
    with open('math.txt') as f:
        x = [int(line.strip()) for line in f]

    # List of the problems to be plotted
    print()
    print("List of the Functions")
    print("1. x^2 + 7x + 2")
    print("2. 3x + 2")
    print("3. x^2")
    print("4. x^3")
    print("5. x^5")
    print("6. x^3 + 2x^2 + x + 10")
    print("7. x^4 - 3x^3 + 2x^2 - x + 11")
    print("8. sin(x)")
    print("9. cos(x)")
    print("10. x^5 + 4x^4 + x^3 - 2x^2 + 100")
    print("0 =  QUIT")
    print()
    math_func = int(input("Enter the number (1-10) of the function to plot or press 0 to QUIT: "))

    if math_func == 0:
        break
    if 1 <= math_func <= 10:
        # Plot the chosen function
        if math_func == 1:
            title = "x^2 + 7x + 2"
            y = [f1(i) for i in x]
        elif math_func == 2:
            title = "3x + 2"
            y = [f2(i) for i in x]
        elif math_func == 3:
            title = "x^2"
            y = [f3(i) for i in x]
        elif math_func == 4:
            title = "x^3"
            y = [f4(i) for i in x]
        elif math_func == 5:
            title = "x^5"
            y = [f5(i) for i in x]
        elif math_func == 6:
            title = "x^3 + 2x^2 + x + 10"
            y = [f6(i) for i in x]
        elif math_func == 7:
            title = "x^4 - 3x^3 + 2x^2 - x + 11"
            y = [f7(i) for i in x]
        elif math_func == 8:
            title = "sin(x)"
            y = [f8(i) for i in x]
        elif math_func == 9:
            title = "cos(x)"
            y = [f9(i) for i in x]
        elif math_func == 10:
            title = "x^5 + 4x^4 + x^3 - 2x^2 + 100"
            y = [f10(i) for i in x]

        # Plot the function
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Problem {math_func} = {title}')
        plt.grid()
        plt.show()
