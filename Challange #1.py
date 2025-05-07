#tasks = ["Walk dog", "Do homework", "Wash dishes", "Go to gym"]
#write a function that removews a take from the list based on its name
#dont assume task names are perfectly typed e.g not capitalized or is when it shouldn't be.
#if task is found remove it and print message. task ____ removed successfully if not found print task not found

tasks = ["Walk dog", "Do homework", "Wash dishes", "Go to gum"]

def removeTaskByName(tasks):
   listRemove= input("Please Enter the task you want to remove: ")
   for index, task in enumerate(tasks):
       if listRemove.lower() == task.lower():
           del tasks[index]
           print(f"Removed '{task}' Successfully!")
           break
   else:
       print("Task not found.")


removeTaskByName(tasks)