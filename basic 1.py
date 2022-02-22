#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	Write a Python program to print "Hello Python"?
print("Hello Python")


# In[ ]:


#2.	Write a Python program to do arithmetical operations addition and division.?
def su_m(a,b):
    return a+b
def division(a,b):
    return a/b


# In[3]:


#3.	Write a Python program to find the area of a triangle?
def triangle_area(a,b,c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area
triangle_area(3,4,5)


# In[5]:


#4.	Write a Python program to swap two variables?
P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  
   
# To Swap the values of two variables  
P, Q = Q, P  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q) 


# In[4]:


#5.	Write a Python program to generate a random number?
import random
n = random. random()
print(n)


# In[ ]:




