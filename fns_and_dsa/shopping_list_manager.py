shopping_list = []
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def check_empty_list(shopping_list_menu):
    if shopping_list_menu == []:
        print("Shopping list is empty!")
        return True
    return False

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        # Prompt for and add an item
        item_name = input("Enter the item to add: ").lower().strip()
        shopping_list.append(item_name)
        print(item_name, "has been added to shopping list successfully.")
    elif choice == '2':
        # Prompt for and remove an item
        if check_empty_list(shopping_list):
            pass
        else:
            item_name = input("Enter item to remove: ").lower().strip()
            if item_name in shopping_list:
              shopping_list.remove(item_name)
              print(item_name, "has been removed from shopping list successfully.")
            else:
                print("Item not found in list!")
    elif choice == '3':
        # Display the shopping list
        if check_empty_list(shopping_list):
            pass
        else:
            for item in shopping_list:
                print(item)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")