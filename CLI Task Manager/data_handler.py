import json

FILE_PATH = "tasks.json"

def load_tasks():
    try:
        with open(FILE_PATH, "r")as file:
            tasks = json.load(file)
            return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)