#write a python function that accepts a string and calculate the number 
#of uppercase and lower case letters.
string=input("enter string:")
count1=0
count2=0
for i in string:
    if(i.islower()):
        count1=count1+1
    elif(i.isupper()):
        count2=count2+1
        print("The number of lowercase characters is:")
        print(count1)
        print("The number of uppercase characters is:")
        print(count2)