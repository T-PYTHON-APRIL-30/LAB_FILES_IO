'''LAB_FILES_IO
Using what you learned about Python File I/O , we want to make a progeram called To-Do List , this program should do the following:
Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
If the user answers yes , then ask the user to type in his new To-Do item . Then save that To-Do item inside the a file to_do.txt on a new line.

If the user answers no, then ask the user : do you want to list your To-Do items ? answer "y" for yes and "n" for no.

If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"'''





#directory operations
import os

#get the working directory
print(os.getcwd())

#get a list of the content of a directory
print(os.listdir())
#Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
#file = open('test.txt', "w", encoding="utf-8")
file= open('lap10.txt',"a+",encoding="utf-8")
while True:
    To_Do_Items=input("do you want to add a new To-Do item? answer by y for yes and n for no.")

    if To_Do_Items=="y":
             New_To_Do_Items=input("please type in your new To-Do item ")
            file.write("\n"+New_To_Do_Items)
          
            '''file = open("fav_movies.txt", "w", encoding="utf-8")
          #2- operation on file
          file.write("1- Lord of the rings : the fellow of the ring")
          #3- close the file
          file.close()
          '''
          out=input("do you want to exit?")

    else:
        To_Do_Items=="N"
        New_To_Do_Items=input("do you want to list your To-Do items ? answer y for yes and n for no.")
        
        file.write(New_To_Do_Items)
        i=0
        for i in New_To_Do_Items:
            file.seek(i)
            content = file.read()
            print(content+"\n")
            file.close()
        out=input("do you want to exit?")
          
    if out==True:
            break
    else:
            continue
file.close()


'''If the user answers yes for reading his To-Do list , then print a list of the To-Do items one item per line.
            Then return again to ther first question and ask again, you coninue this untill the user types in "exit" , then you exit the program. and print to the user "thank you for using the To-Do program, come back again soon"'''



