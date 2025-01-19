# Python Practice Project - Week 2 - Code:You
# Developer: Ashley Schultz
#   === To-Do List ===
#   Task:
#   WHILE Running
#       Allow for User Input
#           - Adding to List
#               - ask for # to add/for x # added do
#           - Marking task as done
#               - ask for task/update status
#           - Display list
#               - print list/status
#           - Ending the program
#       Account for
#           - Input Errors
#           - Instructions for user
#   ===================

#array created
tasks = []
#While Loop Control
while True:
    #Program Start
    print("=========== To-Do List Main Menu =============")
    print("Please select an option from the list (1-3)")
    print("==============================================")
    print("1. Add Task")
    print("2. View/Update Task")
    print("3. Exit To-Do List")
    print("==============================================")
    #get input
    selection = input("Enter your selection: ")
    #if selection
    #Add Task
    if selection == '1':
        print("=============== Add List =================")
        print("Instructions: Please use numerical values")
        try:
            numTasks = int(input("How many tasks will be added? "))
            #for numTasks do
            for numInput in range(numTasks):
                print("Instructions: Enter Task Description (ex: Clean House) ")
                task = input("Task Description: ")
                tasks.append({"task": task, "done": False})
                print("Task Recorded!")
        except ValueError:
            print("Returning to Main Menu \n")
    #View/Update
    elif selection == '2':
        if not tasks:
            print("==============================================")
            print("  Your To-Do List is Empty - Relax & Enjoy")
            print("      or select option (1) to Add Tasks \n")
        else:
            print("============ Active To-Do List ===============")
            for index, task in enumerate(tasks):
                status = "Complete!" if task["done"] else "In Progress."
                print(f"{index + 1}. {task['task']} - {status}")
            try:
                print("=================================================")
                print("Instructions: Enter task number to complete a task")
                print("or press any key not in the numbered list to return")
                print("to the main menu.")
                comp_task = int(input("Completed Task Number: ")) - 1
                if 0 <= comp_task < len(tasks):
                    tasks[comp_task]["done"] = True
                    print("Task Completed! \n")
                else:
                    print("Returning to Main Menu \n")
            except ValueError:
                print("Returning to Main Menu \n")
    #Exit
    elif selection == '3':
        print("Closing your To-Do List. Goodbye!")
        break
    #Error
    else:
        print("Returning to Main Menu \n")

