from objects import Product, Book, Movie

products = (
    Product("iPhone", 160000.0, 1),
    Book("Management", 1200.0, 5, "Srikanth"),
    Movie("Bahubali", 500.0, 0, 2016)
)

print("PRODUCTS")

for product in products:
    print(product)