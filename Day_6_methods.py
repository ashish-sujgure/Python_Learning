'''
Day 6
count()
sort()
'''

a=[1,1,1,2,3,4,5,6,7,8,9]
b=[10,11,12,13,14,15,16,17,18]
c=["Ashish","Nilesh","Shrejith","shrejith","Shrejith","Shrejith","Shrejith","Pankaj","Abhijit"]
d=["Rakesh","Manoj","Kunal","Chaitanya"]

#count()
#returns number of given occurence in list.
# it is case sensitive
e=a.count(1)
print(e)
print(c.count('Shrejith'))

#sort()
#returs none, updates the original list with assending format
#DOES NOT WORK WITH INT AND CHAR MIX LIST
a.sort()
print(a)
c.sort()
print(c)

#a.extend(c)
#print(a)
#print(a.sort())



