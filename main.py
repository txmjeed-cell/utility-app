# Vending Machine Application
# Utility App Assignment
# Language: Python 3
# Description: Console-based vending machine using OOP

class Item:
    def __init__(self, code, name, price, category, stock):
        self.code = code
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def is_available(self):
        return self.stock > 0


class VendingMachine:
    def __init__(self):
        self.items = {
            "A1": Item("A1", "Coke", 1.50, "Cold Drinks", 5),
            "A2": Item("A2", "Water", 1.00, "Cold Drinks", 5),
            "B1": Item("B1", "Coffee", 2.00, "Hot Drinks", 4),
            "B2": Item("B2", "Tea", 1.80, "Hot Drinks", 4),
            "C1": Item("C1", "Chocolate Bar", 1.20, "Snacks", 6),
            "C2": Item("C2", "Biscuits", 1.00, "Snacks", 6)
        }
        self.balance = 0.0

    def display_menu(self):
        print("\n====== VENDING MACHINE MENU ======")
        categories = set(item.category for item in self.items.values())

        for category in categories:
            print(f"\n-- {category} --")
            for item in self.items.values():
                if item.category == category:
                    if item.stock > 0:
                        print(f"{item.code}: {item.name} - £{item.price}")
                    else:
                        print(f"{item.code}: {item.name} - OUT OF STOCK")

    def insert_money(self):
        while True:
            try:
                amount = float(input("\nInsert money (£): "))
                if amount <= 0:
                    print("Please insert a positive amount.")
                else:
                    self.balance += amount
                    print(f"Current balance: £{self.balance:.2f}")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

    def select_item(self):
        code = input("\nEnter item code: ").upper()

        if code not in self.items:
            print("Invalid item code.")
            return

        item = self.items[code]

        if not item.is_available():
            print("Sorry, this item is out of stock.")
            return

        if self.balance < item.price:
            print("Insufficient balance.")
            return

        item.stock -= 1
        self.balance -= item.price
        print(f"\nDispensing {item.name}... Enjoy!")

        self.suggest_item(item.category)

    def suggest_item(self, current_category):
        for item in self.items.values():
            if item.category != current_category and item.stock > 0:
                print(f"Suggestion: Try {item.name} for £{item.price}")
                break

    def return_change(self):
        print(f"\nChange returned: £{self.balance:.2f}")
        self.balance = 0.0

    def run(self):
        print("Welcome to the Vending Machine!")
        self.insert_money()

        while True:
            self.display_menu()
            self.select_item()

            choice = input("\nBuy another item? (y/n): ").lower()
            if choice != "y":
                self.return_change()
                print("Thank you for using the vending machine!")
                break


if __name__ == "__main__":
    vm = VendingMachine()
    vm.run()
