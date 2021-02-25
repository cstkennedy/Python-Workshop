import numpy as np

def print_matrices(matrix_XTX, matrix_XTY):
    """
    Print the XTX and XTY matrices
    """

    print("{:*^40}".format("XTX"))
    print(matrix_XTX)

    print()
    print("{:*^40}".format("XTY"))
    print(matrix_XTY)


def _backsolve(matrix_XTX, matrix_XTY):

    num_rows, _ = matrix_XTX.shape

    for i in reversed(range(1, num_rows)):
        for j in reversed(range(0, i)):
            s = matrix_XTX[j, i]

            matrix_XTX[j, i] -= (s * matrix_XTX[i, i])
            matrix_XTY[j] -= (s * matrix_XTY[i])


def solve_matrix(matrix_XTX, matrix_XTY):
    """
    Solve a matrix and return the resulting solution vector
    """

    # Get the dimensions (shape) of the XTX matrix
    num_rows, num_columns = matrix_XTX.shape

    for i in range(0, num_rows):
        # Find column with largest entry
        largest_idx = i
        current_col = i
        for j in range(i + 1, num_rows):

            if matrix_XTX[largest_idx, i] < matrix_XTX[j, current_col]:
                largest_idx = j

        # Swap
        if largest_idx != current_col:
            matrix_XTX[[i, largest_idx], :] = matrix_XTX[[largest_idx, i], :]
            matrix_XTY[[i, largest_idx]] = matrix_XTY[[largest_idx, i]]

        # Scale
        scaling_factor = matrix_XTX[i, i]
        matrix_XTX[i, :] /= scaling_factor
        matrix_XTY[i] /= scaling_factor

        # Eliminate
        for row_i in range(i + 1, num_rows):
            s = matrix_XTX[row_i][i]

            matrix_XTX[row_i] = matrix_XTX[row_i] - s * matrix_XTX[i]
            matrix_XTY[row_i] = matrix_XTY[row_i] - s * matrix_XTY[i]

        #  print("{:-^80}".format(f"Iteration #{i:}"))
        #  print_matrices(matrix_XTX, matrix_XTY)

    _backsolve(matrix_XTX, matrix_XTY)

    return matrix_XTY


def main():

    # Set up input data points, X, Y, and XT
    points = [(0., 0.), (1., 1.), (2., 4.)]

    matrix_X = np.array([[1., 0., 0.],
                         [1., 1., 1.],
                         [1., 2., 4.]])

    matrix_Y = np.array([0,
                         1,
                         4])

    matrix_XT = matrix_X.transpose()

    # Compute XTX and XTY
    matrix_XTX = np.matmul(matrix_XT, matrix_X)
    matrix_XTY = np.matmul(matrix_XT, matrix_Y)

    print_matrices(matrix_XTX, matrix_XTY)

    print()
    print("{:-^40}".format("Solution"))
    solution = solve_matrix(matrix_XTX, matrix_XTY)
    print(solution)


if __name__ == "__main__":
    main()
