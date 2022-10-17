# If we refer one list variable to other variable then its just a referance of original list assigned to new variable. NO MEMORY created
# i.e no copy done, only list referancing
# i.e. update to original list will be shown in both variable lists.
listA = [1,2,3,4,5]
listB = listA # Created only referance
print(listA)
print(listB) # ONLY REFERANCE


listA[1]=100
print(listA)
print(listB)

listB[1]=200
print(listA)
print(listB)

#For making a copy you need to use COPY method.
