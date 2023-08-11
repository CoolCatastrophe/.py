# to-do text in python
header = """
To-Do List
  """
print("*" * 45)
print("*" * 45)
print(f"\t\t{header.strip().upper()}")
print("*" * 45)

todo_list = []
completed_list=[]
while True:
    print("Your To-Do List:")
    print("*"*45)
    if todo_list:
        for task in range(len(todo_list)):
            print(f"{task+1}. {todo_list[task].capitalize()}")
    choice = input("Enter a command: (Type 'h' for help)-\t")
    if choice == "h":
        print(
            """
TODO LIST HELP
Type 'q' to quit 
To add a task to the todo list, type it and hit enter
To complete a todo task enter its number and hit enter
              """
        )
    elif choice == "q":
        print(f"Here are the {len(completed_list)} task/s you completed today:")
        if completed_list:
            for completed_task in completed_list:
                print(f"🎉  {completed_task}")
            print("*" * 45)
        else:
             print("Sorry! You have Completed Any Tasks Today")
        break
    elif choice.isnumeric():
        task_idx=int(choice) - 1
        if task_idx in range(len(todo_list)):
                    done = todo_list.pop(task_idx)
                    completed_list.append(done)
        else:
                print("Invalid Task number!")
    else:
        todo_list.append(choice)
    
