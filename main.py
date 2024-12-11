toDoList=[]


def add_item():
    item=input("Enter a task: ")
    toDoList.append(item)
    for i in range(0, len(toDoList)):
        print(str(i + 1) + ". " + toDoList[i])

def remove_item():
    for i in range(0, len(toDoList)):
        print(str(i+1)+". " + toDoList[i])
    remove=int(input("Enter a the # to remove: "))
    remove=remove-1
    toDoList.pop(remove)
    for i in range(0, len(toDoList)):
        print(str(i + 1) + ". " + toDoList[i])

def print_list():
    for i in range(0, len(toDoList)):
        print(str(i + 1) + ". " + toDoList[i])

def reset_list():
    toDoList.clear()
    for i in range(0, len(toDoList)):
        print(str(i + 1) + ". " + toDoList[i])
def show_menu():
    print( "Press 1 to, Add a task.")
    print( "Press 2 to, Remove a task.")
    print( "Press 3 to, Show list.")
    print( "Press 4 to, Reset list.")
    choice=input("Enter Choice: ")
    if choice == "1":
            add_item()
    elif choice == "2":
            remove_item()
    elif choice == "3":
            print_list()
    elif choice == "4":
            reset_list()
    else:
        print("Invalid input")
        show_menu()




#for testing (remove when finished)
while True:
    show_menu()