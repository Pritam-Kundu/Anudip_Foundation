#  Write a Python program to find the sum of all elements in a 2D list.
# Initializing a 2d list
twoDList = [[1,2,3],[4,5,6],[7,8,9]]
#Initializing a variable which we will use to store the sum
sum = 0
for i in twoDList:      #At first we are going to 1st inner list
    for j in i:         #Then 2nd inner list
        sum = sum + j   #Adding elements one by one
print("Sum is:",sum)    #Final display of sum