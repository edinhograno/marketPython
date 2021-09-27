from product import Product
from list import List

avocato = Product("Avocato", 2, 4, 3.40, "I like to eat avocado with milk.")
pineapple = Product("Pineapple", 4, 2, 1.29,
                    "My mother hates pineapple juice.")
banana = Product("Banana", 3, 2, 5.16, "Banana avoids muscle cramps.")

list = List()
list.append(avocato)
list.append(pineapple)
list.append(banana)
list.print()
