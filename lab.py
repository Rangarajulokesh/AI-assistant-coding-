"""

1. "Create a Python-based hotel management system using
   object-oriented programming with separate Room, Booking,
   and Hotel classes."

2. "Develop a menu-driven hotel reservation system that
   manages limited single and double rooms with dynamic
   billing calculation."

3. "Design a console hotel system in Python that tracks
   room availability, prevents invalid bookings, and
   generates revenue analytics."

4. "Implement a scalable hotel management application
   using constructors, loops, conditional statements,
   and encapsulated class design."

5. "Write a Python OOP project demonstrating real-world
   system modeling using classes, state updates, and
   revenue reporting."


=========================================================
HOTEL MANAGEMENT SYSTEM
=========================================================
"""

# Price per day
SINGLE_PRICE = 10000
DOUBLE_PRICE = 20000

class Room:
    def __init__(self, total, price):
        self.total = total
        self.available = total
        self.price = price
    def book(self):
        if self.available > 0:
            self.available -= 1
            return True
        return False
    def release(self):
        if self.available < self.total:
            self.available += 1

class Hotel:
    def __init__(self, single_count, double_count):
        self.single = Room(single_count, SINGLE_PRICE)
        self.double = Room(double_count, DOUBLE_PRICE)
        self.bookings = {}
        self.total_guests = 0
        self.total_revenue = 0
        self.total_days = 0

    def book_room(self, name, rtype, days):
        if days <= 0:
            print("Days must be at least 1."); return
        room = self.single if rtype=="single" else self.double if rtype=="double" else None
        if not room:
            print("Invalid room type."); return
        if not room.book():
            print("No rooms available."); return
        self.bookings[name] = (rtype, days)
        print("Booking confirmed.")

    def checkout(self, name):
        if name not in self.bookings:
            print("No booking found."); return
        rtype, days = self.bookings.pop(name)
        room = self.single if rtype=="single" else self.double
        room.release()
        bill = days * room.price
        self.total_revenue += bill
        self.total_guests += 1
        self.total_days += days
        print(f"Bill: ₹{bill}")

    def report(self):
        print("\nTotal Guests:", self.total_guests)
        print("Total Revenue: ₹", self.total_revenue)
        avg = self.total_revenue/self.total_days if self.total_days else 0
        print("Average Revenue Per Day: ₹", round(avg))

hotel = Hotel(3,2)

while True:
    print("\n1.Book 2.Checkout 3.Availability 4.Exit")
    ch = input("Choice: ")
    if ch=="1":
        n=input("Name: ")
        t=input("Room (single/double): ").lower()
        try: d=int(input("Days: "))
        except: print("Invalid days."); continue
        hotel.book_room(n,t,d)
    elif ch=="2":
        hotel.checkout(input("Name: "))
    elif ch=="3":
        print("Single:",hotel.single.available,"Double:",hotel.double.available)
    elif ch=="4":
        hotel.report(); break
    else:
        print("Invalid choice.")
        
        """


Test Case 1 – Normal Booking & Checkout
Input:
1
Ravi
single
2
2
Ravi
Expected:
Bill = 2 × 10000 = 20000



Test Case 2 – Multiple Bookings
1
Arjun
double
3

1
Meena
single
1

Expected:
Rooms decrease accordingly.



Test Case 3 – Invalid Room Type
1
Rohit
deluxe
2
Expected:
Room type must be 'single' or 'double'.



Test Case 4 – Checkout Non-Existing Guest
2
Unknown
Expected:
No active booking found.



Test Case 5 – Booking With Zero Days
1
Kiran
single
0
Expected:
Days of stay must be at least 1.

        """