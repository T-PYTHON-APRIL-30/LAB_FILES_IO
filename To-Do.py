'''# LAB_FILES_IO

## Using what you learned about Python File I/O , we want to make a progeram called To-Do List ,
 this program should do the following:
*- Ask the user do you want to add a new To-Do item? answer by "y" for yes and "n" for no.
*- If the user answers yes , then ask the user to type in his new To-Do item .
 Then save that To-Do item inside the a file to_do.txt on a new line.
- If the user answers no, then ask the user : do you want to list your To-Do items ?
 answer "y" for yes and "n" for no. 
- If the user answers yes for reading his To-Do list ,
 then print a list of the To-Do items one item per line.
- Then return again to ther first question and ask again,
 you coninue this untill the user types in "exit" , then you exit the program. and print to the user
 "thank you for using the To-Do program, come back again soon"'''


print('Welcome to our To-Do list...')
file = open("ToDo.txt","a+", encoding="utf-8")

while True:

    choise = input('do you want to add a new To-Do item?\n(answer by "y" for yes, "n" for no and "e" for exit):')
    print()
    if choise.lower() == 'y':
        file = open("ToDo.txt", "a")
        item = input('Type in your new To-Do item: ')
        file.write('* ' + item + '\n' )
        print()
        

    elif choise.lower() == 'n':
        choise2 = input('do you want to list your To-Do items?\n (answer by "y" for yes, "n" for no): ')
        print()
        if choise2.lower() == 'y':
            file.seek(0)
            content = file.readlines()
            for line in content:
                print(line)
                
            print()

        elif choise2.lower() == 'n':
            pass

    elif choise.lower() == 'e':
        print("Thank you for using the To-Do program, come back again soon")
        file.close()
        break

    else:
        print('Wrong entry please re-enter a correct choise..')
        print()


