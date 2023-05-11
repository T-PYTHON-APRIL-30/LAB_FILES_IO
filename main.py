print("\----- Welcome to your To-Do-List -----/")

file = open("toDo_list.txt", "a+", encoding="utf-8") 
while True :   
    print("--------- This is the main page ---------")
    userInput = str(input("'s' -> show the tasks\n'a' -> add new task \n'e' -> Exit \nEnter: ")).lower()
    if not userInput.isdigit() and len(userInput) == 1 :
        if userInput == "s" :
            print("--------- Your To-Do-List is ---------")
            file.seek(0)
            content = file.read()
            print(content)
        elif userInput == "a" :
            newTask = input("Enter your new task: ")
            file.write(f"- {newTask}\n")
            print(f"--------- {newTask} is added ---------")
        elif userInput == "e" :
            print("Good bye :)")
            break
        else:
            print("Wrong entry.. Try again !")
    else:
        print("Wrong enters.. Try again !")
file.close()