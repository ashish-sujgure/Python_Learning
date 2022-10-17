#################################################
# HW
#################################################

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
#1. PRINT FACTORS OF 5 FROM THE LIST ( OUTPUT SHOULD BE [5,10])
list_num = [1,2,3,4,5,6,7,8,9,10]
print(list_num[4::5])

#2. PRINT LAST THREE ITEMS FROM THE LIST
list_num = [1,2,3,4,5,6,7,8,9,10]
print(list_num[-3::])

#3. PRINT THE ITEMS OF LIST IN REVERSE ORDER 
name_pal = ['M', 'A', 'D', 'A', 'M']
name_d = ['R', 'A', 'K', 'E', 'S', 'H']

print(name_pal[::-1],name_d[::-1])
#4. print 5 from below list
list_z = [1,[2,[3,[4,[5]]]]]
print(list_z[1][1][1][1])