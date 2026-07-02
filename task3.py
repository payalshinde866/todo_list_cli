print("===== TO-DO LIST MANAGER =====")

tasks = []

while True:
    print("\nMenu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ").strip()
        if task:
            tasks.append(task)
            print("Task added successfully.")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            print("\nCurrent Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

            try:
                number = int(input("Enter task number to delete: "))
                if 1 <= number <= len(tasks):
                    removed = tasks.pop(number - 1)
                    print(f"'{removed}' deleted successfully.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using the To-Do List Manager.")
        break

    else:
        print("Invalid choice. Please try again.")