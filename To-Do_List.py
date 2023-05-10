print("Wellcome to To-do_List program :) ")

file = open("To-Do_List.txt","a+",encoding="utf-8")
check = ""

def to_do_list():
  answer_user = input("do you want to add new to-do item? y(Yes) or n(NO)")

  if answer_user == "y":
        new_to_do_item = input("Enter a type to-do you want... ")
        file.write(new_to_do_item+"\n")

  elif answer_user == "n":
        answer_user = input("Do you want to list your to-do item? y(Yes) or n(NO)")

        if answer_user == "y":
             file.seek(0)
             content = file.readlines()

             for a in content:
                  print(a)
  return answer_user         

while check != "exit":
     check = to_do_list()
else:
     print("thank you for using to-do_list program, wish you happy to use it :)")
     file.close()