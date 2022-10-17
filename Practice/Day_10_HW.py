#################################################
# HW
#################################################

# 1. FIND THE DATA TYPE AND LENGHT OF z

z = "Repetition is the mother of learning"

print(type(z))

# 2 . REVERSE THE STRING USING NEGATIVE INDEXING/SLICING 

k  = "Was it a car or a cat I saw? "
p = "Do geese see God?"

print(k[::-1])
print(p[::-1])

# 3 . PRINT THE FOLLOWING USING range()

h = "HYDERABAD"
c = "CHENNAI"
d = "DELHI"

for i in range(len(h)):
    print(h[i], end=' ')

print("********************")

for i in range(len(c)):
    print(c[i], end=' ')
print("********************")
for i in range(len(d)):
    print(d[i], end=' ')
print("********************")
# 4.  find number of spaces in song2
#     find count of Ganga in song2
#     replace  Ganga with "GANGA" in song2



song2 = '''
Jana Gana Mana Adhinaayak Jaya Hey, 
Bhaarat Bhaagya Vidhaataa 
Panjaab Sindhu Gujarat Maraatha, 
Draavid Utkal Banga 
Vindhya Himaachal Yamuna Ganga, 
Vindhya Himaachal Yamuna Ganga, 
Uchchhal Jaladhi Taranga
Tav Shubh Naamey Jaagey, 
Tav Shubh Aashish Maange Gaahey 
Tav Jayagaathaa 
Jana Gana Mangal Daayak, Jaya Hey Bhaarat Bhaagya Vidhaataa 
Jaya Hey, 
Jaya Hey, 
Jaya Hey, 
Jaya Jaya jaya, 
Jaya Hey
'''

print(song2.count(" "))
print(song2.count("Ganga"))
print(song2.replace("Ganga","GANGA"))


# 5 . using format() method print below  

s = "sun"
m = "moon"
e = "earth"

print("{1} is nearest and {0} is farthest from {2}".format(s, m, e))
print("{0} is biggest of {2} and {1}".format(s, m, e))
print("the order is {} , {} and {}".format(s, m, e))

" sun is farthest from earth and nearest is moon"
#  sample ans of above output : 
print("{0} is farthest from {1} and nearest is {2}".format(s,e,m))

"moon is nearest and sun is farthest from earth"

"sun is biggest of earth and moon"

"the order is sun , earth and moon"
