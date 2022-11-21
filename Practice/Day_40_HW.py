#################################################
# HW
#################################################


'''
1. create a class Vehicle with below attributes/variables

Brand  =  "Maruti"
color =  "White"
Capacity =  4
Safety   =  True

2. create an object c1 of class Vehicle and print all the attributes

3. create an object c2 of class Vehicle , 
but change the value of Safety as False
and then  print all the attributes

4. also check if the class Vehicle can access the attributes/variables
if yes , then print the attributes

# 👆 share the output screenshot 📷
'''
print("1. create a class Vehicle with below attributes/variables")
class Vehical:
    Brand  =  "Maruti"
    color =  "White"
    Capacity =  4
    Safety   =  True

print("2. create an object c1 of class Vehicle and print all the attributes")
c1=Vehical()
print(c1.Brand)
print(c1.color)
print(c1.Capacity)
print(c1.Safety)

print("""
3. create an object c2 of class Vehicle , 
but change the value of Safety as False
and then  print all the attributes
""")
c2=Vehical()
print(c1.Brand)
print(c1.color)
print(c1.Capacity)
c2.Safety=False
print(c1.Safety)

print("""
4. also check if the class Vehicle can access the attributes/variables
if yes , then print the attributes
""")
print(Vehical.Brand)
print(Vehical.color)
print(Vehical.Capacity)
print(Vehical.Safety)