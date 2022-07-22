class Item():

    def __init__(self, name: str, id: int, price: float, store: int, imagePath: str):
        'Construtor do item'

        self.name = name
        if id == None:
            raise Exception("Id can't be none")
        else:
            self.id = id
        if price <=0:
            raise ValueError("Price can't be less than zero")
        self.price = price
        if store < 0:
            raise ValueError("Store can't be less or igual than zero")
        self.store = store
        self.imagePath = imagePath

    def getName(self):
        return self.name

    def getId(self):
        return self.id
    
    def getPrice(self):
        return self.price

    def getAmount(self):
        return self.store

    def getImagePath(self):
        return self.imagePath

    def sell(self, quantity):
        if self.store < quantity:
            raise Exception("Quantity must be less than store")
        self.store = self.store - quantity
        
    def upAmount(self, quantity:int):
        self.store  = self.store + quantity

    def __str__(self):
        return str(self.name) + "  Preço: R$" +str(self.price) + " Quantidade: " +str(self.store) + " Total: R$" + '{:.2f}'.format((self.price * self.store))  
