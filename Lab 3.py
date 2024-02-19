# Date: 5th Feb,2024
# Time: 15:00 hrs
# Prakhar Punj
# 220150011
# Data Science and AI
# Lab 3

#Question 1
print("\n   Question 1   ")   # To print an empty line for new Question
print("Printing numbers from 1 to 55")
for val in range(1,56):
    print(val)
    
    
    
#Question 2
# To print an empty line for new Question 
print("\n   Question 2  ")   
# Creating a list from 1 to 1000(inclusive) 
print("The list of numbers frm 1 to 1000 is:")
list_1000 =[value for value in range(1,1001)] 
for val in list_1000:
    print(val)
    
    
    
#Question 3 
# To print an empty line for new Question
print("\n   Question 3  ")   
# Creating another list from 1 to 1000(inclusive) 
list_1000_1 =[value1 for value1 in range(1,1001)] 
# Printing only the Minimum value of the list 
print(f"The minimum value in the list of Question 3 is:"+str(min(list_1000_1)))
# Printing only the Maximum value of the list 
print(f"The maximum value in the list of Question 3 is:"+str(max(list_1000_1)))



#Question 4
print("\n   Question 4   ")
sum_list_1000=sum(list_1000_1)
print(f"The sum of all the 1000 values is:"+str(sum_list_1000))



#Question 5
print("\n   Question 5")
list_odd=[odd_val for odd_val in range(1,56,2)]
print("The List of Odd Numbers from 1 to 55 is:")
for odd_v in list_odd:
    print(odd_v)
    
    
    

#Question 6
print("\n   Question 6")
list_3=[multiple for multiple in range(3,301,3)]
print("The multiples of 3 from 3 to 300 are:")
for multiple_3 in list_3:
    print(multiple_3)
    
    
    
#Question 7
print("\n   Question 7")
list_cube=[num**3 for num in range(1,101,1)]
print("The cube of numbers from 1 to 100 are:")
for cube_3 in list_cube:
    print(cube_3) 
    


#Question 8 
print("\n   Question 8")
cubes = [i**3 for i in range(1,101)]
print("The Generated list is:")
print(cubes)




#Question 9
print("\n    Question 9")
print("The Even numbers from 1 to 55 are:")
for j in range(2,55,2):
    print(j)
    
    
    
#Question 10
print("\n    Question 10")    
squares=[k**2 for k in range(1,21,1)]
print("The Squared numbers are:")
for p in squares:
    print(p)


 