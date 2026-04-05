# create a class laptop with attributes : brand,ram,price.create 2 objects 
# with different values.

class laptop:
    brand="default"
    ram="default 8GB"
    price="default 1 lakh"

laptop1= laptop()
laptop1.brand="asus"
laptop1.ram="16"
print("Laptop 1 brand == ",laptop1.brand)
laptop2=laptop()
laptop2.brand="lenovo"
laptop2.ram="32"
print("Laptop 2 brand ==",laptop2.brand)


