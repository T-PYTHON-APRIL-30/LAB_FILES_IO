
def add_item():
    while True:
        file = open("to_do.txt","r+",encoding="utf-8")
        yes="y"
        no="n" 
        answer= input("do you want to add a new To-Do item?")
        if answer == yes:
            inseritem= input("Enter your item:")
            file.write("\n"+inseritem)
            print("Item added!")
            
        elif answer == no:
            item = input("do you want to list your To-Do items?")
            if item == yes:
                print(file.read())
                break
            else :
                item == no
                Exit_cond = input("print exite to close:")
                if Exit_cond == "exite":
                    print("thank you for using the To-Do program, come back again soon")
                    break
        file.close()
add_item()
