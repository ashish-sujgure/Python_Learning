#################################################
# HW
#################################################

'''
1. Create a class with below attribute 

group  =  'dog'
age   =  7
class  = 'canine'

also create a method named Display() to print below

"Dog is man's Best friend"

call above attributes and methods by creating object named

Tommy

'''

class animal:
    group='dog'
    age='7'
    classs='canine' # class is a reserved pytohn keyword and cannot be used as for variable declaration. Hence using classs

    def display():
        print("Dog is man's Best friend")

Tommy=animal
print(Tommy.group)
print(Tommy.age)
print(Tommy.classs)
Tommy.display()