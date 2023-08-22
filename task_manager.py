import json
import os

tasks = []

# import data from file
def read_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
        return tasks
    else:
        return []

# save tasks to file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

# add task
def add_task():
    title = input("Task title: ")
    description = input("Task description: ")
    new_task = {"title": title, "description": description}
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")

# list tasks
def list_tasks():
    if not tasks:
        print("No tasks found!")
        return
    print("Task list:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['title']}")

def main():
    global tasks
    tasks = read_tasks()
    while True:
        print("\nCLI Task Manager")
        print("1. Add task")
        print("2. List tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            save_tasks(tasks)  # Save tasks before exiting
            print("Thank you for using CLI Task Manager!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
