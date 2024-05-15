class Person:
    count = 0
    def __init__(self):
       Person.count += 1

p1 = Person()
p2 = Person()

print(Person.count)