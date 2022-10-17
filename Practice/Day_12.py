#comparison
'''
==
!=
<
<=
>
>=
'''

#operators
'''
# Logical operators
#  AND , OR ,NOT 
# Identity operators
#  IS , NOT IS 
# Membership operators
# IN , NOT IN 
'''

a=100
b=200
c=300
d=300
e="ashish"
print(c==d)
print(a!=b)
print(a<b)
print(c<=d)
print(b>a)
print(c>=d)


print(c==d and a!=b) # true and true = true
print(a>b and c==d)  # false and true = false
print(b<a and c<=d)  # true and fale = false
print(a>=d and d<=a) # false and false = false

print(c==d or a!=b) # true or true = true
print(a>b or a<b) # false or false = true
print(a<b or a>b) # true or false = true
print(a>b and a>d) # false or false = false

print("a" in e)
print('d' not in e)

#Use of operators in condition

a=int(input("Enter value of a: "))
b=int(input("Enter valuse of b: "))
print(f"Value entered is a={a} and b={b}")
if a<b:
    print(f"{a} is less then {b}")
else:
    print(f"{a} is greater then {b}")

# Find pass or fail

e=int(input("Enter marks scored in Englist out of 100: "))
m=int(input("Enter marks scored in Marathi out of 100: "))
h=int(input("Enter marks scored in Hindi out of 100: "))
ma=int(input("Enter marks scored in Maths out of 100: "))
s=int(input("Enter marks scored in Science out of 100: "))

total=e+m+h+ma+s
#average=total/5
percentage=(total/500)*100
print(f"{percentage}")
if percentage>=90:
    print("Grade A")
elif percentage >= 65 and percentage < 90:
    print("Grade B")
else:
    print("Grade C")