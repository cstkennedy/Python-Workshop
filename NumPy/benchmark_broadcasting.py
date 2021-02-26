import timeit
import numpy as np


def broadcast_demo():
    """
    Demonstrate the NumPy broadcast mechanic and compare it to the usual Python
    techniques (benchmark).
    """

    num_values = 1000000
    num_runs = 100

    def op_wrapper_py():
        prices = range(1, num_values, 1)
        prices = [0.9 * price for price in prices]

    py_list = timeit.timeit(op_wrapper_py, number=num_runs)

    def op_wrapper_np():
        prices = np.arange(0, num_values, 1, dtype=np.float64)
        prices[:] *= 0.9

    np_array = timeit.timeit(op_wrapper_np, number=num_runs)

    print(f"Python Time: {py_list:.4f}")
    print(f"NumPy Time : {np_array:.4f}")


if __name__ == "__main__":
    broadcast_demo()
