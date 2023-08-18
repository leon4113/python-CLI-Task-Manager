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
        
