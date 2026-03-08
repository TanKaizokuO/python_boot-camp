import os

TASKS_FILE = "tasks.txt"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip().rsplit("||", 1) for line in file.readlines()]
        for task in tasks:
            if task[1] == "done":
                task[1] = True
            else:
                task[1] = False
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            status = "done" if task[1] else "not done"
            file.write(f"{task[0]}||{status}\n")


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task[1] else "✗"
        print(f"{idx}. {task[0]} [{status}]")


def taskmanager():
    lst = load_tasks()
    while True:
        print("\n--------------------Task Manager-------------------------")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks(lst)

        elif choice == "2":
            task_name = input("Enter task name: ")
            lst = load_tasks()
            lst.append([task_name, False])
            save_tasks(lst)
            print("Task added.")

        elif choice == "3":
            lst = load_tasks()
            display_tasks(lst)
            task_num = int(input("Enter task number to mark as done: "))
            if 0 < task_num <= len(lst):
                lst[task_num - 1][1] = True
                save_tasks(lst)
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        elif choice == "4":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid option. Please try again.")


taskmanager()
