import json
import os

# import data from file
def read_task():
    if os.path.exists('task.json'):
        with open('task.json', 'r') as f:
            task = json.load(f)
        return task
    else:
        return []
    
# save task to file
def save_task(task):
    with open('task.json', 'w') as f:
        json.dump(task, f)
        
# add task
def add_task(task):
    title = input("Task title: ")
    description = input("Task description: ")
    newTask = {"title": title, "description": description}
    task.append(newTask)
    save_task(task)
    print("Task added successfully!")
    
# list task
def list_task(task):
    if not task:
        print("No task found!")
        return
    print("Task list:")
    for index, task in enumerate(task, start=1):
        print(f"{index+1}. {task['title']}")
        
def main():
    task = read_task()
    while True:
        print("\nCLI Task Manager")
        print("1. Add task")
        print("2. List task")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(task)
        elif choice == "2":
            list_task(task)
        elif choice == "3":
            print("Thank you for using CLI Task Manager!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()