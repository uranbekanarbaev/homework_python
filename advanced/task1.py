
def is_symmetric(matrix: list = None) -> bool:
    """
        The function checks whether the matrix is symmetrical or not

        Args:
            list: matrix
        
        Returns:
            bool: whether matrix is symmetrical or not
    """
    n = len(matrix)
    for i in range(n):
        if len(matrix[i]) != n:
            return False
        
    for i in range(n):
        for j in range(i + 1, n):  # Сравниваем только верхнюю треугольную часть
            if matrix[i][j] != matrix[j][i]:
                return False  # Если найдена пара неравных элементов, матрица несимметрична
    return True


# Тест
matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

if __name__ == '__main__':
    print(is_symmetric(matrix))