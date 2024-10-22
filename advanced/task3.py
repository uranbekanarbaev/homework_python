def clean_file(input_file: str, output_file: str) -> None:
    with open(input_file, 'r') as file:
        lines = file.readlines()

    cleaned_file = [line for line in lines if line.strip()]
    
    print(cleaned_file)

    with open(output_file, 'w') as file:
        file.writelines(cleaned_file)


input_file = "input.txt"
output_file = "output.txt"
clean_file(input_file, output_file)