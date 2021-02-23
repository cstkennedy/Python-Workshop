import numpy as np


def create_arrays():
    """
    Demonstrate how to create NumPy array by creating
      - an array of zeroes
      - an array of ones
      - an empty array
      - an array of integers from a Python list
      - an array of floats from a Python list
    """

    array_size = 8
    zeroes_array = np.zeros(array_size)
    print(zeroes_array)
    print()

    array_size = 12
    ones_array = np.ones(array_size)
    print(ones_array)
    print()

    # Contents are "whatever happens to be in memory"
    array_size = 16
    unitialized_array = np.empty(array_size)
    print(unitialized_array)
    print()

    # Create two NumPy arrays from Python lists
    python_list = [2, 4, 8, 16, 32, 64]
    np_array = np.array(python_list)
    print(np_array)
    print()

    python_list = [2., 4., 8., 16., 32., 64.]
    np_array = np.array(python_list)
    print(np_array)
    print()


def main():
    create_arrays()




if __name__ == "__main__":
    main()
