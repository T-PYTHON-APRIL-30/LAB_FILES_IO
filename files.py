file = open('to_do.txt ', "a+", encoding="utf-8")
while True:
    answer_user = input(f"Do You want to add a new To-Do item? answer by 'y' for yes 'n' for no 'exit' for exit ")
    if answer_user.lower() == "y":
        todolist = input("write your note")
        file.write(todolist+"\n")
    elif answer_user.lower() == "n":
     viewlist = input("do you want to list your To-Do items ? ")
     if viewlist =="y":
      file.seek(0)
      content = file.readlines()
      for line in content:
         print(f"- {line}")
    elif viewlist.lower() == "exit":
        file.close
        break
print("thank you for using the To-Do program, come back again soon")
