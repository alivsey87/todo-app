def main():
    print("\nWelcome to the To-Do List!")
    tasks = []
    # loop entered to keep program running until a break
    while True:
        # Display the menu...with STYLE :)
        print(" ________________")
        print("       MENU")
        print(" ----------------")
        print(" ________________")
        print("|                |")
        print("| 1: Add task    |")
        print("|                |")
        print("| 2: Delete task |")
        print("|                |")
        print("| 3: View tasks  |")
        print("|                |")
        print("| 4: Quit        |")
        print(" ~~~~~~~~~~~~~~~~")
        
        # loop entered if invalid menu choice to keep from returning to main menu
        while True:
            try:
                user_input = int(input("\nMake a selection: "))
                if 1 <= user_input <= 4:
                    break  # Valid input made, now exit loop
                else:
                    print("\nPlease choose a menu item from the list (1 - 4)")
            except ValueError:
                print("\nInput needs to be a number!")

        # loop entered if no valid entry
        if user_input == 1:
            while True:
                try:
                    task = input("\nWhat task would you like to add? ").strip().lower()
                    if not task:
                        print("\n...enter something please")
                    elif task in tasks:
                        print("\nThis task is already in the list")
                    else:
                        tasks.append(task)
                        print(f"\nSuccessfully added {task}")
                        break  # Exit the loop after successfully adding a task
                except ValueError:
                    print("\nPlease type in a valid string!")

        elif user_input == 2:
            if len(tasks) == 0:
                print("\nThere are no tasks to delete")
            else:
                # yet another loop entered until valid entry...or user enters nothing
                while True:
                    try:
                        task = input("\nWhat task would you like to delete? ").strip().lower()
                        if not task:
                            print("\n...very well, nothing deleted")
                            break  # Exit the loop if no input is provided
                        elif task not in tasks:
                            print(f"\n{task} not in task list")
                        else:
                            tasks.remove(task)
                            print(f"\nSuccessfully deleted {task}")
                            break  # Exit the loop after successfully deleting a task
                    except ValueError:
                        print("\nPlease type in a valid string!")

        elif user_input == 3:
            if len(tasks) == 0:
                print("\nThere are no tasks")
            else:
                print("\nYour tasks:\n")
                for task in tasks:
                    print(f"- {task}")
        # the point where the outer loop breaks and the app ends
        elif user_input == 4:
            print("\nGoodbye!")
            break
        
main()        