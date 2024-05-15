import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% of discount.
    all = []

    def __init__(self, name:str, price:float, quantity=0):
        #run validations to the received arguments.
        assert price >= 0, f"price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)
    
    def calcualte_total_price(self):
        return self.__price * self.quantity
    
    def apply_discount(self):
        self.__price = self.__price * (self.pay_rate)
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        # print(items)
        for item in items:
            # print(item['name'])
          Item(
          item.get('name'),
          float(item.get('price')),
          float(item.get('quantity'))
          )
    
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero.
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


    
    def __repr__(self):
        return f"Item('{self.__name}',{self.__price}, {self.quantity} )"
    
    # setters and getters.

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            raise ValueError("Price must be greater than or equal to zero")
    





