'''
Day 11:
isalpha()
isdigit()
isalnum()
isspace()
istitle()
strip()
split()
'''


a="Ashish"
b="180592"
c="Ash180592"
d='Ashish Sujgure'
e=" Ashish Arun Sujgure "

print(a.isalpha())
print(b.isdigit())
print(c.isalnum())
print(d.isspace())
print(e.istitle())
print(e)
print(e.strip())
print(e.split(" "))

s = "sun"
m = "moon"
e = "earth"
# print("{0} is farthest from {1} and nearest is {2}".format(s,e,m))

#f-format()

print(f"{s} is farthest from {m} and nearest is {e}")


code1 = "123456"

print(code1.isdigit())
print(code1.isnumeric())
print(code1.isdecimal())


name1 = "Rahul"

print(name1)
print(list(name1))