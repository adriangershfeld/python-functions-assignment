# Task 1: Write a function that lets the user add items to a list.

def add_to_list(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

# Task 2: Include a function to remove items from the list.

def remove_from_list(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} not found in the list.")

# Task 3: Add a function that prints out the entire list in a formatted way.

def print_formatted(shopping_list):
    if shopping_list:
        print("\nCurrent Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("\nThere are no items in the list.")

shopping_list = []

while True:

    user_choice = input("Would you like to [A]dd an item, [R]emove an item, [P]rint the shopping list, or [Q]uit? ").upper()

    if user_choice == 'A':
        add_to_list(shopping_list)
    elif user_choice == 'R':
        remove_from_list(shopping_list)
    elif user_choice == 'P':
        print_formatted(shopping_list)
    elif user_choice == 'Q':
        print("Exiting Shopping List Maker!")
        break
    else:
        print("Invalid Choice. Please try again.")