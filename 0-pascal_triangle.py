#!/usr/bin/python3
"""Create pascal_triangle function """


def pascal_triangle(n):
    """print pascal triangle"""
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Initialize the row with 1s
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
