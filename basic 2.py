#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	Write a Python program to convert kilometers to miles?
def kilo_to_mile(a):
    b = a*0.621371
    return b
kilo_to_mile(3)


# In[3]:


#2.	Write a Python program to convert Celsius to Fahrenheit?
def cel_to_fah(a):
    b = (a*1.8)+32
    return b
cel_to_fah(3)


# In[5]:


#3.	Write a Python program to display calendar?
import calendar
# Enter the month and year.
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
# display the calendar.
print(calendar. month(yy,mm))


# In[6]:


#4.	Write a Python program to solve quadratic equation?
# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# In[7]:


#5.	Write a Python program to swap two variables without temp variable?
x = 5
y = 7
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


# In[ ]:




