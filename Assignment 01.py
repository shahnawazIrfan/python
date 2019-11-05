# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:03:25 2019

@author: Shahnawaz Irfan
"""
import sys
import datetime
from math import pi


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

print("Python version")
print (sys.version)


now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


radius = float(input ("Enter radius  : "))
print ("The area of the circle with radius " + str(radius) + " is: " + str(pi * radius**2))


fname = input("Entert your First Name : ")
lname = input("Enter your Last Name : ")
print (lname + " " + fname)


x = input('Enter first number: ')
y = input('Enter second number: ')
sum = int(x) + int(y)
print(sum)