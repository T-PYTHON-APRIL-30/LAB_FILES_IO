'''Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
Then return again to ther first question and ask again, you coninue this untill the user types in "exit" ,
 then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
 '''

print("Welcome to 'To-Do List' program")


while True:
    
    user_ToDo_item= input('do you want to add a new To-Do item? answer by "y" for yes and "n" for no: ')
    if user_ToDo_item.lower() == "exit":
        break
    elif user_ToDo_item.lower() == "y":
        user_item= input("Type your new to-Do item: ")
        file = open("to_do.txt", "a", encoding="utf-8")
        file.writelines(user_item+"\n")
        file.close()

    elif user_ToDo_item.lower() == "n":
        list_ToDo_items= input('do you want to list your To-Do items ? answer "y" for yes and "n" for no: ')
        if list_ToDo_items.lower() == "exit":
            break
        elif list_ToDo_items.lower() =="y":
            file = open("to_do.txt", "r", encoding="utf-8")
            content = file.read()
            file.close()
            print(content)
        elif list_ToDo_items.lower() == "n":
            print("To close the program type 'exit'")

print("thank you for using the To-Do program, come back again soon ^_^")