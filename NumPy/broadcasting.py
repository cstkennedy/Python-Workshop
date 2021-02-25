import timeit
import numpy as np



def broadcast_demo():
    """
    Demonstrate the NumPy broadcast mechnic and compare it to the usual Python
    techniques.
    """

    # Plain Python
    prices = [1.00, 2.95, 8.40, 3.50, 3.30, 16.91]
    prices = [0.9 * price for price in prices]

    print(prices)

    # NumPy Broadcasting
    prices = np.array([1.00, 2.95, 8.40, 3.50, 3.30, 16.91])
    prices *= 0.9

    print(prices)

    print()
    print("*" * 80)
    print()

    # Benchmark
    def op_wrapper_py():
        prices = range(1, 1000000, 1)
        prices = [0.9 * price for price in prices]

    py_list = timeit.timeit(op_wrapper_py, number=100)

    def op_wrapper_np():
        prices = np.arange(0, 1000000, 1, dtype=np.float64)
        prices[:] *= 0.9

    np_array = timeit.timeit(op_wrapper_np, number=100)

    print(f"Python Time: {py_list:.4f}")
    print(f"NumPy Time : {np_array:.4f}")




if __name__ == "__main__":
    broadcast_demo()
