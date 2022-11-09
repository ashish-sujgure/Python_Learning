#################################################
# HW
#################################################

'''
1. CREATE TEXT FILE WITH BELOW DATA IN IT AND NAME  IT AS colors.txt

Brown
Yellow
Green


2. READ THE FILE  colors.txt AND DISPLAY THE OUTPUT ON THE SCREEN

3. ADD BELOW DATA IN THE FILE colors.txt WITHOUT REMOVING OLD DATA

BLUE

4. DISLAY THE DATA OF THE FILE colors.txt USING FOR LOOP 


# 👆 share the output screenshot 📷
'''
print("****************************************")

file=open(r"C:\Users\ashis\Python_Learning\Practice\colors.txt","w")
file.write("Brown \nYellow \nGreen")
file.close()

file=open(r"C:\Users\ashis\Python_Learning\Practice\colors.txt","r")
for i in file:
    print(i)

print("****************************************")

file=open(r"C:\Users\ashis\Python_Learning\Practice\colors.txt","a")
file.write("\nBlue")
file.close()

file=open(r"C:\Users\ashis\Python_Learning\Practice\colors.txt","r")
for i in file:
    print(i)