"""
1.	Write a c ++ program to find the volume and surface area of sphere.
Hint: PI=3.14
volume=4.0/3 *pi*r*r*r;
area=4*pi*r*r;
"""
import math
r  = float(input("Enter the the radius of the sphere: "))
volume = 4.0 * 3 *math.pi * math.pow(r,3)
print("The volume of the sphere is: ", volume)
area = 4 * math.pi *math.pow(r,2)
print("The surface area of the sphere is: ", area)

#3.	What is the output of:
print(3 /2 +5.5)
