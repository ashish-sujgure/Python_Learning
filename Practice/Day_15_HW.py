#################################################
# HW
#################################################

t = (False,False,True,False,True)

'''
#1. CONVERT THE ABOVE  TUPLE INTO A LIST
#2. FIND THE MEMORY ADDRESS OF BOTH TUPLE AND LIST
#3. APPEND 99 AT THE END OF THE LIST
#4. CONVERT BACK THE LIST  INTO TUPLE
#5. NOW FIND THE MEMORY ADDRESS OF THIS TUPLE
'''
# 👆 share the output screenshot 📷

print(t)
print(type(t))
t2=(list(t))
print(t2)
print(type(t2))


print(id(t))
print(id(t2))

t2.append(99)
print(t2)


t2=tuple(t2)
print(t2)
print(type(t2))

print(id(t2))



listName = ["Ashish", "Sheejit", "Nilesh", "Sachin", "Abhijit"]
y=1
for i in range(len(listName)):
    x=listName[i]
    #print((i),".", (listName[i]))
    print(f'{y} {x}')
    y=y+1