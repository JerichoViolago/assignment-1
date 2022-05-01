#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Assignment 1
This assignment covers your basic profiency with
    Python. It engages your ability to transform
    data without affecting anything outside the program.
This assignment places heavy emphasis on basic Python constructs.
'''

def factorial(x):
    '''Item 1. 
    Factorial. 1 point.
    
    Returns the factorial of an integer.
    An integer's factorial is the product of the integer and all
        integers below it.
    Parameters
    ----------
    x: int
        the integer whose factorial to return
    Returns
    -------
    integer
        the factorial of the argument
    '''
    # Write your code below this line


# In[10]:


x = int(input('Enter Your Number Here: '))
factorial=1
if x>0:
    for i in range (1, x + 1):
        factorial = factorial*i
    print ("Factorial of", x , "is", factorial)
elif x==0:
    print ("Factorial of 0 is 1")
else:
    print ("There are no factorials for negative numbers")


# In[11]:


def classify_grade(number_grade):
    '''Item 2.
    Classify Grade. 2 points.
    
    Returns the letter grade equivalent of a number grade.
    For this item, use these letter grade buckets:
        A: 92-100
        B+: 86-91.9
        B: 80-85.9
        C+: 74-79.9
        C: 67-73.9
        D: 60-66.9
        F: 0-59.9
    Parameters
    ----------
    number_grade: float
        the number grade to convert into a letter grade.
    Returns
    -------
    str
        the letter grade equivalent of the number grade.
    '''
    # Write your code below this line


# In[2]:


grade = float(input("Enter Score Grade Here:"))


if grade >=92 and grade <=100:
    print ("A")
elif grade >= 86 and grade<= 91.9:
    print ("B+")
elif grade >= 80 and grade <= 85.9:
    print ("B")
elif grade >= 74 and grade <= 79.9:
    print ("C+")
elif grade >= 67 and grade <= 73.9:
    print ("C")
elif grade >= 60 and grade <= 66.9:
    print ("D")
elif grade >= 0 and grade <= 59.9:
    print ("F")


# In[28]:


def average_weight(item_quantity_1, item_weight_1, item_quantity_2, item_weight_2):
    '''Item 3.
    Average Weight. 3 points.
    
    You have purchased two bags of items. 
    The first bag contains one type of item, and the second bag contains another type.
    Return the weighted average weight of the items.
        
    Parameters
    ----------
    item_quantity_1: int
        the quantity of items in the first bag.
    item_weight_1: float
        the weight of each individual item in the first bag.
    item_quantity_2: int
        the quantity of items in the second bag.
    item_weight_2: float
        the weight of each individual item in the second bag.
    Returns
    -------
    float
        the weighted average weight of one item.
    '''
    # Write your code below this line


# In[15]:


item_quantity_1 = int(input("enter item 1 quantity here: "))
item_weight_1 = float(input("enter item 1 weight here: "))
item_quantity_2 = int(input("enter item 2 quantity here: "))
item_weight_2 = float(input("enter item 2 weight here: "))

avg= ((item_quantity_1 * item_weight_1) + (item_quantity_2 * item_weight_2))/ (item_quantity_1 + item_quantity_2)

print(avg)


# In[ ]:




