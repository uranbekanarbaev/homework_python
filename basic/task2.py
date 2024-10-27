"""
Задача 2: Максимальная сумма подмассива
Напишите функцию, которая принимает список чисел и возвращает максимальную сумму подмассива.
"""


def max_subarray_sum(nums: list = None) -> int:
    """
        Calculates the subarray within an array that gives max sum

        Args:
            nums: list. The array of numbers
        
        Returns:
            int: The subarray with maximum sum
    """
    max_sum = current_sum = nums[0]
    if not nums:
        return []
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum


# Тест
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

if __name__ == '__main__':
    print(max_subarray_sum(nums))