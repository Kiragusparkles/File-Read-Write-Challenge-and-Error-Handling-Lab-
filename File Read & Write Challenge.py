import os

def modify_file(input_file, output_file):
    try:
        # Step 1: Check if the input file exists
        if not os.path.exists(input_file):
            print(f"The file '{input_file}' does not exist.")
            create_file = input("Would you like to create it? (yes/no): ").strip().lower()
            if create_file == 'yes':
                with open(input_file, 'w') as infile:
                    print("Enter the text you want to add to the new file (press Enter to finish):")
                    custom_text = input()
                    infile.write(custom_text)
                    print(f"File '{input_file}' has been created with your custom content.")
            else:
                print("No file was created. Exiting program.")
                return
        
        # Step 2: Ask if the user wants to modify the file with custom text
        modify_choice = input("Would you like to modify the file with custom text? (yes/no): ").strip().lower()
        
        if modify_choice == 'yes':
            # Ask for custom text to modify
            custom_text = input("Enter the text you want to add to the file: ").strip()

            # Step 3: Open the file in append mode to add the new custom text
            with open(input_file, 'a') as infile:
                infile.write("\n" + custom_text)  # Add a new line before appending the text
                print(f"Custom text has been added to '{input_file}'.")
        else:
            print("No modification made to the file.")

        # Step 4: Read the content of the input file
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Step 5: Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()  # This is just an example; you can change it to other modifications
        
        # Step 6: Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File successfully modified and saved to '{output_file}'!")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
input_file_name = 'input.txt'  # You can replace this with any file name
output_file_name = 'output.txt'

modify_file(input_file_name, output_file_name)