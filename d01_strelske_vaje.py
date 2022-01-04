import math

g = 9.807
v = input("hitrost = ")
f = input("kot = ")

f = math.radians(int(f))

s = (pow(int(v), 2) * math.sin(2*f))/g

print(s)