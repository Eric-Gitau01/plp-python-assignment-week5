
filename = input("Please enter the filename you want to open: ")

try:

    with open(filename, 'r') as original_file:
        content = original_file.read()
    

    modified_content = content.upper()
    

    new_filename = "modified_" + filename
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)
    
    print(f"Success! Your modified file is saved as {new_filename}")


except FileNotFoundError:
    print(f"Error: The file '{filename}' doesn't exist.")
except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")
except Exception as e:
    print(f"Something went wrong: {e}")