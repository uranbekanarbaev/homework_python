"""
Задача 4: Разработка контекстного менеджера для работы с файлами
Создайте контекстный менеджер для работы с файлами, который будет автоматически открывать и закрывать файл, а также обрабатывать возможные исключения. Используйте магические методы __enter__ и __exit__.
"""

import logging

class FileManager:
    """
    A context manager class for handling file operations.

    This class simplifies the process of opening and closing files 
    using the `with` statement, ensuring that files are properly 
    closed after their use, even in the event of an error.

    Attributes:
        filename (str): The name of the file to be managed.
        mode (str): The mode in which to open the file (e.g., 'r', 'w', 'a').

    Methods:
        __enter__(): Opens the file and returns the file object.
        __exit__(exc_type, exc_value, traceback): Closes the file and handles exceptions.
    """

    def __init__(self, filename: str, mode: str):
        """
        Initializes a new FileManager instance.

        Args:
            filename (str): The name of the file to be managed.
            mode (str): The mode in which to open the file (e.g., 'r', 'w', 'a').
        """
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        """
        Opens the file and returns the file object.

        Returns:
            file object: The opened file object, allowing for file operations.
        """
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Closes the file and handles exceptions if they occur.

        Args:
            exc_type (type): The type of exception raised, if any.
            exc_value (Exception): The exception instance raised, if any.
            traceback (Traceback): The traceback object, if any.

        Returns:
            bool: True to suppress the exception, False to propagate it.
        """
        if self.file:
            self.file.close()
        if exc_type:
            logging.error(f"Error being faced: {exc_value}")
            return True 

# Пример использования
if __name__ == '__main__':
    with FileManager("example.txt", "w") as file:
        file.write("Hello, world!")
