print("Welcome in To-Do List program...")

while True:
    user_input = input("Do you want to add a new To-Do item?\n - 'y' for yes 'n' for no 'exit' for exit -\n > ")

    if user_input.lower() == "y":
        add_new = input("Type in your new To-Do item:\n > ")

        file = open("to_do.txt", "a+", encoding = "utf-8")
        file.write(f"{add_new}\n")
        file.close()

    elif user_input.lower() == "n":
        read_list = input("Do you want list of your To-Do items?\n - 'y' for yes 'n' for no -\n > ")

        if read_list.lower() == "y":
            file = open("to_do.txt", "r", encoding = "utf-8")
            list_item = file.read()
            file.close()
            
            print(list_item)

        elif read_list.lower() == "n":
            continue
        else:
            print("Some thing wrong!! try later.")
            continue
    elif user_input.lower() == "exit":
        print("Thank you for using the To-Do List program, come back again soon.")
        break
    else:
        print("Some thing wrong!! try later.")
        continue