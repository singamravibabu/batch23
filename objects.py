class Product:
    def __init__(self, name="", price=0.0, discountPercent=0):
        self.name = name
        self.price = price
        self.discountPercent = discountPercent
    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100
    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()
    def __str__(self):
        return self.name + " | " + str(self.price) + " | " + str(self.discountPercent)
    
    
class Book(Product):
    def __init__(self, name="", price=0.0, discountPercent=0, author=""):
        # call the constructor of the superclass
        Product.__init__(self, name, price, discountPercent)
        # set the author
        self.author = author
        # override the getDescription method
    def __str__(self):
        return self.name + " | " + str(self.price) + " | " + str(self.discountPercent)

        
class Movie(Product):
    def __init__(self, name="", price=0.0, discountPercent=0, year=1900):
        # call the constructor of the superclass
        Product.__init__(self, name, price, discountPercent)
        # set the year
        self.year = year
        # override the getDescription() method
    def __str__(self):
        return self.name + " | " + str(self.price) + " | " + str(self.discountPercent)
