#################################################
# HW
#################################################

'''
1 . UNPACK THE TUPLE AND PRINT 0 AFTER UNPACKING IT

z = ([22,33], [True,False],[0,1],[111,999])


# 2. UNPACK THE TUPLE AND PRINT 9 AFTER UNPACKING IT 
# t_num = (1,2,3,4,5,6,7,8,9)
#     ,,c,,,,,, = t_even

3. 
convert the list into sets:
name1 = ['R', 'A', 'H', 'U', 'L']
name2 = ['A', 'K', 'S', 'H', 'A', 'Y']
bool3 = [True, False, False, False, True]

4. find length of the set
    use for loop to print the items of  the set

d = set([True, False, False, False, True])

'''

# 👆 share the output screenshot 📷

print("************Q1************")
z = ([22,33], [True,False],[0,1],[111,999])
z1=list(z)
z1.append(0)
print(z1)
z=tuple(z1)
print(z)

print("************Q2************")
t_num = (1,2,3,4,5,6,7,8,9)
a,b,c,d,e,f,g,h,i=t_num
print(i)

print("************Q3************")
name1 = ['R', 'A', 'H', 'U', 'L']
name2 = ['A', 'K', 'S', 'H', 'A', 'Y']
bool3 = [True, False, False, False, True]
print(set(name1))
print(set(name2))
print(set(bool3))

print("************Q4************")
d = set([True, False, False, False, True])
print(d)
print(len(d))
for i in d:
    print(i)