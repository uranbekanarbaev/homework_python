"""
Задача 3: Частота символов
Напишите функцию, которая принимает строку и возвращает словарь, где ключами являются символы, а значениями — их частота в строке.
"""


from collections import Counter
import time

def time_counter(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Total time of function execution is {end_time - start_time}')
        return result
    return wrapper

@time_counter
def char_frequency(s: str) -> dict:
    """
        Calculates the frequency of characters within a word

        Args:
            s: str. The 
        
        Returns:
            dict: the dictionary where keys are the character, and the value is the number of frequency
    """
    result = {}
    for character in s:
        result[character] = result.get(character, 0) + 1
    return result

'''@time_counter
def char_frequency_with_counter(s: str) -> dict:
    """
        Calculates the frequency of characters within a word

        Args:
            s: str. The 
        
        Returns:
            dict: the dictionary where keys are the character, and the value is the number of frequency
    """
    return Counter(s)'''



# Тест
s = "abracadabra"

if __name__ == '__main__':
    print(char_frequency(s))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
    # print(char_frequency_with_counter(s))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

'''
В 7 из 10 случаев быстрее обычный код без Counter. В случае если входные данные будут большими, Counter должен выигрывать.

Console response:
uranbekanarbaev@URAN-Laptop:~/python_tasks/homework_python$ python3 basic/task3.py
Total time of function execution is 1.6689300537109375e-06
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
Total time of function execution is 1.9311904907226562e-05
Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
uranbekanarbaev@URAN-Laptop:~/python_tasks/homework_python$ python3 basic/task3.py
Total time of function execution is 1.9073486328125e-06
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
Total time of function execution is 1.7404556274414062e-05
Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
uranbekanarbaev@URAN-Laptop:~/python_tasks/homework_python$ python3 basic/task3.py
Total time of function execution is 2.6226043701171875e-06
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
Total time of function execution is 7.534027099609375e-05
Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
'''