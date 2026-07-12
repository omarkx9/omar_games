print("📑-------welcome to the To-Do List App!-------📑\n")
tasks = []
while True:
    print("""
    Choose an option:
    1. Add task
    2. View tasks
    3. Delete task
    4. Exit
    """)
    choice = int(input("Enter your choice (1-4): "))
    if choice < 5 and choice > 0:
        if choice == 1:
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"👌 Task ({task}) added!\n")
        elif choice == 2:
            i = 0
            print("📃 Your tasks 📋:")
            for x in tasks:
                i += 1
                print(i,".",x)
        elif choice == 3:
            i = 0
            print("📃 Your tasks 📋:")
            for x in tasks:
                i += 1
                print(i,".",x)
            task_number = int(input("Enter task number to delet: "))
            del_tasks = tasks.pop(task_number-1)
            print(f"🗑️ Deleted: {del_tasks}")
        else:
            print("👋 Good bye!")
            break
    else:
        print("🙅‍♂️ Invalid Coice.........Try again")