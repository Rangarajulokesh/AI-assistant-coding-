# create a stident class and it must take inputs such as name , age , roll no . all the details must be displayed using the display details method
#Task 1 
class Student:
    def __init__(self, name: str, age, roll_no: str):
        self.name = str(name).strip()
        try:
            self.age = int(age)
        except (TypeError, ValueError):
            raise ValueError("age must be an integer")
        self.roll_no = str(roll_no).strip()

    def display_details(self):
        print("Student Details")
        print("----------------")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Roll No.: {self.roll_no}")
if __name__ == "__main__":
    name = input("Enter name: ")
    age = input("Enter age: ")
    roll_no = input("Enter roll no.: ")

    try:
        s = Student(name, age, roll_no)
        s.display_details()
    except ValueError as e:
        print(f"Error: {e}")
#a simple program which takes an input as a number and displays it's first 10 multiples
# TASK 2 
        def print_first_10_multiples(value):
            try:
                n = int(value)
            except (TypeError, ValueError):
                raise ValueError("Please enter a valid integer.")
            for i in range(1, 11):
                print(f"{n} x {i} = {n * i}")

        if __name__ == "__main__":
            try:
                num = input("Enter a number to show its first 10 multiples: ")
                print_first_10_multiples(num)
            except ValueError as e:
                print(f"Error: {e}")
                #generate a age classification function child, teenager, adult, senior use if,else-if,else
                #TASK 3
                def classify_age(age):
                    """Return age category: child, teenager, adult, or senior."""
                    try:
                        n = int(age)
                    except (TypeError, ValueError):
                        raise ValueError("age must be an integer")
                    if n < 0:
                        raise ValueError("age cannot be negative")
                    if n <= 12:
                        return "child"
                    elif n <= 19:
                        return "teenager"
                    elif n <= 64:
                        return "adult"
                    else:
                        return "senior"


                if __name__ == "__main__":
                    try:
                        age_input = input("Enter age to classify: ")
                        print(f"Classification: {classify_age(age_input)}")
                    except ValueError as e:
                        print(f"Error: {e}")