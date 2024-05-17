class Employee: 
    no_of_employees = 0
    raise_amount = 1.4

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        Employee.no_of_employees += 1
    
    def fullname(self):
        return self.first + self.last
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_amount
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = 1.5
    
    @classmethod
    # sometimes used as a constructors, here we are using it to create a objects of employee type.
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    
    #static methods
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 
    
    @property
    def email(self):
        return '{} {}@company.com'.format(self.first, self.last)
    
    @property 
    def fullname(self):
           return '{} {}'.format(self.first, self.last)
    
    #setters
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last 

        

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print(emp.first)






emp_1 = Employee("arun", "giri", 10000)
emp_2 = Employee("aayush", "bhatta", 5000)

print(emp_1.email)
emp_1.fullname = "ashish giri"
print(emp_1.first)

dev1 = Developer("subrat", "pandey", 20000, "python")
print(dev1.email)
print(dev1.prog_lang)

mng1 = Manager("ajay", "pokhrel", 8000, [dev1])
mng1.print_emps()


