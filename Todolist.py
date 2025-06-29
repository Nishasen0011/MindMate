📋 Smart To-Do App (Real Terminal Version by Nisha)

import os from datetime import datetime import random

-----------------------------

🔐 Password Setup

PASSWORD = "nisha123"

-----------------------------

📌 Motivational Quotes

QUOTES = [ "Keep going, you're getting stronger!", "Code. Learn. Repeat.", "You're one step closer to Google!", "Make progress, not excuses." ]

-----------------------------

📋 Task Structure

Each task = [description, category, due_date, status]

tasks = []

-----------------------------

📤 Export Tasks

def export_tasks(): with open("todo_export.txt", "w") as file: for i, t in enumerate(tasks, 1): file.write(f"{i}. {t[0]} | Category: {t[1]} | Due: {t[2]} | Status: {t[3]}\n") print("\n📤 Exported to todo_export.txt\n")

-----------------------------

📅 Check if Task is Due Today

def is_today(date_str): return date_str == datetime.today().strftime('%Y-%m-%d')

-----------------------------

✔️ Mark Task as Done

def mark_done(): view_tasks() try: i = int(input("Enter task number to mark as done: ")) tasks[i-1][3] = "Completed" print("✔️ Task marked as done!\n") except: print("❌ Invalid task number.\n")

-----------------------------

❌ Delete Task

def delete_task(): view_tasks() try: i = int(input("Enter task number to delete: ")) tasks.pop(i-1) print("🗑️ Task deleted.\n") except: print("❌ Invalid task number.\n")

-----------------------------

🔍 Search by Category

def search_by_category(): cat = input("Enter category to search: ").capitalize() found = False for i, t in enumerate(tasks, 1): if t[1] == cat: print(f"{i}. {t[0]} | Due: {t[2]} | Status: {t[3]}") found = True if not found: print("❌ No tasks found in that category.\n")

-----------------------------

📆 Show Today's Tasks

def show_today(): today = datetime.today().strftime('%Y-%m-%d') print(f"\n📅 Tasks for Today ({today}):") found = False for i, t in enumerate(tasks, 1): if t[2] == today: print(f"{i}. {t[0]} | Category: {t[1]} | Status: {t[3]}") found = True if not found: print("🎉 No tasks due today!\n")

-----------------------------

➕ Add Task

def add_task(): task = input("Task description: ") category = input("Category (Study/Health/Work): ").capitalize() due = input("Due date (YYYY-MM-DD): ") tasks.append([task, category, due, "Pending"]) print("✅ Task added!\n")

-----------------------------

📋 View All Tasks

def view_tasks(): if not tasks: print("📭 No tasks added yet.\n") return for i, t in enumerate(tasks, 1): print(f"{i}. {t[0]}\n   🏷️ {t[1]} | 📅 {t[2]} | 📌 {t[3]}")

-----------------------------

🆘 Help Section

def show_help(): print(""" 🆘 HELP MENU

1. View All Tasks: See all your saved tasks


2. Add Task: Add new task with category and due date


3. Mark as Done: Set a task as completed


4. Delete Task: Remove task from list


5. Search by Category: Filter tasks


6. Show Today's Tasks: Due today only


7. Export: Save tasks to file


8. Help: Show this menu


9. Exit """)



-----------------------------

🔐 Password Check

def check_password(): pw = input("🔒 Enter password to open To-Do App: ") return pw == PASSWORD

-----------------------------

🎬 Main Program

if check_password(): print("\n🎉 Welcome to Smart To-Do App by Nisha!") print("🌟 " + random.choice(QUOTES))

while True:
    print("""

============================== 📋 TO-DO LIST MENU 1️⃣ View All Tasks 2️⃣ ➕ Add New Task 3️⃣ ✔️ Mark Task as Done 4️⃣ 🗑️ Delete a Task 5️⃣ 🔍 Search by Category 6️⃣ 📆 Show Today's Tasks 7️⃣ 📤 Export to File 8️⃣ 🆘 Help 9️⃣ ❌ Exit

""") choice = input("Enter your choice: ")

if choice == '1': view_tasks()
    elif choice == '2': add_task()
    elif choice == '3': mark_done()
    elif choice == '4': delete_task()
    elif choice == '5': search_by_category()
    elif choice == '6': show_today()
    elif choice == '7': export_tasks()
    elif choice == '8': show_help()
    elif choice == '9':
        print("👋 Goodbye! Stay productive, Nisha!")
        break
    else:
        print("❌ Invalid choice. Please try again.\n")

else: print("🔐 Incorrect password. Access denied!")

