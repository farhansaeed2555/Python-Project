tasks = []

def add_task():
    task_name = input("Enter task name: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ")
    
    task = {"name": task_name, "due_date": due_date, "priority": priority}
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks found.\n")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. Name: {task['name']}, Due Date: {task['due_date']}, Priority: {task['priority']}")
        print()

def main():
    while True:
        print("Task Management Tool")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            print("Exiting Task Management Tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
