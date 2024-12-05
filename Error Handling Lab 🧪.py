import os

def handle_file_errors_and_add_text():
    try:
        # Step 1: Ask the user for a filename
        file_name = input("Enter the name of the file: ").strip()
        
        # Step 2: Check if the file exists
        if not os.path.exists(file_name):
            print(f"The file '{file_name}' does not exist.")
            create_file = input("Would you like to create it? (yes/no): ").strip().lower()
            if create_file == 'yes':
                with open(file_name, 'w') as file:
                    print("Enter the text you want to add to the new file (press Enter to finish):")
                    custom_text = input()
                    file.write(custom_text)
                    print(f"File '{file_name}' has been created with your custom content.")
            else:
                print("No file was created. Exiting program.")
                return
        
        # Step 3: Ask if the user wants to add custom text or just read the file
        action = input("Would you like to add custom text or just read the file? (add/read): ").strip().lower()
        if action == 'add':
            with open(file_name, 'a') as file:  # 'a' mode appends to the file
                print("Enter the text you want to add (press Enter to finish):")
                custom_text = input()
                file.write("\n" + custom_text)  # Add a new line before appending
                print(f"Your text has been added to '{file_name}'.")
        elif action == 'read':
            with open(file_name, 'r') as file:
                content = file.read()
                print("\nFile content:")
                print(content)
        else:
            print("Invalid action. Exiting program.")
    
    except PermissionError:
        print(f"Error: You do not have permission to access the file '{file_name}'.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
handle_file_errors_and_add_text()
