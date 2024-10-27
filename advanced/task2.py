"""
Задача 2: Словари и множества
Напишите функцию, которая принимает список строк и возвращает словарь, где ключами являются уникальные слова, а значениями — множества индексов строк, в которых эти слова встречаются.
"""


def words_index_map(strings: list = None) -> dict:
    """
        The function calculates the words index map and gives the dictionary of words

        Args:
            list: an array with words
        
        Returns:
            dict: the number of words frequency
    """
    result = {}
    for i, sentence in enumerate(strings):
        for word in sentence.split():
            if word not in result:
                result[word] = {i}
            else:
                result[word].add(i) 

    return result


# Тест
strings = [
    "hello world",
    "world of python",
    "hello again"
]

if __name__ == '__main__':
    print(words_index_map(strings))