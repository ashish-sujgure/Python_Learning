#################################################
# HW
#################################################

'''
1. write a function to take email id from user and 
separate the name ans domain

Eg. raghav123@gmail.com
output should be  [raghav123, gmail.com]

2. write a function to take 3 integers from user and 
give average as output

3.  write a function to take student name and
print "Good luck" with student name
"Good luck" to be used as default argument


4. use *args and find average of 5 nos 
NOTE : dont use 5 directly, instead find
the leng of the argument.


# 👆 share the output screenshot 📷
'''
# 1. write a function to take email id from user and separate the name ans domain
# Eg. raghav123@gmail.com output should be  [raghav123, gmail.com]
def fun_email_name(email):
    print("Entered email ID is: ", email)
    print("Requested output is: ", email.split("@"))
fun_email_name("ashish.sujgure@gmail.com")

# 2. write a function to take 3 integers from user and 
# give average as output
def fun_average_cal(num1,num2,num3):
    total=num1+num2+num3
    return(total/3)
average=fun_average_cal(5,10,15)
print(average)

# 3.  write a function to take student name and
# print "Good luck" with student name
# "Good luck" to be used as default argument
def fun_welcome(Name,gret='Good luck'):
    #return ('good luck', Name)
    print(gret, Name)
fun_welcome("Ashish")

# 4. use *args and find average of 5 nos 
# NOTE : dont use 5 directly, instead find
# the leng of the argument.
def fun_average_5(*args):
    ln=len(args)
    total=sum(args)
    if ln == 5:
        return total/ln
    else:
        return "WARNING! Enter only five numbers"
print(fun_average_5(1,2,4,5,6))
print(fun_average_5(1,2,4,5))