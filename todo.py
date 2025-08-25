import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file, or create file if missing."""
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "w") as f:
            pass
    with open(TASKS_FILE, "r") as f:
        tasks = f.read().splitlines()
    return tasks

def save_tasks(tasks):
    """Save tasks back to file."""
    with open(TASKS_FILE, "w") as f:
        f.write("\n".join(tasks))

def show_tasks(tasks):
    if not tasks:
        print("📂 No tasks found!")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"🗑️ Removed: {removed}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
