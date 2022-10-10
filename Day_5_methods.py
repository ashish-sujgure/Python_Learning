
'''
Day 5: 

len()
min()
max()
append()
extend()
insert()
index()
pop()
remove()
reverse()
'''


a=[1,2,3,4,5,6,7,8,9]
b=[10,11,12,13,14,15,16,17,18]
c=["Ashish","Nilesh","Shrejith","Pankaj","Abhijit"]
d=["Rakesh","Manoj","Kunal","Chaitanya"]

#len()
#Retursn lenght on list
print(len(c))
print(len(c[0]))
print(len(a))

#min()
#Returns minimum number

print(min(a))
print(min(c)) #If applied on string/char it compaires the ASCII

#max()
#Returns maximum number

print(max(a))
print(max(c)) #If applied on string/char it compaires the ASCII

#append()
#Returns none, update original list
a.append(10)
print(a)

#extend
#Returns none, extends original list

a.extend(b) # Will extend list a with elements in list b
print(a)

c.extend(d)
print(c)

#insert
#returns none, updates original list
print(a.insert(1,50)) # Will insert 50 to index 1 of a
print(a)

c.insert(2,['tom,dick,herry']) # Will insert complete list in index 2 of c
#eg.: ['Ashish', 'Nilesh', ['tom,dick,herry'], 'Shrejith', 'Pankaj', 'Abhijit', 'Rakesh', 'Manoj', 'Kunal', 'Chaitanya']
print(c)
print((c[2]))

#index
#returns index of element
e=c.index('Ashish')
#e=c.index('[tom,dick,herry]') #Does not work with list inside list
print(e)

#pop()
#returns element which will be removed, updates the actual list
# by default removed last element if no index passed

e=c.pop(2)
print(e) # returns element by index value, which will be removed
print(c) # updated list.

#remove
#returns none, removed element by element name.
a.remove(50)
a.remove(10)
print(a)

#reverse
#returns none, update original list in reverse format
a.reverse()
print(a)
a.reverse()
print(a)