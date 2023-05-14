
    
filename = "to_do.txt"

while True:
    user_input = input("Do you want to add a new To-Do item? (y/n): ")

    if user_input.lower() == "y":
        new_item = input("Enter your new To-Do item: ")
        with open(filename, "a") as file:
            file.write(new_item + "\n")

    elif user_input.lower() == "n":
        user_input = input("Do you want to list your To-Do items? (y/n): ")
        if user_input.lower() == "y":
            print("To-Do List:")
            with open(filename, "r") as file:
                todo_items = file.readlines()
                for item in todo_items:
                    print(item.strip())
                    
    elif user_input.lower() == "exit":
        print("Thank you for using the To-Do program, come back again soon.")
        break


