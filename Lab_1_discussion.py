# Created on 29th January, 2024
# Assignment 1 discussion
# By Prakhar Punj
# DSAI
# 220150011



#Question 1
first_name= "Prakhar"
last_name="Punj"
roll_number="220150011"
introduction=f"My name is {first_name} {last_name} and Roll number is {roll_number}"
print(introduction)



#Question 2
in_values= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

out_values=[2, 4, 5, 4, 5, 8, 10, 9, 11, 14]

s_in = in_values[0] + in_values[1] + in_values[2] + in_values[3] + in_values[4] + in_values[5]+ in_values[6] + in_values[7]+ in_values[8] + in_values[9]

m_in= s_in/10 
# 9 ~ -1 = in_values[9]=in_values[-1]

s_out= out_values[0] + out_values[1] + out_values[2] + out_values[3] + out_values[4] + out_values[5] + out_values[6] + out_values[7] + out_values[8] + out_values[9]

m_out=s_out/10

s_inout=  (in_values[0] * out_values[0]) + (in_values[1] * out_values[1]) + (in_values[2] * out_values[2]) + (in_values[3] * out_values[3]) + (in_values[4] * out_values[4]) + (in_values[5] * out_values[5]) + (in_values[6] * out_values[6]) + (in_values[7] * out_values[7]) + (in_values[8] * out_values[8]) + (in_values[9] * out_values[9])

s_insq= (in_values[0] * in_values[0]) + (in_values[1] * in_values[1]) + (in_values[2] * in_values[2]) + (in_values[3] * in_values[3]) + (in_values[4] * in_values[4]) + (in_values[5] * in_values[5]) + (in_values[6] * in_values[6]) + (in_values[7] * in_values[7]) + (in_values[8] * in_values[8]) + (in_values[9] * in_values[9])

sh = (10 * s_inout - s_in * s_out) / (10 * s_insq - s_in * s_in)
ts=m_out - sh * m_in

print("sh:", sh)
print("ts:", ts)



#Question 3
# the program calculates sh andts using given input array
# sh is the slope of the linear regression line



#Question 4
#Python Program with modified input values based on roll number

#Defining modified iput and output array
roll_digits= [2,2,0,1,5,0,0,1,1]
out_values_mod=[roll_digits[0]**2, roll_digits[1]**2, roll_digits[2]**2, roll_digits[3]**2, roll_digits[4]**2, roll_digits[5]**2, roll_digits[6]**2, roll_digits[7]**2, roll_digits[8]**2]

s_in_mod= roll_digits[0] + roll_digits[1] + roll_digits[2] + roll_digits[3] + roll_digits[4] + roll_digits[5] + roll_digits[6] + roll_digits[7] + roll_digits[8] 

m_in_mod= s_in_mod/9

s_out_mod= out_values_mod[0] + out_values_mod[1] + out_values_mod[2] + out_values_mod[3] + out_values_mod[4] + out_values_mod[5] + out_values_mod[6] + out_values_mod[7] + out_values_mod[8] 

m_out_mod= s_out_mod/9

#Calculate required sums without using sum()
s_inout_mod= (
    roll_digits[0] * out_values_mod[0] + roll_digits[1] * out_values_mod[1] + roll_digits[2] * out_values_mod[2] + roll_digits[3] * out_values_mod[3] + roll_digits[4] * out_values_mod[4] + roll_digits[5] * out_values_mod[5] + roll_digits[6] * out_values_mod[6] + roll_digits[7] * out_values_mod[7] + roll_digits[8] * out_values_mod[8])

s_insq_mod=  (
    roll_digits[0] * roll_digits[0] + roll_digits[1] * roll_digits[1] + roll_digits[2] * roll_digits[2] + roll_digits[3] * roll_digits[3] + roll_digits[4] * roll_digits[4] + roll_digits[5] * roll_digits[5] + roll_digits[6] * roll_digits[6] + roll_digits[7] * roll_digits[7] + roll_digits[8] * roll_digits[8])

#calculate modified sh and ts
sh_mod= (10 * s_inout_mod -s_in_mod * s_out_mod)/ (10* s_insq_mod - s_in_mod * s_in_mod)

ts_mod= m_out_mod - sh_mod * m_in_mod

print("Modified sh:", sh_mod)
print("Modified ts:", ts_mod)