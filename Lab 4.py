# Created on 12th Feb, 2024
# Time: 3pm
# Program by
# Prakhar Punj
# 220150011
# Data Science and AI



#Question 1
print("\n   Question 1")
msg=input("Enter your message: ")
a_msg=""
for ch in msg:
    if(ch.islower()==True):
        a_msg=a_msg+ch.upper()
    elif(ch.isupper()==True):
        a_msg=a_msg+ch.lower()
    else:
        a_msg=a_msg+ch
print(f"Altered Message: {a_msg}")



#Question 2
print("\n   Question 2")
str=input("Enter your string:")
count=0
vow=["a","e","i","o","u"]
for i in str:
    if(i.lower() in vow):
        count=count+1
print(f"The number of vowels={count}")        



#Question 3
print("\n   Question 3")
str2=input("Enter your string:")
rev_string=str2[::-1]
print(f"Reversed String: {rev_string}")     #Slicing statement



#Question 4
print("\n   Question 4")
tup=("Pineapple", "Mango", "Apple","Banana", "Kiwi", "Orange")
print(f"Length of the tuple= {len(tup)}")   #To print the length of the Tuple
print(f"The First Element of the Tuple: {tup[0]} & The Last element of the Tuple= {tup[-1]}")
print(f"The Elements from 2nd to 4th are:{tup[1:4]}")
tup[0]="Papaya"     #Trying to Change the 1st element of the tuple

# When we try to change the tuple value, we get the following error statement:
#The Error we get is: tup[0]="Papaya"
#     ~~~^^^
# TypeError: 'tuple' object does not support item assignment
# The Error statement means that we cannot modify a Tuple Element



#Question 5
print("\n   Question 5")
tup_a=(5,4,3,67,331)
tup_b=(19,420,999,771,41,-3)
tup_c=tup_a+tup_b
print(f"The First Tuple:{tup_a}")
print(f"The Second Tuple:{tup_b}")
print(f"The concatenated Tuple is:{tup_c}")
print(f"The Maximum value in the Tuple is: {max(tup_c)} & The Minimum value in the Tuple is:{min(tup_c)}")
print(f"The sum of all the elements is:{sum(tup_c)}")
