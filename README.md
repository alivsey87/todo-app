# To Do Application
---
---

## TABLE OF CONTENTS

1. [UI](#1-ui)

2. [Add task](#2-add-task)

3. [Delete task](#3-delete-task)

4. [View tasks](#4-view-tasks)

5. [Quit](#5-quit)

## 1. UI

There is one function here that the entire app operates from called `main()`. It initially prints a welcome message and then enters into a while loop displaying the main menu with options to choose from. I "styled" the menu to look like a page of sorts:

```py
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
```

This always displays until the user selects [Quit](#5-quit) and breaks the loop to exit the app. I also used the new line character, `\n`, very often to create space throughout the app. This snippet of code covers the main validation:

```py
while True:
            try:
                user_input = int(input("\nMake a selection: "))
                if 1 <= user_input <= 4:
                    break  # Valid input made, now exit loop
                else:
                    print("\nPlease choose a menu item from the list (1 - 4)")
            except ValueError:
                print("\nInput needs to be a number!")
```

the user enters another inner loop to ensure they are making a valid number selection and also not a string. The loop breaks when a valid choice is made.

---
---

## 2. Add task

Here a user can add a task. An array `tasks = []` is initiated at the beginning of the function to eventually store all the tasks. If the user makes this selection:

```py
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
```

another loop is entered to provide validation. A valid input is stripped of any extra space and made lower to provide case-insensitivity in the app. The task is appended to the array and the user is brought back to the main menu.

---
---

## 3. Delete task

This is where a user can delete a task. The following code covers this selection:

```py
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
```

Immediately, the user is returned to the main menu with a message indicating no tasks are present if the array is empty. If there are tasks, another validation "loop" is entered to ensure a valid task is found and deleted.

---
---

## 4. View tasks

This option simply displays tasks if any exist:

```py
elif user_input == 3:
            if len(tasks) == 0:
                print("\nThere are no tasks")
            else:
                print("\nYour tasks:\n")
                for task in tasks:
                    print(f"- {task}")
```

A for loop iterates through the array and prints the task preceded by the '-' character for a "bulleted" list style. If no tasks present, returns the user to the main menu with a message indicating such.

---
---

## 5. Quit

The option for a user to quit the application:

```py
elif user_input == 4:
            print("\nGoodbye!")
            break
```

This simply prints a goodbye message and breaks the main loop keeping the app going.

[back to top](#to-do-application)