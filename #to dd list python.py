class ToDoList:
    def __init__(self):
        self.tasks = []  # Initialize an empty list to store tasks

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task Added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        print("\n----- To-Do List -----")
        for i, task in enumerate(self.tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['task']} [{status}]")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task {task_number} updated to: {new_task}")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task removed: {removed_task['task']}")
        else:
            print("Invalid task number.")

    def mark_complete(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")


# Main program
todo = ToDoList()

while True:
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        todo.add_task(task)
    elif choice == '2':
        todo.view_tasks()
    elif choice == '3':
        todo.view_tasks()
        task_number = int(input("Enter the task number to update: "))
        new_task = input("Enter the new task: ")
        todo.update_task(task_number, new_task)
    elif choice == '4':
        todo.view_tasks()
        task_number = int(input("Enter the task number to delete: "))
        todo.delete_task(task_number)
    elif choice == '5':
        todo.view_tasks()
        task_number = int(input("Enter the task number to mark as complete: "))
        todo.mark_complete(task_number)
    elif choice == '6':
        print("Exiting the To-Do List Manager. Stay productive!")
        break
    else:
        print("Invalid choice. Please try again.")
 