from multiplicationOfMatrix import inputMatrix
from copy import deepcopy


def minorMatrix(matrix: list, row: int, col: int):
    # Make deepcopy of matrix to prevent it from changing
    matrixCopy = deepcopy(matrix)

    # Remove given row from matrix
    matrixCopy.remove(matrix[row])

    # Remove column from matrix
    for i in range(len(matrixCopy)):
        matrixCopy[i].remove(matrixCopy[i][col])
    return matrixCopy


def matrixDeterminant(matInp: dict):
    # Parse matrix from dict
    matrix = matInp["matrix"]
    rowlen = len(matrix)  # Get row length

    # Check if every row == col
    for row in matrix:
        if len(row) != rowlen:
            print("Not a square matrix")
            return None
        else:
            collen = len(matrix[0])

    if rowlen == collen:
        # check if it is a matrix of order 1
        if len(matrix[0]) == 1:
            return {"determinant": matrix[0][0]}

        # return simple determinant for matrix of order 2
        elif len(matrix[0]) == 2:
            determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return {"determinant": determinant}

        # if not of order 1 and also square matrix
        else:
            det = 0
            for col in range(collen):
                # Get minor matrix from declared function
                minor_Matrix = minorMatrix(matrix, 0, col)
                minorDet = matrixDeterminant(
                    {"matrix": minor_Matrix}
                )  # Get determinant of minor matrix

                # Do cofactor expansion and add it to det
                det += ((-1) ** col) * matrix[0][col] * minorDet["determinant"]
            return {"determinant": det}

    else:
        print(f"\nError: Matrix must be a square matrix")


if __name__ == "__main__":
    A = inputMatrix("A")
    print(A)
    # A = {"order": "4x4", "matrix": [
    #         [4,3,2,2],
    #         [0,1,-3,3],
    #         [0,-1,3,3],
    #         [0,3,1,1]
    #     ]}
    determinant = matrixDeterminant(A)
    print(determinant)
