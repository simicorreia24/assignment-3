#!/usr/bin/env python
# coding: utf-8

# ## Check whether the no. is positive or negative

# In[1]:


a = int(input("Enter a number "))
if a >= 0:
    print("{} is a positive number".format(a))
elif a==0:
    print("The number is zero")
else:
    print("{} is a negative number".format(a))
    


# ## Check if a Number is Odd or Even

# In[4]:


a = int(input("Enter a number "))
if a % 2 == 0:
    print("{} is a Even number".format(a))
else:
    print("{} is a Odd number".format(a))


# ## Check Leap Year

# In[3]:


year=int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{} is a leap year".format(year))
       else:
           print("{} is not a leap year".format(year))
   else:
       print("{} is a leap year".format(year))
else:
   print("{} is not a leap year".format(year))


# ## Check Prime Number

# In[67]:


num = int(input("Enter any number "))
for i in range(2,num):
    if num % i == 0:
        print("The number is not Prime")
        break
else:
    print("The number is Prime")


# ## Print all Prime Numbers in an Interval of 1-10000

# In[64]:


for i in range(1,10001):
    for j in range(2,i):
        if i % j == 0:
            break           
    else:
        print(i,end=" ")


# In[ ]:




