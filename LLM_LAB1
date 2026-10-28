def show_menu():
    """Displays the main menu options."""
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

def main():
    tasks = []
    
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ").strip()
        
        # 1. View Tasks
        if choice == "1":
            if not tasks:
                print("\nYour to-do list is empty.")
            else:
                print("\n--- Current Tasks ---")
                for i, task in enumerate(tasks, 1):
                    status = "[X]" if task["completed"] else "[ ]"
                    print(f"{i}. {status} {task['name']}")
        
        # 2. Add Task
        elif choice == "2":
            task_name = input("\nEnter the task description: ").strip()
            if task_name:
                tasks.append({"name": task_name, "completed": False})
                print(f"'{task_name}' has been added successfully.")
            else:
                print("Error: Task description cannot be empty.")
        
        # 3. Mark Task as Completed
        elif choice == "3":
            if not tasks:
                print("\nYour to-do list is empty.")
                continue
            
            task_name = input("\nEnter the name of the task to mark as completed: ").strip()
            found = False
            for task in tasks:
                if task["name"].lower() == task_name.lower():
                    task["completed"] = True
                    print(f"'{task['name']}' has been marked as completed.")
                    found = True
                    break
            if not found:
                print(f"Error: Task '{task_name}' not found.")
        
        # 4. Remove Task
        elif choice == "4":
            if not tasks:
                print("\nYour to-do list is empty.")
                continue
            
            task_name = input("\nEnter the name of the task to remove: ").strip()
            initial_count = len(tasks)
            # Filter out the task matching the given name (case-insensitive)
            tasks = [task for task in tasks if task["name"].lower() != task_name.lower()]
            
            if len(tasks) < initial_count:
                print(f"'{task_name}' has been removed.")
            else:
                print(f"Error: Task '{task_name}' not found.")
        
        # 5. Exit
        elif choice == "5":
            print("\nGoodbye!")
            break
        
        # Invalid Choice Handling
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()