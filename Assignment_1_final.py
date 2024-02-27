#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task_1:

def fizz_buzz():
    for i in range(1, 101):
        output = ""

        if i % 3 == 0:
            output += f"{i} - Fizz"
        if i % 5 == 0:
            output += f"{i} - Buzz"
        if i % 3 == 0 and i % 5 == 0:
            output = f"{i} - FizzBuzz"

        if output == "":
            output = i

        print(output)

# Call the function
fizz_buzz()


# In[3]:


#Task_2:

name = input("Enter your name: ")

exist = False
for character in name:
    if character.isdigit():
        exist = True
        break
if exist:
    print("Error: User name can't include numeric characters.")
else:
    print("Correct input")

if len(name) > 15:
    print("Error: User name can't exceed 15 characters.")
else:
    print("Correct input")
    
email = input("Enter your email address: ")

if email.find(name) == 0:
    print("Correct input")
else:
    print("Error: Email address must start with user name.")

exist = False
for character in name:
    if character.isupper():
        exist = True
        break
if exist:
    print("Error: All email letters must be in lower case.")
else:
    print("Correct input")

if email.endswith("@ubs.com"):
    print("Correct input")
else:
    print("Error: Email address must end with '@ubs.com'.")

if not "_" in email:
    print("Error: Email address must include underscore.")
else:
    print("Correct input")

if " " in email:
    print  ("Error: Email address must not contain whitespaces.")
else:
    print("Correct input")


# In[4]:


#Task_3:

import math
a = input("Enter first number: ")
aint = int(a)
b = input("Enter second number: ")
bint = int(b)
print(math.gcd(aint,bint))


# In[ ]:




