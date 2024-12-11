def add_item3():
    item = input("Enter a task: ")
    toDoList3.append(item)
    for i in range(0, len(toDoList3)):
        print(str(i + 1) + ". " + toDoList3[i])


def remove_item3():
    for i in range(0, len(toDoList3)):
        print(str(i + 1) + ". " + toDoList3[i])
    remove3 = int(input("Enter a the # to remove: "))
    remove3 = remove3 - 1
    toDoList3.pop(remove3)
    for i in range(0, len(toDoList3)):
        print(str(i + 1) + ". " + toDoList3[i])


def print_list3():
    for i in range(0, len(toDoList3)):
        print(str(i + 1) + ". " + toDoList3[i])


def reset_list3():
    toDoList3.clear()
    for i in range(0, len(toDoList3)):
        print(str(i + 1) + ". " + toDoList3[i])


def show_menu3():
    print("Press 1 to, Add a task.")
    print("Press 2 to, Remove a task.")
    print("Press 3 to, Show list.")
    print("Press 4 to, Reset list.")
    choice = input("Enter Choice: ")
    if choice == "1":
        add_item3()
    elif choice == "2":
        remove_item3()
    elif choice == "3":
        print_list3()
    elif choice == "4":
        reset_list3()
    else:
        print("Invalid input")
        show_menu3()