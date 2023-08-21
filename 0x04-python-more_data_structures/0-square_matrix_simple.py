def square_matrix_simple(matrix=[]):
    """Compute the square value of all integers of a matrix."""
    return [  # Creates a new list containing the squared rows
        [x * x for x in row]  # Squares each element in the row
        for row in matrix  # Iterates through each row in the matrix
    ]
