# LAB_FILES_IO


# Using what you learned about Python File I/O ,
# we want to make a progeram called To-Do List , this program should do the following:
'''
- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
- If the user answers yes , then ask the user to type in his new To-Do item .
 Then save that To-Do item inside the a file to_do.txt on a new line.
- If the user answers no, then ask the user : 
do you want to list your To-Do items ? answer "y" for yes and "n" for no. 
- If the user answers yes for reading his To-Do list ,
 then print a list of the To-Do items one item per line.
- Then return again to ther first question and ask again,
 you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"
'''
print("welcome to your To-Do List")

user_input = input("do you want to add a new To-Do item? ")
while user_input != "exit":
    if user_input == "y":
        file = open("to_do_list.txt", "+a", encoding="utf-8")
        print("Please type in your new To-Do item: ")
        user_input3 = input()
        file.write("\n"+user_input3)
        file.close()
        user_input = input("do you want to add a new To-Do item? ")

    elif user_input == "n":
        user_input2 = input("do you want to list your To-Do items ? ")
        if user_input2 == "y":
            file = open("to_do_list.txt", "r", encoding="utf-8")
            content = file.read()
            print(content)
            file.close
            user_input = input("do you want to add a new To-Do item(type exit to exit)? ")
        else:
                print("please enter 'y' to add item and 'exit' to exit")
                user_input = input("do you want to add a new To-Do item? ")
    else:
                print("please enter 'y' to add item 'n' to contenue and 'exit' to exit")
                user_input = input("do you want to add a new To-Do item? ")
else:
    print("thank you for using the To-Do program, come back again soon")
