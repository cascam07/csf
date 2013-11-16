# Name: Cameron Casey
# Evergreen Login: cascam07
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

"""
Define a function that takes in 3 parameters that are all integers (x,y,z). 
The function will multiply x by y and then add the result to z. Then return the result.
"""

def arithmetic(x,y,z):
    return ((x*y)+z)

print "Given x = 2, y = 3, and z = 4, (x*y)+z = ",arithmetic(2,3,4)

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

"""
Create a Dictionary that holds the phone numbers for Joe (111-222-3333),
Bob (222-333-4444), and Zach (333-444-5555). The names are the keys. 
Then delete Bob from the list and add Suzy (444-555-6666).
"""

phone = {'Joe':'111-222-3333','Bob':'222-333-4444','Zach':'333-444-5555'}
print phone
del(phone['Bob'])
phone['Suzy']='444-555-6666'
print phone
###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

"""
Using one or more of the following dictionaries, 
write two statements using the id function about object equality 
(one that prints True and one that prints False).

dict1 = {1:2, 3:4, 5:6}
dict2 = {1:2, 3:4, 5:6}
dict3 = dict1
"""
dict1 = {1:2, 3:4, 5:6}
dict2 = {1:2, 3:4, 5:6}
dict3 = dict1

print "dict1 == dict2 : ", id(dict1)==id(dict2)
print "dict1 == dict3 : ", id(dict1)==id(dict3)
###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

"""
Use a for loop to add 1 to each item on the following list and print each total.
list1 = [1, 2, 3, 4, 5]
"""
list1 = [1, 2, 3, 4, 5]
list_copy = list1[:]
for i in range(len(list_copy)):
    a = list_copy[i] + 1
    list_copy[i] = a
print "list1: ", list1
print "modified list1: ", list_copy

###
### Problem 7
###


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

"""
Create a list of 10 random numbers. Sort them in ascending order using a 
nested looping structure (selection sort). Don't use list.sort().
"""
import random
a = range(10)
random.shuffle(a)
print "unsorted list: ",a
count = 0

while count<len(a): #loop runs as many times as there are items in a
    minimum = a[count] #initial minimum is first unsorted item
    for i in range(count, len(a)): #only runs through unsorted items
        if a[i]<=minimum:
            minimum = a[i]
            tracking = i #location of smallest element
        else: pass
    temp = a[count]
    a[count] = minimum #swaps location of smallest element and first unsorted element
    a[tracking] = temp
    count += 1 #elements up to index count are now sorted
print "sorted list: ",a
###
### Collaboration
###

# ... Joe Clevenger and I worked together to create questions. We answered the other group's
# questions on our own. I looked at the wikipedia page for "Selection sort" to figure out
# how the algorithm worked. I also referenced python.org for documentation on built in functions.