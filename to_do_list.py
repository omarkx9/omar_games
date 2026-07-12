print("\n\t 📑-------welcome to the To-Do List App!-------📑")
tasks = []
while True:
    print("""
    _________________
    Choose an option:
    1. Add task
    2. View tasks
    3. Delete task
    4. Exit
    -----------------
    """)
    choice = int(input("Enter your choice (1-4): "))
    if choice < 5 and choice > 0:
        if choice == 1:
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"👌 Task ({task}) added!")
        elif choice == 2:
            if not tasks:
                print("📪 No tasks Yet")
            else:
                i = 0
                print("📃 Your tasks 📋:")
                for x in tasks:
                    i += 1
                    print(i,".",x)
        elif choice == 3:
            if not tasks:
                print("📪 No tasks Yet")
            else:
                i = 0
                print("📃 Your tasks 📋:")
                for x in tasks:
                    i += 1
                    print(i,".",x)
                task_number = int(input("Enter task number to delet: "))
                if task_number <= len(tasks) and task_number > 0:
                    del_tasks = tasks.pop(task_number-1)
                    print(f"🗑️ Deleted: {del_tasks}")
                    i = 0
                    print("📃 Your tasks 📋:")
                    for x in tasks:
                        i += 1
                        print(i,".",x)
                else:
                    print("😐  😑")
        else:
            print("👋 Good bye!")
            break
    else:
        print("🙅‍♂️ Invalid Coice.........Try again")