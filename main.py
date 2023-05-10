print("\----- Welcome to your To-Do-List -----/")

while True :
    file_read = open("toDo_list.txt", "r", encoding="utf-8")
    file_write = open("toDo_list.txt", "a+", encoding="utf-8")
    print("--------- This is the main page ---------")
    userInput = str(input("'s' -> show the tasks\n'a' -> add new task \n'e' -> Exit \nEnter: ")).lower()
    if not userInput.isdigit() and len(userInput) == 1 :
        if userInput == "p" :
            print("--------- Your To-Do-List is ---------")
            content = file_read.read()
            print("-",content)
        elif userInput == "a" :
            newTask = input("Enter your new task: ")
            file_write.write(newTask+"\n")
            print(f"--------- {newTask} is added ---------")
        elif userInput == "e" :
            print("Good bye :)")
            file_read.close()
            file_write.close()
            break
        else:
            print("Wrong entry.. Try again !")
    else:
        print("Wrong enters.. Try again !")