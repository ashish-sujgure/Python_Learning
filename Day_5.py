#List manipulation

from turtle import st


str_a=['A','B','C','D','E']
str_b=['F','G','H','I','J']

int_a=[1,2,3,4,5,6]
int_b=[7,8,9,10,11,12]

#Concatination

print(str_a+str_b)
print(int_a+int_b)

# Concatination combines two list into one single list.

#Substract - This is not supported operand in Python

#Divide - THis is not supported operand in Python

#Multiplication

print(str_a*2) # Doing this the list will be printed twice
#print(str_a*str_b) # This won't work. multiplication cannot multiply 2 lists.
print(int_a*2) # Doing this the list will be print twice.
#print(int_a*int_b) # This won't work. multiplication cannot multiply 2 lists.


#Slicing
print(type(str_a))
print("Length is :", len(str_a))
print("Index is :", len(str_a)-1)
print(str_a[1]) # To print specific int or str.
print(str_a[-1]) # To print specific int or str using negative indexing.
print(str_a[0:5:]) # To print int or str from start ponint to end point -1.
print(str_a[0:5:2]) # To print in hop of 2
print(str_a[::-1]) # To print in reverse order

#Loop using regular method
for i in str_a:
    print(i)

#Loop using range function
for i in range(0,5):
    print(i) # should print the count of range specified.
    print(str_a[i]) # should print the str/int in vertical format.

for i in range(0,5,2):
#    print(i)
    print(str_a[i]) # should print in hop of 2

