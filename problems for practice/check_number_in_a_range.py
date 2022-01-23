#write a python function to check whether a number is in a given range.
test_list=[4,5,6,7,3,9]
#printing original list
print("The original list is::"+str(test_list))
#initialization of range
i,j=3,10
#test if list contains elements in range
#using loop
res=True
for ele in test_list:
    if ele<i or ele>=j:
        res=False
        break