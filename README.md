#  Task Tracker – Python CLI Project

This is a simple **Task Tracker** built in Python as part of my hands-on learning during the **Google IT Automation with Python** course and personal study. It allows users to add tasks, mark them as complete, and save them to a text file.

This project helped me practice:
- Python basics
- File handling
- Input validation
- Loops and conditionals

##  Features

-  Add new tasks  
-  View current task list  
-  Mark tasks as complete  
-  Save tasks to a `task.txt` file  
-  Cleans up input and prevents empty tasks  

##  How It Works

The program runs in a simple loop using the command line:

1. Prompts the user to add or complete a task  
2. Stores each task in a list (or dictionary if extended)  
3. Saves completed tasks to a local file  
4. Ends when the user exits  

### Example:

Enter a task: Study Python
Enter a task: Go to the gym
Enter a task: done

Your tasks:

  1.  Study Python

  2.  Go to the gym

Tasks saved to task.txt.



##  Files Included

- `task_tracker.py` – main script with core logic  
- `task.txt` – stores saved tasks (created automatically)  

##  Skills Practiced

- Python input/output  
- Loops and logic control  
- Basic file I/O (`open`, `write`, `close`)  
- Clean coding habits  

##  How to Run

You can run this file in any Python 3 environment:

```bash
python3 task_tracker.py

