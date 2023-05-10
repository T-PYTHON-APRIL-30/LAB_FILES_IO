exit = 0
while exit <1 :
    user_inp = input("do you want to add a new To-Do item? answer by 'y' for yes and 'n' for no, 'e' to exit: ")
    if  user_inp == 'y':
        file = open("to_do.txt","a",encoding="utf-8")
        file.write("\n"+input("what do you want to add? "))
        file.close()
    elif  user_inp == "n":
        user_inp2 = input('do you want to list your To-Do items ? answer "y" for yes and "n" for no "e" to exit: ')
        if  user_inp2 == 'y':
            file = open("to_do.txt","r",encoding="utf-8")
            cont = file.read()
            print(cont)
            file.close()
        elif user_inp2=="n":
            continue
        elif user_inp2=="e" :
            exit+=1
    elif user_inp == "e":
        exit+=1