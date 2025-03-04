import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def main():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    
    sum_arrays = a + b
    dot_product = np.dot(a, b)
    matrix = np.array([[1, 2], [3, 4]])
    determinant = np.linalg.det(matrix)
    
    integral_result, integral_error = quad(lambda x: np.sin(x), 0, np.pi)
    
    print("Let's do some simple math with NumPy and SciPy...")
    print("Array a:", a)
    print("Array b:", b)
    print("Sum of a and b:", sum_arrays)
    print("Dot product of a and b:", dot_product)
    print("Determinant of matrix [[1,2],[3,4]]:", determinant)
    print("Integral of sin(x) from 0 to pi:", integral_result, "with error estimate:", integral_error)
    print("If you made it this far, seems like numpy and scipy are working fine.")
    
    # Generate a sine wave series and display it with a graph
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
    plt.xlabel("x (radians)")
    plt.ylabel("sin(x)")
    plt.title("Sine Wave")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    input("Press Enter to exit...")
if __name__ == "__main__":
    main()