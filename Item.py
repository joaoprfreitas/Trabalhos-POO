class Item():
    def __init__(self, name: str, id: int, price:float, store=0):
        self.name = name
        if id == None:
            raise Exception("Id can't be none")
        else:
            self.id = id
        if price <=0:
            raise ValueError("Price can't be less than zero")
        else:
            self.price = price
        self.store = store
    
    def sell(self, quantity):
        if self.store < quantity:
            raise Exception("Quantity must be less than store")
        self.store = self.store - quantity
