def display_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    if tasks:
        print("#################")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("#################\n")  # Added line break here
    else:
        print("No tasks found.")

def remove_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter task number to remove: "))
    if 0 < task_num <= len(tasks):
        removed_task = tasks.pop(task_num - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()