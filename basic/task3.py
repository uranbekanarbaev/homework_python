
def char_frequency(s: str) -> dict:
    result = {}
    for character in s:
        if character not in result:
            result[character] = 1
        else:
            result[character] += 1
    return result

# Тест
s = "abracadabra"
print(char_frequency(s))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
