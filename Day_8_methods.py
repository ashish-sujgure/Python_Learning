'''
Day 8: 
copy()
'''
a=[1,2,3,4,5,6,7,8,9]
b=[10,11,12,13,14,15,16,17,18]
c=["Ashish","Nilesh","Shrejith","Pankaj","Abhijit"]
d=["Rakesh","Manoj","Kunal","Chaitanya"]

#copy()
#returns copy of original list
e=a.copy()
print(e)
e[1]=20
print(e)
print(a)