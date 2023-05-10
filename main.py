'''Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.
If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.
If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"'''

while True:
    user_input = input("\nDo you want to add a new To-Do item? \n")
    if user_input == "y":
        new_item = input("\nType To-Do item:\n")
        to_do_file = open("To-Do list.txt","a+",encoding="utf-8")
        to_do_file.write("\n"+new_item)
        

    elif user_input == "exit":
        break

    elif user_input == "n":
        user_input2 = input("\nDo you want to list your To-Do items? \n")
        if user_input2 == "y":
            to_do_file.seek(0)
            print(to_do_file.read())
            to_do_file.close()
        
        elif user_input2 == "n":
            print("\nif you want to exit the program type exit.\n")
print("Thank you for using the To-Do program, come back again soon\n")