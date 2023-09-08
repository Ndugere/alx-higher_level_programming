#!/usr/bin/python3
"""
Defines a matrix multiplication function using NumPy.
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.

    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """
    try:
        result = np.matmul(np.array(m_a), np.array(m_b))
        return result.tolist()
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except TypeError:
        raise TypeError("invalid data type for matrix multiplication")
