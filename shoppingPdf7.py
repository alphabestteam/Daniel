def main():
    bill = 0
    shopping_list = []
    shopping_continue = True

    while shopping_continue:
        user_choosen = int(input(
            "Hello sir.\n to add item please press 1 \n"
            " to remove item please press 2 \n"
            " to finish shopping please press 3"))
        while 1 > user_choosen > 3:
            user_choosen = int(input(
                "You've entered the wrong number, please try again: "))

        if user_choosen == 1:
            item_name = input("Enter product name: ")
            item_quantity = int(input("Enter quantity: "))

            for item in shopping_list:
                if item_name in item:
                    item[item_name]["quantity"] += item_quantity
                    bill += item[item_name]["price"] * item_quantity
                    break
            else:  # if after running through shopping list the item doesnt exist, ask for price and add to list:
                item_price = float(input("Enter product price: "))
                new_item = {item_name: {"price": item_price, "quantity": item_quantity}}
                shopping_list.append(new_item)
                bill += item_price * item_quantity
                
        elif user_choosen == 2:
            remove_item = input("Enter the name of the item to remove: ")
            item_exist = False
            for item in shopping_list:
                if remove_item in item:
                    item_exist = True
                    item_qut_remove = int(input("Enter the quantity to remove: "))
                    while item_qut_remove > item[remove_item]["quantity"]:
                        item_qut_remove = int(
                            input(f"You have only {item[remove_item]['quantity']} left,  Enter amounte again: "))
                    item[remove_item]["quantity"] -= item_qut_remove
                    bill -= item[remove_item]["price"] * item_qut_remove
                if item[remove_item]["quantity"] == 0:
                    shopping_list.remove(item)
                    print(f"You removed {remove_item} from you shopping list.")
            if item_exist == False:
                print("Item not in you shopping list")
        elif user_choosen == 3:
            shopping_continue = False
            print(f"The bill is: {bill}\n")
            print("Your shopping list: ")
            for item in shopping_list:
                for item_name, item_values in item.items():
                    print(f"Item: {item_name}   Price: {item_values['price']} * Quantity: {item_values['quantity']}")

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
