2# Name: Mark Dymek
# Purpose: Simple To-Do List Manager
# Date: 4/26/2025

def showMenu():
    print("\n===== To-Do List Menu =====")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Mark Task As Completed")
    print("5. Exit")
    print("============================")

def viewTasks(taskList):
    if len(taskList) == 0:
        print("\nYour task list is empty.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(taskList, start=1):
            print(f"{i}. {task}")

def addTask(taskList):
    task = input("\nEnter the task you want to add: ")
    taskList.append(task)
    print(f"Task '{task}' added successfully!")

def removeTask(taskList):
    if len(taskList) == 0:
        print("\nYour task list is empty. Nothing to remove.")
        return
    viewTasks(taskList)
    try:
        taskNumber = int(input("Enter the number of the task to remove: "))
        if 1 <= taskNumber <= len(taskList):
            removed = taskList.pop(taskNumber - 1)
            print(f"Task '{removed}' removed successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def saveTasks(taskList):
    with open("tasks.txt", "w") as file:
        for task in taskList:
            file.write(task + "\n")
    print("Tasks saved successfully!")

def loadTasks():
    taskList = []
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                task = line.strip()
                taskList.append(task)
    except FileNotFoundError:
        return []
    return taskList

def markTaskComplete(taskList):
    viewTasks(taskList)  # Helpful to show tasks before marking
    try:
        markTask = int(input("\nPlease enter the task number you would like to mark as completed: "))
        if 1 <= markTask <= len(taskList):
            index = markTask - 1
            if "[Completed]" not in taskList[index]:  # Prevent double marking
                taskList[index] = taskList[index] + " [Completed]"
                print(f"Task '{taskList[index]}' marked as completed!")
            else:
                print("Task is already marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    taskList = loadTasks()

    while True:
        showMenu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            viewTasks(taskList)
        elif choice == "2":
            addTask(taskList)
        elif choice == "3":
            removeTask(taskList)
        elif choice == "4":
            markTaskComplete(taskList)
            saveTasks(taskList)
        elif choice == "5":
            saveTasks(taskList)
            print("\nGoodbye! See you later!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
main()
