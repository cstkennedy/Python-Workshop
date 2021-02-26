import numpy as np


def broadcast_demo():
    """
    Demonstrate the NumPy broadcast mechanic and compare it to the usual Python
    techniques (e.g., a list comprehension).
    """

    # Plain Python
    prices = [1.00, 2.95, 8.40, 3.50, 3.30, 16.91]
    prices = [0.9 * price for price in prices]

    print(prices)

    # NumPy Broadcasting
    prices = np.array([1.00, 2.95, 8.40, 3.50, 3.30, 16.91])
    prices *= 0.9

    print(prices)


if __name__ == "__main__":
    broadcast_demo()
