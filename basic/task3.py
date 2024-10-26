

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


# Тест
s = "abracadabra"

if __name__ == '__main__':
    print(char_frequency(s))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
