tasks = []

while True:
    action = input("Add, view, delete, or quit? ").strip().lower()

    if action == "add":
        task = input("Enter task: ").strip()
        if task:
            tasks.append(task)
        else:
            print("Task cannot be empty.")
    elif action == "view":
        if not tasks:
            print("No tasks yet.")
        else:
            print("Your tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
    elif action == "delete":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("Select a task to delete")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")
            choice = input("Enter task number:")
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a number.")
    elif action == "quit":
        print("Goodbye")
        break
    else:
        print("Invalid choice.")

