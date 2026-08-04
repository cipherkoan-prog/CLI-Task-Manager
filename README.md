# 📝 CLI Task Manager

A simple yet powerful **Command-Line Task Manager** built with **Python** using **Object-Oriented Programming (OOP)**. This application helps users manage daily tasks efficiently by allowing them to add, delete, search, sort, and mark tasks as completed. All tasks are stored in a JSON file for persistent storage.

---

## 🚀 Features

* ✅ Add new tasks
* 🗑️ Delete existing tasks
* 📋 View all tasks
* ✔️ Mark tasks as completed
* 🔍 Search tasks by title
* 📌 Sort tasks by priority (High, Medium, Low)
* 💾 Automatic data storage using JSON
* 🧱 Modular project structure using OOP

---

## 🛠️ Built With

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **JSON** (for persistent data storage)

---

## 📂 Project Structure

```text
CLI Task Manager/
│
├── main.py              # Entry point of the application
├── task.py              # Task class
├── task_manager.py      # Task management logic
├── data_handler.py      # Load and save tasks to JSON
├── tasks.json           # Stores task data
└── README.md            # Project documentation
```

---

## ▶️ How to Run

1. Clone this repository:

```bash
git clone <repository-url>
```

2. Open the project folder.

3. Run the application:

```bash
python main.py
```

---

## 📸 Preview

Example menu:

```text
===== Task Manager =====

1. Add Task
2. Delete Task
3. View Tasks
4. Mark Completed
5. Search Task
6. Sort by Priority
7. Exit
```

---

## 📁 Data Storage

All tasks are saved in a `tasks.json` file.

Each task contains:

* Title
* Priority
* Completion Status

Example:

```json
[
    {
        "title": "Complete Python project",
        "priority": "High",
        "completed": false
    }
]
```

---

## 💡 Concepts Practiced

* Object-Oriented Programming (Classes & Objects)
* File Handling
* JSON Serialization
* Modular Programming
* User Input Validation
* Lists and Dictionaries
* Functions and Methods

---

## 🎯 Future Improvements

* ✏️ Edit existing tasks
* 📅 Add due dates
* 🏷️ Task categories
* 🎨 Colored terminal output
* 📊 Task statistics
* ⏰ Task reminders
* ⭐ Task filtering (Completed/Pending)

---

## 👨‍💻 Author

**Sayan Oraon**

If you found this project helpful or interesting, feel free to ⭐ the repository!
