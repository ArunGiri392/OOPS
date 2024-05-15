from item import Item
from phone import Phone

# using a class method to instantiate a objects.
Item.instantiate_from_csv()
# print(Item.all)

item1 = Item("tiger", 600, 5)
print(item1.price)

item1.price = 1000
print(item1.price)