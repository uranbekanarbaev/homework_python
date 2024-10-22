
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Произошла ошибка: {exc_value}")
            return True  # Подавить исключение

# Пример использования
with FileManager("example.txt", "w") as file:
    file.write("Hello, world!")