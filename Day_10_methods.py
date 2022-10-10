'''
Day 10:
upper()
lower()
isupper()
islower()
capitalize()
startswith()
endswith()
index()
replace()
'''

a=[1,2,3,4,5,6,7,8,9]
b=[10,11,12,13,14,15,16,17,18]
c=["Ashish","Nilesh","Shrejith","shrejith","Shrejith","Shrejith","Shrejith","Pankaj","Abhijit"]
d=["Rakesh","Manoj","Kunal","Chaitanya"]
e="ashish"
g="ASHISH"
h="I Love Nashik"
f=e.upper()
print(f)

f=e.lower()
print(f)

f=e.capitalize()
print(f)

print(e.islower())

print(g.isupper())

print(e.startswith("A"))

print(g.endswith("H"))

print(g.index("H"))

print(h)

print(h.replace('Nashik','Pune'))