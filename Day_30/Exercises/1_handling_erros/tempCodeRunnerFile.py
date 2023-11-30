
    # Handle the FileNotFoundError here.
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_name = "a_file.txt"
    file_path = os.path.join(current_directory, file_name)
    with open(file_path, 'w') as new_file:
        new_file.write("Hi, I'm there")