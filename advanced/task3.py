"""
Задача 3: Работа с файлами
Напишите программу, которая читает текстовый файл, удаляет из него все пустые строки и строки, состоящие только из пробелов, а затем записывает результат в новый файл.
"""

def clean_file(input_file: str = None, output_file: str = None) -> None:
    """
        The function cleans file from empty lines and not useful spaces

        Args:
            input_file (str): The file path for the document that needs to be cleaned
            output_file (str): The name of file path that the resulted file must be saved in 
        
        Returns:
            None: The result must be just written in a new file
    """
    with open(input_file, 'r') as file:
        lines = file.readlines()

    cleaned_file = [line for line in lines if line.strip()]
    
    with open(output_file, 'w') as file:
        file.writelines(cleaned_file)
        


input_file = "input.txt"
output_file = "output.txt"

if __name__ == '__main__':
    clean_file(input_file, output_file)