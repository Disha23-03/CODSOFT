tasks=[]
while True:
    print("\n==== To-Do List ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")


    choice = input("Enter your choice (1-4): ")

    if choice=="1":
        task=input("Enter task: ")
        tasks.append(task)
        print("Your task was added! ")
    elif choice=="2":
        if not tasks:
            print("No tasks found: ")
        else:
            print("\n Your tasks: ")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == "3":
        if not tasks:
            print("No tasks to be marked as done. ")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                done_index = int(input("Enter task number to mark as done: ")) - 1
                removed = tasks.pop(done_index)
                print(f"Task '{removed}' marked as done and removed.")
            except (ValueError, IndexError):
                print("Invalid task number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-4.")