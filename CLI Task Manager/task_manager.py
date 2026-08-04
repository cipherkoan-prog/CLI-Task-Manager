from task import Task
from data_handler import load_tasks, save_tasks

class TaskManager:
    def __init__(self):
        self.tasks = []


    def add_task(self):
        title = input("Enter task title: ")
        priority = input("Enter task priority (High, Medium, Low): ")

        if not title or not priority:
            print("Title and Priority cannot be empty.")
            return 

        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority. Please enter High, Medium, or Low.")
            return

        task = Task(
            title,
            priority
        )

        tasks = load_tasks()

        tasks.append(task.to_dict())
        save_tasks(tasks)

        self.view_tasks()

        print(f"Task '{task.title}' added successfully.") 
    
    def delete_task(self):
        tasks = load_tasks()
        task = input("Enter the title of the task to delete: ")

        tasks = [t for t in tasks if t['title'] != task]
        save_tasks(tasks)
        print(f"Task '{task}' deleted successfully.")
        
    def view_tasks(self):
        tasks = load_tasks()
        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            status = "Completed" if task['completed'] else "Pending"
            print(f"Title: {task['title']}, Priority: {task['priority']}, Status: {status}")

    def mark_completed(self):
        tasks = load_tasks()
        task_title = input("Enter the title of the task to mark as completed: ")

        for task in tasks:
            if task['title'] == task_title:
                task['completed'] = True
                save_tasks(tasks)
                print(f"Task '{task_title}' marked as completed.")
                return
            
        print(f"Task '{task_title}' not found.")
                  
    def search_tasks(self):
        tasks = load_tasks()
        keyword = input("Enter Keyword: ")
        matching_tasks = [task for task in tasks if keyword.lower() in task['title'].lower()]
        if not matching_tasks:
            print(f"No tasks found matching '{keyword}'.")
        else:
            print(f"Tasks matching '{keyword}':")
            for task in matching_tasks:
                status = "Completed" if task['completed'] else "Pending"
                print(f"Title: {task['title']}, Priority: {task['priority']}, Status: {status}")
        return matching_tasks
    
    def sort_by_priority(self):
        tasks = load_tasks()
        priority_order = {"High": 1, "Medium": 2, "Low": 3}
        sorted_tasks = sorted(tasks, key=lambda x: priority_order.get(x['priority'], 4))
        print("Tasks sorted by priority:")
        for task in sorted_tasks:
            status = "Completed" if task['completed'] else "Pending"
            print(f"Title: {task['title']}, Priority: {task['priority']}, Status: {status}")
