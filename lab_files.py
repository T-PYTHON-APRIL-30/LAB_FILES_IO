# LAB_FILES_IO

# fuction that opens a file and write in it
def add_items(user_input3: str):
    file = open("to_do_list.txt", "+a", encoding="utf-8")
    file.write("\n"+user_input3)
    file.close()


# function that open a file and read it's content
def read_items():
    file = open("to_do_list.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
    file.close


print("welcome to your To-Do List")
user_input = input("do you want to add a new To-Do item? ")

while user_input != "exit":  # while loop to keep the program running

    if user_input == "y":
        print("Please type in your new To-Do item: ")
        user_input3 = input()
        add_items(user_input3)
        user_input = input("do you want to add a new To-Do item? ")

    elif user_input == "n":
        user_input2 = input("do you want to list your To-Do items ? ")
        if user_input2 == "y":
            read_items()
            user_input = input(
                "do you want to add a new To-Do item(type exit to exit)? ")
        else:
            print("please enter 'y' to add item and 'exit' to exit")
            user_input = input("do you want to add a new To-Do item? ")
    else:
        print("please enter 'y' to add item 'n' to contenue and 'exit' to exit")
        user_input = input("do you want to add a new To-Do item? ")
else:  # Exit the while loop
    print("thank you for using the To-Do program, come back again soon")
