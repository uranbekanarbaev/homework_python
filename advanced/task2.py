
def words_index_map(strings: list) -> dict:
    result = {}
    for i, sentences in enumerate(strings):
        for word in sentences.split():
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
print(words_index_map(strings))