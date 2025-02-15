
import math

vector =[]

print("input the dimensions for x,y,z:  ")

for dimensions in ["x","y","z"]:
    value=(int)(input("insert value: "))
    vector.append(value)

magnitude = math.sqrt(sum(n**2 for n in vector))

print(magnitude)