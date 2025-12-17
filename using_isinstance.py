from objects import Product, Book, Movie

product1 = Product("iPhone", 160000.0, 1)
product2 = Movie("Bahubali", 500.0, 0, 2016)

print("PRODUCT DATA")

if isinstance(product1, Product):
    print("Product", product1.name)

if isinstance(product1, Movie):
    print("Movie", product2.name)

if isinstance(product2, Movie):
    print("Year", product2.year)