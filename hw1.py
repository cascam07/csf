# Name: ...Cameron Casey
# Evergreen Login: ... cascam07
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"
#x2-5.86 x+ 8.5408
a = 1
b = -5.86
c = 8.5408
sol1 = (-b+math.sqrt(b**2 - 4*a*c))/(2*a)
sol2 = (-b-math.sqrt(b**2 - 4*a*c))/(2*a)
print sol1, sol2
###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test
print hw1_test.a
print hw1_test.b
print hw1_test.c
print hw1_test.d
print hw1_test.e
print hw1_test.f
###
### Problem 3
###

print "Problem 3 solution follows:"

print ((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f)) 


###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").
