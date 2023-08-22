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

# list tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return
    print("Task list:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']}")

def delete_task(tasks):
    if not tasks:
        print("Tasks is empty!")
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

def main():
    tasks = read_tasks()
    while True:
        print("\nCLI Task Manager")
        print("1. Add task")
        print("2. List tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)  # Save tasks before exiting
            print("Thank you for using CLI Task Manager!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
