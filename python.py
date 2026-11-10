my_tasks = []                          # 1. Create the empty list ONCE, before the loop

while True:                            # 2. Repeat the menu forever (until break)
    print("\n1. Add task")             # 3. Show menu. \n means "start a new line"
    print("2. View tasks")
    print("3. Quit")
    choice = input("Choose: ")         # 4. INPUT: ask what they want to do

    if choice == "1":                  # 5. User wants to add
        task = input("Enter task: ")   #    INPUT: get the task text
        my_tasks.append(task)          #    PROCESS: store it in the list
        print("Task added!")           #    OUTPUT: confirm

    elif choice == "2":                # 6. User wants to view
        if not my_tasks:               #    "not my_tasks" is True when the list is empty
            print("No tasks yet.")
        else:
            for task in my_tasks:      #    OUTPUT: loop through and print each
                print("-", task)

    elif choice == "3":                # 7. User wants to quit
        break                          #    Exit the while loop, program ends

    else:                              # 8. Anything else
        print("Invalid choice.")