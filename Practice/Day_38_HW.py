
# 1. catch exception in below code using try... except 
# else print "Code Execution was successful"
print("************Q1.************")

try: 
    list_z = [1,2,3,"a"]
    for i in range(5):
        if type(list_z[i]) == int:
            print("This is int")
        else:
            print("This is not int")
except IndexError as e:
    print("List index out of range" , e)
else:
    print("Code Execution was successful")


# 2. catch exception in below code using try... except
# else print " Code Execution was successful"
print("************Q2.Part1************")
try:
    f = open(r"C:\Users\ashis\Python_Learning\Practice\one.txt")
    print(f.read())
except FileNotFoundError as e:
    print("ERROR!", e)
else:
    print("Code Execution was successful")
finally:
    f.close()

print("************Q2.Part2************")

try:
    f = open(r"one.txt")
    print(f.read())
except FileNotFoundError as e:
    print("ERROR!", e)
else:
    print("Code Execution was successful")
finally:
    f.close()