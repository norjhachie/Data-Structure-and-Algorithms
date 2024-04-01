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
    return x* np.sin(x)

def f10(x):
    return x**5 + 4*x**4 + x**3 - 2*x**2 + 100

# Generate x values from 1 to 50
x_values = np.arange(1, 50)

# Plot each function individually with the provided value of x
plt.figure(figsize=(10, 6))

# plot f1(x)
plt.plot(x_values, f1(x_values), label= (f'x^2 + 7x + 2'))
# plot f2(x)
plt.plot(x_values, f2(x_values), label= (f'3x + 2'))
# plot f3(x)
plt.plot(x_values, f3(x_values), label= (f'x^2'))
# plot f4(x)
plt.plot(x_values, f4(x_values), label= (f'x^3'))
# plot f5(x)
plt.plot(x_values, f5(x_values), label= (f'x^5'))
# plot f6(x)
plt.plot(x_values, f6(x_values), label= (f'x^3 + 2x^2 + x + 10'))
# plot f7(x)
plt.plot(x_values, f7(x_values), label= (f'x^4 - 3x^3 + 2x^2 - x + 11'))
# plot f8(x)
plt.plot(x_values, f8(x_values), label= (f'sin(x)'))
# plot f9(x)
plt.plot(x_values, f9(x_values), label= (f'cos(x)'))
# plot f10(x)
plt.plot(x_values, f10(x_values), label= (f'x^5 + 4x^4 + x^3 - 2x^2 + 100'))

# Display graphs
plt.title(f'ALL GRAPHS')
plt.xlabel('x')
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()