rivers=['Saraswati','Bhagirathi','Krishna','Kaveri','Godavari']
#Using basic for loop
print("Number of rivers in list: ",len(rivers))
print("Indexes of rivers in list: ",*range(0,len(rivers)))
print("Printing rivers list ",(rivers)," using basic for loop: ")
for i in rivers:
    print(i)
print("================================================")
fruits=['Apple','Mango','Banana','Pinaple']
#Using range function
print("Number of fruits in list: ",len(fruits))
print("Indexes of fruits in list: ",*range(0,len(fruits)))
print("Printing fruits list ",(fruits)," using range function: ")
for i in range(len(fruits)):
    print(fruits[i])
