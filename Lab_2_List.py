# Created on 29th January, 2024
# By Prakhar Punj
# DSAI
# 220150011


names = ["First Name 1", "Second Name 2", "Third Name 3", "Fourth Name 4"]
print(names)
# print("The length of string define in the above command is: ",len(names)) 
len_n= len(names)
len_n= str(len_n)
print("The length of list defined in the above command:"+len_n)

#Accessing elements in a list
print(names[0])
print(names[3])
print(names[-1])
print(names[-2])
print(names[2])
#  str.title() returns the whole string with first alphabet of each word in Upper Case
print(names[-1].title())

temp_first= names[0]
temp_last= names[-1]
# print("The first element is ",temp_first,"\nThe last element is ",temp_last)
print(f"The first element is {temp_first}\nThe last element is {temp_last}")

# Modifying elemnts in the list
names[1]= "Modified name 2"
print(names)

#Adding elements in a list
names.append('Fifth Name 5')
print(names)

#Adding elements at a specific location
names.insert(1,"Adding first name")
print(names)

del names[1]
print(names)

temp_name_del = names.pop(1)
del names[1]

print (names)

i=0
for name in names:
    print(i)
    print(name)
    i=i+1

print('The code is now completed....')



#list of numerical values
roll_digits = [0,1,2,3,4,5,6,7,8,9]
roll_digits_func= list(range(0,10))

for value in range(0,101):
    print(value)

for value in roll_digits_func[3:6]:
    print(value)
    
for value in 