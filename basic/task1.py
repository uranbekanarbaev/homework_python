def reverse_words(s: str) -> str:
    return " ".join(s.split()[::-1])
# Тест
s = "Hello world from Python"
print(reverse_words(s))  # "Python from world Hello"
