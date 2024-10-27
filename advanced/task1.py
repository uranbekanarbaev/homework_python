"""
Задача 1: Проверка матрицы на симметричность
Напишите функцию, которая принимает на вход квадратную матрицу и проверяет, является ли она симметричной относительно главной диагонали.
"""


def is_symmetric(matrix: list = None) -> bool:
    """
        The function checks whether the matrix is symmetrical or not

        Args:
            list: matrix
        
        Returns:
            bool: whether matrix is symmetrical or not
    """

    if not matrix or not matrix[0]:
        return False

    n = len(matrix)
    
    for row in matrix:
        if len(row) != n:
            return False
        
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


# Тест
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if __name__ == '__main__':
    print(is_symmetric(matrix))