tasks = []

def add_task():
    task_name = input("Enter task name: ")
    assigned_member = input("Enter assigned team member: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    
    task = {
        "name": task_name,
        "assigned_member": assigned_member,
        "deadline": deadline,
        "status": "To Do"
    }
    
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks found.\n")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. Name: {task['name']}, Assigned Member: {task['assigned_member']}, Deadline: {task['deadline']}, Status: {task['status']}")
        print()

def update_task_status(index, new_status):
    tasks[index]['status'] = new_status
    print(f"Task status updated to {new_status} successfully!\n")

def view_task_details(index):
    task = tasks[index]
    print(f"\nTask Details for {task['name']}:")
    print(f"Assigned Member: {task['assigned_member']}")
    print(f"Deadline: {task['deadline']}")
    print(f"Status: {task['status']}\n")

def main():
    while True:
        print("Project Task Tracker")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. View Task Details")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            if tasks:
                task_index = int(input("Enter the task number to update status: ")) - 1
                if 0 <= task_index < len(tasks):
                    new_status = input("Enter the new status (To Do/In Progress/Done): ")
                    update_task_status(task_index, new_status)
                else:
                    print("Invalid task number. Please enter a valid number.\n")
            else:
                print("No tasks available. Please add a task first.\n")
        elif choice == '4':
            view_tasks()
            if tasks:
                task_index = int(input("Enter the task number to view details: ")) - 1
                if 0 <= task_index < len(tasks):
                    view_task_details(task_index)
                else:
                    print("Invalid task number. Please enter a valid number.\n")
            else:
                print("No tasks available. Please add a task first.\n")
        elif choice == '5':
            print("Exiting Project Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.\n")

if __name__ == "__main__":
    main()
