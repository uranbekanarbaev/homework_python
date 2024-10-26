

def reverse_words(s: str) -> str:
    """
        This function allows to reverse words within a sentence.

        Args:
            s: str. Sentence that needs to be reversed
            
        Returns:
            str: The sentence with reversed order
    """
    return " ".join(s.split()[::-1])


# Тест
s = "Hello world from Python"

if __name__ == '__main__':
    print(reverse_words(s))  # "Python from world Hello"
