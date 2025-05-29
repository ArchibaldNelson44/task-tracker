from datetime import datetime

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


# Define the Task class
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description} ({self.timestamp})"


# Save all tasks to file
def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task.description}|{task.completed}|{task.timestamp}\n")


# Load tasks from file (if it exists)
def load_tasks(filename="tasks.txt"):
    tasks = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    desc, completed, timestamp = parts
                    task = Task(desc)
                    task.completed = completed == "True"
                    task.timestamp = timestamp
                    tasks.append(task)
    except FileNotFoundError:
        pass
    return tasks


# Main program
def display_menu():
    print("\n" + CYAN + "=" * 30)
    print("       📝 TASK TRACKER MENU")
    print("=" * 30 + RESET)
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark a task as complete")
    print("4. Save and Exit")



tasks = load_tasks()

while True:
    display_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        if not tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    elif choice == "2":
        desc = input("Enter task description: ")
        tasks.append(Task(desc))
        print("Task added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
            try:
                index = int(input("Enter task number to mark complete: ")) - 1
                if 0 <= index < len(tasks):
                    tasks[index].mark_complete()
                    print("Task marked complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        save_tasks(tasks)
        print("Tasks saved. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose 1-4.")
