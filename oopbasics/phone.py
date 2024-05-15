from item import Item

class Phone(Item):
    all = []
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
        # call to super function to have access to all attributes/methods.

        super().__init__(
            name, price, quantity
        )

        assert broken_phones  >= 0, f"broken_phones  {broken_phones } is not greater or equal to zero"

        #ASSIGN TO SELF OBJECT
        self.broken_phones = broken_phones

phone1 = Phone("iphone", 500, 5, 1)
# print("from child class")
# print(phone1.calcualte_total_price())