snack_inventory = []


def display_inventory():
    if not snack_inventory:
        print("No snacks available.")
    else:
        print("Snack Inventory:")
        print("ID  |  Name  |  Price  |  Availability")
        print("-------------------------------------")
        for snack in snack_inventory:
            print(
                f"{snack['id']:3} | {snack['name']:6} | {snack['price']:7.2f} | {snack['availability']}"
            )


def add_snack():
    snack = {}
    snack['id'] = int(input("Enter the snack ID: "))
    snack['name'] = input("Enter the snack name: ")
    snack['price'] = float(input("Enter the snack price: "))
    snack['availability'] = 'yes'
    snack_inventory.append(snack)
    print("Snack added successfully.")


def remove_snack():
    snack_id = int(input("Enter the snack ID to remove: "))
    for snack in snack_inventory:
        if snack['id'] == snack_id:
            snack_inventory.remove(snack)
            print("Snack removed successfully.")
            return
    print("Snack not found.")


def update_availability():
    snack_id = int(input("Enter the snack ID to update availability: "))
    for snack in snack_inventory:
        if snack['id'] == snack_id:
            new_availability = input("Enter the new availability (yes or no): ")
            snack['availability'] = new_availability
            print("Availability updated successfully.")
            return
    print("Snack not found.")


def sell_snack():
    snack_id = int(input("Enter the snack ID to sell: "))
    for snack in snack_inventory:
        if snack['id'] == snack_id:
            if snack['availability'] == 'yes':
                snack['availability'] = 'no'
                print("Snack sold successfully.")
                return
            else:
                print("Snack is not available for sale.")
                return
    print("Snack not found.")


def main():
    while True:
        print("\n===== Canteen Snack Inventory =====")
        print("1. Display Inventory")
        print("2. Add Snack")
        print("3. Remove Snack")
        print("4. Update Availability")
        print("5. Sell Snack")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_inventory()
        elif choice == '2':
            add_snack()
        elif choice == '3':
            remove_snack()
        elif choice == '4':
            update_availability()
        elif choice == '5':
            sell_snack()
        elif choice == '6':
            print("Thank you for using the snack inventory management system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
