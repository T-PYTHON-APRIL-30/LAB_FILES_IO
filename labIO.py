
flag = True
while flag:
    user_input = input("Welcome to to-do-list, please answer with (y/n or exit to leave the program) on wether you want to add somethings to your to-do-list:")

    if user_input.lower() == "y":
        flag1 = True
        lines = []
        while flag1:
            user_to_do_input = input(("enter whatever you want to your to-do-list (type end for stopping): ") + '\n')
            if user_to_do_input.lower() == "end":
                flag1 = False
            else:
                lines.append(user_to_do_input + "\n")
                print(lines)

        file = open("to_do.txt", "a+", encoding="UTF-8")
        file.writelines(lines)
        file.close()

    if user_input.lower() == "n":
        n_user_input = input("would you like to see your to-do-list? please answer with (y/n):")
        if n_user_input.lower() == "y":
            file = open("to_do.txt", "r", encoding="UTF-8")
            file.seek(0)
            print(file.read())
            file.close()
        elif n_user_input.lower() == "n":
            print("thank you for using the program, have a good day")
            flag = False
    if user_input.lower() == "exit":
        print("thank you for using the program, have a good day")
        flag =False


