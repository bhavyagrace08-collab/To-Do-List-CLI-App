#To-Do List CLI Application

#creating an empty list to store tasks
tasks = []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())

    except FileNotFoundError:
        print("No previous tasks found. Starting a new list.")


def add_task():
    task = input("Enter your task: ")

    if task.strip() == "":
        print("Task cannot be empty!")

    else:
        tasks.append(task)
        save_tasks()
        print("Task added successfully!")


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available!")
    else:
        print("\nYour To-Do List:")

        for i, task in enumerate(tasks, start=1):
            print(i, ".", task)


# Function to remove a task
def remove_task():

    # Displaying the available tasks
    view_tasks()

    # Checking whether tasks are available
    if len(tasks) > 0:

        try:
            number = int(input("Enter task number to remove: "))

            # Checking whether the entered number is valid
            if 1 <= number <= len(tasks):

                removed = tasks.pop(number - 1)
                save_tasks()

                print("Task removed:", removed)

            else:
                print("Invalid task number!")

        except ValueError:
            print("Please enter a valid number!")
load_tasks()
# Main menu of the application
while True:

    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice! Please try again.")
