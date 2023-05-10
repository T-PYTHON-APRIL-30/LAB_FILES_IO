'''

Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"


'''


def add_todo_item(item):
    with open("to_do.txt", "a") as file:
        file.write(f"{item}\n")

def read_todo_items():
    with open("to_do.txt", "r") as file:
        items = file.readlines()
        return [item.strip() for item in items]

def main():

    print('-----'*5)
    print("|                       |\n"*3)
    print("Welcome to Do a new List..")
    print('-----' * 5)
    while True:
        add_item = input("Do you want to add a new To-Do item? (y/n) or exit: ")

        if add_item.lower() == "y":
            new_item = input("Enter your new To-Do item: ")
            add_todo_item(new_item)
        elif add_item.lower() == "n":
            list_items = input("Do you want to list your To-Do items? (y/n): ")

            if list_items.lower() == "y":
                items = read_todo_items()
                print("\nYour To-Do List:")
                for index, item in enumerate(items, start=1):
                    print(f"{index}. {item}")

        elif add_item.lower() == "exit":
            break
        else:
            print("Invalid input. Please try again.")

    print("Thank you for using the To-Do program, come back again soon!")

if __name__ == "__main__":
    main()
