import time
print("\n\t 📑-------Welcome Task Manager App!-------📑\n")
def empty(x):
    return bool(x)
def show(**y):
    for a,b in y.items():
        print(f"ID({a}) {b["task"]} {b["status"]}")
    print()
all_tasks = """
            {==========_Options_==========}
               1. Add Task
               2. Show Tasks
               3. Complete Tasks
               4. Delete Tasks
               5. Search Task
               6. Statistics
               7. Exit
            {=============================}
"""
i = 1
tasks = {}
while True:
    print(all_tasks)
    choice = input("Chose Your Move: ").strip()
    if choice.isdigit():
        choice = int(choice)
        if choice < 8 and choice > 0:
            if choice == 1:
                name_task = input("Enter The Task: ").strip().title()
                tasks[str(i)] = {
                    "task" : name_task,
                    "status" : "[Pending]"
                }
                i += 1
                time.sleep(1)
                print(f"Task {name_task} Added! ")
            elif choice == 2:
                if empty(tasks):
                    show(**tasks)
                else:
                    print("\nSorry You Dont Have Any Tasks")
            elif choice == 3:
                if empty(tasks):
                    show(**tasks)
                    task_done = input("Enter Wich Task Is Completed\nBy ID: ").strip().title()
                    if task_done in tasks:
                        tasks[task_done]["status"] = "[completed]"
                    else:
                        if task_done.isdigit():
                            print(f"ID({task_done}) This ID Isn't In Your Tasks")
                        else:
                            print(f"({task_done}) Isn't a Number??")
                else:
                    print("\nSorry You Dont Have Any Tasks")
            elif choice == 4:
                if empty(tasks):
                    show(**tasks)
                    num_of_del = input("Enter The Nubmer Of Task To Delete\nBy ID: ").strip()
                    if num_of_del.isdigit():
                        if num_of_del in tasks:
                            tasks.pop(num_of_del)
                        else:
                            print(f"{num_of_del} Is Out Of The Range....")
                    else:
                        print(f"{num_of_del} That Isn't A Number....")
                else:
                    print("There Are Not Tasks To Delete")
            elif choice == 5:
                if empty(**tasks):
                    pass
                else:
                    print("There Are Not Tasks To Search...")
            elif choice == 6:
                pass
            else:
                time.sleep(1)
                print("Nice To See You Goodbye!")
                break
        else:
            print("Invalid Choice... Please Enter Number Betwen(1,7)")
    else:
        print(f"Invalid Choice... {choice} Is Not Number")
