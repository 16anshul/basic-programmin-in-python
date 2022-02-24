#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.	Write a Python Program to Find the Factorial of a Number?
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)
fact(5)
        


# In[7]:


#2.	Write a Python Program to Display the multiplication Table?
number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
count = 1    
# we are using while loop for iterating the multiplication 10 times      
print ("The Multiplication Table of: ", number)    
while count <= 10:    
    number = number *1   
    print (number, 'x', count, '=', number * count)    
    count += 1    


# In[17]:


#3.	Write a Python Program to Print the Fibonacci sequence?
fib_array = [0,1]
def fibonacci(n):
    if n < 0:
        return "Incoorect input"
    elif n == 0:
        return 0
    elif n ==1 or n == 2:
        return 1
    else:
        fib_series = fibonacci(n-1) + fibonacci(n-2)
        fib_array.append(fib_series)
        return fib_series
fibonacci(9)
print(fib_array)


# In[24]:


#4.	Write a Python Program to Check Armstrong Number?
def Armstrong(n,o):
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** o
        temp = temp//10
    if n == sum:
        print(n,"is an Armstrong number")
    else:
        print(n,"is not an Armstrong number")
    
num = int(input("Enter Number: "))
order = len(str(num))
Armstrong(num,order)


# In[32]:


#5.	Write a Python Program to Find Armstrong Number in an Interval?
#1*1 + 6*6 = 37   so it is not an Armstrong Number.
x=int(input("lower limit: "))
y=int(input("upper limit: "))
print("Armstrong Numbers are: ")
for Number in range(x,y):
    digits=0
    temp = Number
    while temp > 0: # no of digits
        digits = digits+1
        temp = temp//10
        sum = 0
    temp =  Number
    while temp > 0: # calculate armstrong number
        last_digit = temp % 10
        sum = sum +(last_digit**digits)
        temp = temp//10
        if Number == sum:
            print(Number)


# In[2]:


#6.	Write a Python Program to Find the Sum of Natural Numbers?
n = int(input())
if n <0:
    print("Enter a Natural Number")
elif n == 0:
    print("0")
else:
    sumn = 0 
    while n > 0:
        sumn += n
        n -= 1
    print(sumn)
        


# In[ ]:




