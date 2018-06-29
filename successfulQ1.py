print("Please enter 5 integers...")
int1 = input()
int2 = input()
int3 = input()
int4 = input()
int5 = input()  #has the user input a collection of 5 integers

unsorted_list = [int(int1), int(int2), int(int3), int(int4), int(int5)]    #puts users inputs in a list and casts them into int
length = len(unsorted_list)     #number of elements in the list
min = unsorted_list[0]  #first element in list
max = unsorted_list[0]

for index in range(length):     #the loop will go to every element in the list one by one
   if min > unsorted_list[index]:  #min is compared with every element to see if it's the smallest
       min = unsorted_list[index]  #if a number is smaller than min, min becomes the smaller number
print("the minimum is " + str(min))

for index in range(length): #block of code compares the first number to every int in the list
   if max < unsorted_list[index]:
       max = unsorted_list[index]  #if any number is bigger, that number becomes the max
print("the maximum is "+ str(max))

total = 0

for index in range(length):
   total = total + unsorted_list[index]  #adds the next elements value to the total
   mean = total/length
print("the mean of the five integers is " + str(mean))