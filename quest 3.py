from decimal import Decimal

def generator():
   x = 2.0
   while x <= 5.5:
       print(Decimal(x))
       x = x + 0.5

generator()