import json
import os

# import data from file
def read_tasks():
    tasks = []
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            try:    
                tasks = json.load(f)
            except json.JSONDecodeError: # if file is empty
                pass
    return tasks

# save tasks to file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

# add task
def add_task(tasks):
    title = input("Task title: ")
    description = input("Task description: ")
    new_task = {"title": title, "description": description}
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")

def tasks_empty(tasks):
    if not tasks:
        print("Tasks is empty!")
        return True
    return False

# list tasks
def list_tasks(tasks):
    if tasks_empty(tasks):
        return 
    print("Task list:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']}")

def delete_task(tasks):
    if tasks_empty(tasks):
        return
    print("Task list:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']}")
    while True:
        choice = int(input("Enter task number to delete: "))
        if choice < 1 or choice > len(tasks):
            print("Invalid task number!")
        else:
            break
    del tasks[choice - 1]
    save_tasks(tasks)
    print("Task deleted successfully!")

def update_task(tasks):
    if tasks_empty(tasks):
        return
    print("Task list:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']}")
    while True:
        choice = int(input("Enter task number to update: "))
        if choice < 1 or choice > len(tasks):
            print("Invalid task number!")
        else:
            break
    title = input("Task title: ")
    description = input("Task description: ")
    tasks[choice - 1]["title"] = title
    tasks[choice - 1]["description"] = description
    save_tasks(tasks)
    print("Task updated successfully!")

def main():
    tasks = read_tasks()
    while True:
        print("\nCLI Task Manager")
        print("1. Add task")
        print("2. List tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)  # Save tasks before exiting
            print("Thank you for using CLI Task Manager!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
