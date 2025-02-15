import random

temper=random.randint(1,400)
print("The Temperature is:  ",temper,"degrees")

if temper>100:
    print("Temperature is above boiling point")
    
    if temper>320:
          print("Temperature is above smoke point")  
else:
    print("Temperature is not very high")