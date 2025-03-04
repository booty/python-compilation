import numpy as np
from scipy.integrate import quad

def main():
    # Create two NumPy arrays
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    
    # Basic array operations
    sum_arrays = a + b
    dot_product = np.dot(a, b)
    
    # Compute the determinant of a 2x2 matrix
    matrix = np.array([[1, 2], [3, 4]])
    determinant = np.linalg.det(matrix)
    
    # Use SciPy to integrate sin(x) from 0 to pi
    integral_result, integral_error = quad(lambda x: np.sin(x), 0, np.pi)
    
    # Print the results
    print("Let's do some simple math with NumPy and SciPy...")
    print("Array a:", a)
    print("Array b:", b)
    print("Sum of a and b:", sum_arrays)
    print("Dot product of a and b:", dot_product)
    print("Determinant of matrix [[1,2],[3,4]]:", determinant)
    print("Integral of sin(x) from 0 to pi:", integral_result, "with error estimate:", integral_error)
    print("If you made it this far, seems like numpy and scipy are working fine.")
if __name__ == "__main__":
    main()