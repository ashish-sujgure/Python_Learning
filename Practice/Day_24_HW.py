'''
1. CREATE A DICT BY USING TWO LISTS WITH zip() FUNCTION

list_keys = ['A', 'E', 'I', 'O', 'U']
list_values = ['0', '1', '2', '3', '4', '5']

2 . CREATE A DICT USING tuples

x = (1 , True)
y = (2 , False)
z = (3 , False)
p = (4 , False)

3 . ADD  THE KEY : VALUE PAIR  {5 : True} IN ABOVE DICTIONARY AND PRINT 

4 . UPDATE THE VALUE OF   KEY 3 IN DICTIONARY AS  True USING .update()


5 . RETRIEVE THE VALUE CORRESPONDING TO KEY y IN ABOVE DICT
USING []
USING .get()

'''
print("*****************Q1******************")
list_keys = ['A', 'E', 'I', 'O', 'U']
list_values = ['0', '1', '2', '3', '4', '5']

print(dict(zip(list_keys, list_values)))

print("*****************Q2******************")
x = (1 , True)
y = (2 , False)
z = (3 , False)
p = (4 , False)

list_dict=dict([x,y,z,p])
print(list_dict)

print("*****************Q3******************")
list_dict.update({5 : True})
print(list_dict)

print("*****************Q4******************")
list_dict.update({3:True})
print(list_dict)

print("*****************Q5******************")
print(list_dict[y[0]])
print(list_dict.get(y[0]))