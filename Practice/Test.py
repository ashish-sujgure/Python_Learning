test=[]
print(type(test))
for i in range(1,100):
    test.append(i)
print(test)


'''
capital_states= ["Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima"]


1. FIND THE LENGHT OF LIST capital_states

2. PRINT BELOW ITEMS USING INDEXING IN THE LIST  capital_states
OUTPUT SHOULD BE : "Imphal"
OUTPUT SHOULD BE : "Kohima"

3. FIND THE LENGHT OF LIST 
z = ['',"","","",""]
z = [None]
'''

capital_states= ["Bhopal","Mumbai","Imphal","Shillong","Aizawl","Kohima"]
print(len(capital_states))


print(capital_states[2])
print(capital_states[5])
print(capital_states[-1])


z = ['',"","","",""]
print(len(z))
z = [None]
print(len(z))


'''
1. PRINT FACTORS OF 5 FROM THE LIST ( OUTPUT SHOULD BE [5,10])

list_num = [1,2,3,4,5,6,7,8,9,10]

2. PRINT LAST THREE ITEMS FROM THE LIST
list_num = [1,2,3,4,5,6,7,8,9,10]

3. PRINT THE ITEMS OF LIST IN REVERSE ORDER 

name_pal = ['M', 'A', 'D', 'A', 'M']

name_d = ['R', 'A', 'K', 'E', 'S', 'H']

4. print 5 from below list
list_z = [1,[2,[3,[4,[5]]]]]

hint: 
print(list_z[1])
print(list_z[1][1])


'''

list_num = [1,2,3,4,5,6,7,8,9,10]

for i in list_num:
    if i%5 == 0:
        print(i)


print(list_num[-3::])

name_pal = ['M', 'A', 'D', 'A', 'M']
name_d = ['R', 'A', 'K', 'E', 'S', 'H']
print(name_pal[::-1])
print(name_d[::-1])


list_z = [1,[2,[3,[4,[5]]]]]
print(list_z[1][1][1][1][0])
list_zz=[1,[2,3,4,[5,6,7]]]
# print(list_zz[1][3][0])

a=[1,2,3,4,5,6,7,8,9]
b=[10,11,12,13,14,15,16,17,18]
c=["Ashish","Nilesh","Shrejith","Pankaj","Abhijit"]
d=["Rakesh","Manoj","Kunal","Chaitanya"]


# len()
print(len(c))
# min()
print(min(a))
# max()
print(max(b))
# append()
a.append(10)
print(a)
# extend()
a.extend(b)
print(a)
# insert()
a.insert(2,12)
print(a)
# index()
print(c.index("Shrejith"))
# pop()
c.pop()
print(c)
# remove()
c.remove("Nilesh")
print(c)
# reverse()
c.reverse()
print(c)

str_a=['A','B','C','D','E','B','B']
str_b=['F','G','H','I','J']

int_a=[1,2,3,4,5,6]
int_b=[7,8,9,10,11,12]

print(int_a+str_a)

print(int_a[0:4])

for i in int_a:
    print(i)

print(len(int_a))
for i in range(1,len(int_a),2):
    print(int_a[i])



# count()
print(str_a.count("B"))
# sort()
str_a.sort()
print(str_a)

# range()

# clear()
str_a.clear()
print(str_a)

print(list())

test_memory=[1,2,3,4,5,6,7]
test_memory2=test_memory
test_memory3=test_memory.copy()

test_memory2.append(8)
print(test_memory)
print(test_memory2)

test_memory3.append(9)
print(test_memory3)
print(test_memory)

print("""
Hey man, how are you?
Long time no see.
Hope you are doing fine
Lets catchup someday
""")

test_fmt="Ashish"
print(list(test_fmt))

z = "Repetition is the mother of learning"
print(type(z))

k  = "Was it a car or a cat I saw? "
p = "Do geese see God?"

print(k[::-1])
print(p[::-1])

h = "HYDERABAD"
c = "CHENNAI"
d = "DELHI"

for i in range(0,len(h),):
    print(h[i], end=' ')
print("\n")
for i in range(0,len(c),):
    print(c[i], end=' ')
print("\n")
for i in range(0,len(d),):
    print(d[i], end=' ')
print("\n")

"moon is nearest and sun is farthest from earth"

"sun is biggest of earth and moon"

"the order is sun , earth and moon"


s = "sun"
m = "moon"
e = "earth"

print("{1} is nearest and {0} is farthest from {2}".format(s,m,e))

print("{0} is biggest of {2} and {1}".format(s,m,e))

print("the order is {} , {} and {}".format(s,e,m))

# upper()
S=s.upper()
print(S)
# lower()
print(S.lower())
# isupper()
print(S.islower())
# islower()
print(S.isupper())
# capitalize()
print(s.capitalize())
# startswith()
print(S.startswith("S"))
# endswith()
print(s.endswith("n"))
# index()
print(s.index("u"))
# replace()
print(s.replace("u","U"))


a="Ashish"
b="180592"
c="Ash180592"
d='Ashish Sujgure'
e=" Ashish Arun Sujgure "

# isalpha()
print(a.isalpha())
# isdigit()
print(b.isnumeric())
# isalnum()
print(c.isalnum())
# isspace()
print(d.isspace())
# istitle()
print(e.istitle())
# strip()
print(e.strip())
print(e)
# split()
print(e.split(" "))


