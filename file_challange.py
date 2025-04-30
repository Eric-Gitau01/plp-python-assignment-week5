def file_operations():

    filename = input("Enter filename to read (e.g., story.txt): ")
    
    try:

        with open(filename, 'r') as f:
            content = f.read()
        
        modified = content.upper()
    
        new_filename = f"modified_{filename}"

        with open(new_filename, 'w') as f:
            f.write(modified)
        
        print(f"Success! Created {new_filename}")
    
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
    except PermissionError:
        print("Error: No permission to read/write files!")
    except Exception as e:
        print(f"Unexpected error: {e}")


file_operations()