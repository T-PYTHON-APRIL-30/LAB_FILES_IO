

while True:
    answer1=input('do you want to add a new To-Do item? answer by "y" for yes and "n" for no : ')
    if answer1=="y":
        answer2=input('---write your list --- \n')
        file1=open("to_do.txt",'a+',encoding="utf-8")
        file1.write(answer2+"\n")
        file1.close()
    elif answer1 == "n":
        answer3=input('do you want to list your To-Do items ? answer "y" for yes and "n" for no :  ')
        if answer3=="y":
            file2=open("to_do.txt","r")
            print(file2.read())
            file2.close()
        elif answer3=="n":
            print("ok")
    elif answer1=="exit":
        print("thank you for using the To-Do program, come back again soon")
        break
    else:
        print("invalid value try again")
        
    

