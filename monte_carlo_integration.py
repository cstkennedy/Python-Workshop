#! /usr/bin/env python3

import random
import sys

from typing import (Callable, Tuple)

Point = Tuple[float, float]


def generate_random_points(f: Callable,
                           lower_limit: float,
                           upper_limit: float,
                           n: int) -> Point:
    """
    Generate a sequence of random x values and plug them into f(x).

    Args:
        f: mathematical function
        lower_limit: 'a' the lower bound
        upper_bound: 'b' the upper bound
        n: number of points to generate

    Yields:
        A sequence of points in the form (x, f(x))
    """

    for _ in range(0, n):
        x = random.uniform(lower_limit, upper_limit)
        y = f(x)

        yield (x, y)


def naive_main():
    """
    This is a "naive" main function used to demonstrate the basic premise
    behind Monte Carlo integration.
    """

    num_points = int(sys.argv[1])
    limit_a = float(sys.argv[2])
    limit_b = float(sys.argv[3])

    math_f = lambda x: x**2
    #  math_f = lambda x: cos(x)

    print("{:-^80}".format("Points"), file=sys.stderr)

    temp_sum = 0
    for i, point in enumerate(generate_random_points(math_f, limit_a, limit_b, num_points)):
        print(f"{i:5d} - ({point[0]:>12.8f}, {point[1]:>12.8f})", file=sys.stderr)

        temp_sum += point[1]

    integral_result = (limit_b - limit_a) / float(num_points) * temp_sum

    print(f"{integral_result:16.8f}")


def not_so_naive_main():
    """
    This main function demonstrates the more "Pythonic" approach
    """

    num_points = int(sys.argv[1])
    limit_a = float(sys.argv[2])
    limit_b = float(sys.argv[3])

    math_f = lambda x: x**2
    #  math_f = lambda x: cos(x)

    point_sequence = generate_random_points(math_f, limit_a, limit_b, num_points)
    f_of_x_values = (y for x, y in point_sequence)

    integral_result = ((limit_b - limit_a) /
                       float(num_points) *
                       sum(f_of_x_values))

    print(f"{integral_result:16.8f}")


def main_without_a_table_flip():
    """
    This main demonstrates the impact of the number of points on Monte Carlo
    integration
    """

    num_points = int(sys.argv[1])  # Unused in this version of main
    limit_a = float(sys.argv[2])
    limit_b = float(sys.argv[3])
    max_magnitude = int(sys.argv[4])

    math_f = lambda x: x**2

    print("| {:^16} | {:^20} |".format("# Points", "Est. f(x)"))

    max_num_points = 2 ** max_magnitude
    point_sequence = list(generate_random_points(math_f, limit_a, limit_b, max_num_points))

    for magnitude in range(0, max_magnitude + 1):
        num_points = 2 ** magnitude

        f_of_x_values = (y for x, y in point_sequence[:num_points])

        integral_result = ((limit_b - limit_a) /
                           float(num_points) *
                           sum(f_of_x_values))

        print(f"| {num_points:>16} | {integral_result:^20.8f} |")


if __name__ == "__main__":
    #  naive_main()
    #  not_so_naive_main()
    main_without_a_table_flip()
