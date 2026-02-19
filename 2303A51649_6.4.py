#Complete the methods to:
#1. Display student details
#2. Check if student's marks are above class average

class Student:
    def __init__(self, name, roll_number, marks, class_average):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.class_average = class_average

  
    def display_details(self):
        print("Student Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)

  
    def check_performance(self):
        if self.marks > self.class_average:
            return "Performance: Above Class Average"
        else:
            return "Performance: Below Class Average"



s1 = Student("Ram", 101, 85, 75)

s1.display_details()
print(s1.check_performance())

#Identify even numbers, calculate their square, and print them.

sensor_readings = [10, 15, 22, 33, 40, 55]

for reading in sensor_readings:
    
    if reading % 2 == 0:
        square = reading ** 2
        print(f"Even Reading: {reading}, Square: {square}")

#Generate deposit and withdrawal methods with balance validation.

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"Updated Balance: {self.balance}")

    # Withdrawal method
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Remaining Balance: {self.balance}")


# Sample Usage
acc = BankAccount("Ram", 1000)

acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)




#Generate a while loop to print students scoring above 75.
 
students = [
    {"name": "Ram", "score": 80}, 
    {"name": "Rahul", "score": 65},
    {"name": "Sneha", "score": 90},
    {"name": "Priya", "score": 70}
]

index = 0

while index < len(students):
    if students[index]["score"] > 75:
        print(students[index]["name"], "is eligible for scholarship")
    index += 1


#Generate methods to add/remove items, calculate total, and apply discount.

class ShoppingCart:
    def __init__(self):
        self.items = []

    # Add item
    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})
        print(f"{name} added to cart")

    # Remove item
    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                print(f"{name} removed from cart")
                return
        print("Item not found")

    # Calculate total
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]

        # Apply discount
        if total > 1000:
            discount = total * 0.1
            total -= discount
            print("Discount Applied: 10%")

        return total


# Sample Usage
cart = ShoppingCart()

cart.add_item("Laptop", 800, 1)
cart.add_item("Mouse", 200, 2)

cart.remove_item("Mouse")

print("Total Bill:", cart.calculate_total())
