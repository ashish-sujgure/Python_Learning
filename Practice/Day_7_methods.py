'''
Day 7: 
range()
clear()
'''

a=[1,2,3,4,5,6,7,8,9]
b=[10,11,12,13,14,15,16,17,18]
c=["Ashish","Nilesh","Shrejith","shrejith","Shrejith","Shrejith","Shrejith","Pankaj","Abhijit"]
d=["Rakesh","Manoj","Kunal","Chaitanya"]

#range()
#example using for loop
for i in range(0,9,1): # range(START,END - 1,jump)
    print(i)
    print(c[i])

for i in range(1,9,2):
    print(a[i])
#example using list
e=list(range(16,161,16)) # Print table of 16, SHOUD BE USED WITH DATA TYPE
print(e)

print(list(range(200,0,-1))) # Print in reverse order.


#clear()
#returns none, empties the original list
print(e.clear())
print(e)
