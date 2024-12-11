
"""
BLANK LISTS
"""
toDoList=[]
toDoList2=[]
todolist3=[]



"""
LIST 3 FUNCTIONS
"""


def add_item3():
    item = input("Enter a task: ")
    todolist3.append(item)
    for i in range(0, len(todolist3)):
        print(str(i + 1) + ". " + todolist3[i])
def remove_item3():
    for i in range(0, len(todolist3)):
        print(str(i + 1) + ". " + todolist3[i])
    remove3 = int(input("Enter a the # to remove: "))
    remove3 = remove3 - 1
    todolist3.pop(remove3)
    for i in range(0, len(todolist3)):
        print(str(i + 1) + ". " + todolist3[i])
def print_list3():
    for i in range(0, len(todolist3)):
        print(str(i + 1) + ". " + todolist3[i])
def reset_list3():
    todolist3.clear()
    for i in range(0, len(todolist3)):
        print(str(i + 1) + ". " + todolist3[i])
def show_menu3():
    print("Press 1 to, Add a task.")
    print("Press 2 to, Remove a task.")
    print("Press 3 to, Show list.")
    print("Press 4 to, Reset list.")
    print("Press 5 to, Change list.")
    choice = input("Enter Choice: ")
    if choice == "1":
        add_item3()
    elif choice == "2":
        remove_item3()
    elif choice == "3":
        print_list3()
    elif choice == "4":
        reset_list3()
    elif choice == "5":
        listchoice()
    else:
        print("Invalid input")
        show_menu3()


"LIST 2 FUNCTIONS"

def add_item2():
    item = input("Enter a task: ")
    toDoList2.append(item)
    for i in range(0, len(toDoList2)):
        print(str(i + 1) + ". " + toDoList2[i])
def remove_item2():
    for i in range(0, len(toDoList2)):
        print(str(i + 1) + ". " + toDoList2[i])
    remove2 = int(input("Enter a the # to remove: "))
    remove2 = remove2 - 1
    toDoList2.pop(remove2)
    for i in range(0, len(toDoList2)):
        print(str(i + 1) + ". " + toDoList2[i])
def print_list2():
    for i in range(0, len(toDoList2)):
        print(str(i + 1) + ". " + toDoList2[i])
def reset_list2():
    toDoList2.clear()
    for i in range(0, len(toDoList2)):
        print(str(i + 1) + ". " + toDoList2[i])
def show_menu2():
    print("Press 1 to, Add a task.")
    print("Press 2 to, Remove a task.")
    print("Press 3 to, Show list.")
    print("Press 4 to, Reset list.")
    print("Press 5 to, Change list.")
    choice = input("Enter Choice: ")
    if choice == "1":
        add_item2()
    elif choice == "2":
        remove_item2()
    elif choice == "3":
        print_list2()
    elif choice == "4":
        reset_list2()
    elif choice == "5":
        listchoice()
    else:
        print("Invalid input")
        show_menu2()



"LIST ONE FUNCTIONS"

def add_item():
    item = input("Enter a task: ")
    toDoList.append(item)
    for i in range(0, len(toDoList)):
        print(str(i + 1) + ". " + toDoList[i])
def remove_item():
    for i in range(0, len(toDoList)):
        print(str(i + 1) + ". " + toDoList[i])
    remove = int(input("Enter a the # to remove: "))
    remove = remove - 1
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
    print("Press 1 to, Add a task.")
    print("Press 2 to, Remove a task.")
    print("Press 3 to, Show list.")
    print("Press 4 to, Reset list.")
    print("Press 5 to, Change list.")
    choice = input("Enter Choice: ")
    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        print_list()
    elif choice == "4":
        reset_list()
    elif choice == "5":
        listchoice()
    else:
        print("Invalid input")
        show_menu()


##
##
##
##

def listchoice():
    userpick = int(input("Open List 1 , 2, or 3"))
    if userpick==1:
        while True:
            show_menu()
    elif userpick==2:
        while True:
            show_menu2()
    elif userpick==3:
        while True:
            show_menu3()
    else:
        print("Invalid input")
"""
SELECTS  LIST 
"""

listchoice()
