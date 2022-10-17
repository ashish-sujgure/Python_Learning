print('Hello World!')
#used to print
import keyword
#used to import modules
print('=================')
print('List of keywords')
print('=================')
print(keyword.kwlist)
#used to print keword list from keyword module

v=10
w=10.123
x="Ashish"
y="Sujgure"
z=True


print(v)
print(type(v))
print(w)
print(type(w))
print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

#comparison operator <, >, <=, >=, !=, ==
print('=================')
print('Comparison operator test')
print('=================')
print(v > w)

print(w > v)

print(w == v)

print(w!=v)

print(w<=v)

print(w>=v)

#logical operators and / or / not

'''
and

True True = True
False True = False
True False = False
False False = False

or

True True = True
True False = True
False True = True
False False = False

not

True = False
False = True
'''
print('=================')
print('AND test')
print('=================')
print(1 >= 1 and 2 == 2)
print(1 >= 1 and 2 != 2)
print(1 > 1 and 2 == 2)
print(1 > 1 and 2 != 2)
print('=================')
print('OR test')
print('=================')
print(1 >= 1 or 2 == 2)
print(1 >= 1 or 2 != 2)
print(1 > 1 or 2 == 2)
print(1 > 1 or 2 != 2)
print('=================')
print('NOT test')
print('=================')
print(not True)
print(not False)
