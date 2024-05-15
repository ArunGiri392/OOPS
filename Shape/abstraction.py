from abc import ABC, abstractmethod

# Define an abstract class representing a Person interface
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def print_name(self):
        pass

    @abstractmethod
    def print_age(self):
        pass

# Implement the Person interface in the Employee class
class Employee(Person):
    def print_name(self):
        print(f"Employee Name: {self.name}")

    def print_age(self):
        print(f"Employee Age: {self.age}")

# Implement the Person interface in the Customer class
class Customer(Person):
    def print_name(self):
        print(f"Customer Name: {self.name}")

    def print_age(self):
        print(f"Customer Age: {self.age}")

# Create instances of Employee and Customer
employee = Employee(name="John", age=30)
customer = Customer(name="Alice", age=25)

# Use the interface methods
employee.print_name()  # Output: Employee Name: John
employee.print_age()   # Output: Employee Age: 30

customer.print_name()  # Output: Customer Name: Alice
customer.print_age()   # Output: Customer Age: 25
