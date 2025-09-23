tasks_file = "tasks.txt"

# Load tasks from file
try:
    with open(tasks_file, "r") as f:
        tasks = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    tasks = []

while True:
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":  # View tasks
        if not tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":  # Add task
        task = input("Enter a new task: ").strip()
        if task:
            tasks.append(task)
            with open(tasks_file, "w") as f:
                for t in tasks:
                    f.write(t + "\n")
            print(f"Task '{task}' added successfully!")
        else:
            print("Task cannot be empty!")

    elif choice == "3":  # Remove task
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    with open(tasks_file, "w") as f:
                        for t in tasks:
                            f.write(t + "\n")
                    print(f"Task '{removed}' removed successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Enter a valid number.")

    elif choice == "4":  # Exit
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
