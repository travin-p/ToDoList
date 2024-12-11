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
    choice = input("Enter Choice: ")
    if choice == "1":
        add_item2()
    elif choice == "2":
        remove_item2()
    elif choice == "3":
        print_list2()
    elif choice == "4":
        reset_list2()
    else:
        print("Invalid input")
        show_menu2()