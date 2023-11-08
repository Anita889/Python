while True:
    try:
        file_name = input("Enter the name of the text file: ")

        with open(file_name, 'r') as file:
            content = file.read()
            print("File content:\n", content)

        write_option = input("Do you want to write to the same file? (yes/no): ").lower()

        if write_option == 'yes':
            with open(file_name, 'a') as file:
                new_content = input("Enter the new content you want to append: ")
                file.write(new_content)
                print("Content appended successfully.")

        elif write_option == 'no':
            new_file_name = input("Enter the name of the new text file: ")

            with open(new_file_name, 'w') as new_file:
                new_content = input("Enter the content you want to write: ")
                new_file.write(new_content)
                print("Content written to the new file successfully.")

        else:
            print("Invalid option. Please enter 'yes' or 'no'.")

        break

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist. Please enter a valid file name.")

    except ValueError as ve:
        print(f"Error: {ve}. Please enter a valid file name.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please enter a valid file name.")

    finally:
        print("Execution completed.")
