#!/usr/bin/python3
""" divide each number of a list of lists """


def matrix_divided(matrix, div):
    """matrix_divided - divide each number of a list of lists
    args:
        matrix: a list of lists
        div: divisor
    Return: A matrix of division results
    """
    # if not matrix checks if matrix has values 
    if not matrix or type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")
    lenmatrix = len(matrix)
    lenrow = len(matrix[0])
    for i in range(lenmatrix):
        for j in range(lenrow):
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not\
               float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats ")
    for k in range(lenmatrix):
        for l in range(lenrow):
            if (matrix[k][l] + 1) == matrix[k][l]:
                raise OverflowError("number is too large")
    for i in range(lenmatrix):
        if len(matrix[i]) != lenrow:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix2 = list(map(lambda i: list(map(lambda j: j / div, i)), matrix))
    for i in range(lenmatrix):
        for j in range(lenrow):
            matrix2[i][j] = round(matrix2[i][j], 2)
    return matrix2
