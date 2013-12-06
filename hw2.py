# Name: ... Cameron Casey
# Evergreen Login: ... cascam07
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.
## Hello!

###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

import hw2_test
i = 1
x = 0
while (i<=hw2_test.n):
    x = x + i
    i=i+1
print x
###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "\n"
print "Problem 2 solution follows:"

for t in range(2,11):
    print '1/',t


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "\n"
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range(n+1):
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2

###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "\n"
print "Problem 4 solution follows:"

n = 10
factorial = 1
for i in range(1,n+1):
    factorial = factorial*i
print n, "factorial:", factorial
###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "\n"
print "Problem 5 solution follows:"

n = 10
for counter in range(n): #execute inner loop 10 times
    factorial = 1
    for i in range(1,n+1): #computes n factorial
        factorial = factorial*i
    print factorial
    n=n-1

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "\n"
print "Problem 6 solution follows:"

reciprocal = 1 
n = 10
for counter in range(n): #execute inner loop n times
    factorial = 1.0
    for i in range(1,n+1): #adds up 1/n!
        factorial = factorial*i
    reciprocal = reciprocal + (1/factorial)
    n=n-1
print reciprocal
###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... The assignment took me around 3 hours. It would have been helpful to get
# ... some examples of how to use for loops in class before spending so much
# ... time on the code critique.
