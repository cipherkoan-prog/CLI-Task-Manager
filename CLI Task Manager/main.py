from task_manager import TaskManager

if __name__ == "__main__":
    app = TaskManager()

    while True:
        print("\n===== Task Manager =====")
        print("1. Add Task.")
        print("2. delete Task")
        print("3. View Task")
        print("4. Mark Completed")
        print("5. Search Task")
        print("6. Sort by Priority")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            app.add_task()
        elif choice == "2":
            app.delete_task()
        elif choice == "3":
            app.view_tasks()
        elif choice == "4":
            app.mark_completed()
        elif choice == "5":
            app.search_tasks()
        elif choice == "6":
            app.sort_by_priority()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice!")

        