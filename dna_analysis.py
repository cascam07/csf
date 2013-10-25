# Name: Cameron Casey
# Evergreen Login: cascam07
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G, C, A, and T nucleotides seen so far.
gc_count = 0
at_count = 0
g_count = 0
c_count = 0
a_count = 0
t_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
    # if the bp is an A or a T,
    if bp == 'A' or bp == 'T':
        #increment the count for at
        at_count = at_count + 1
    if bp == 'G':
        g_count = g_count +1
    if bp == 'C':
        c_count = c_count +1
    if bp == 'A':
        a_count = a_count +1
    if bp == 'T':
        t_count = t_count +1

# divide the gc_count  and at_count by the total_count
gc_content = float(gc_count) / (g_count+c_count+a_count+t_count)
at_content = float(at_count) / (g_count+c_count+a_count+t_count)
atgc_content =float(at_count) / float(gc_count)

# Print the answer
print 'GC-content:', gc_content
print 'AT-content:', at_content
print 'G-count:', g_count
print 'C-count:', c_count
print 'A-count:', a_count
print 'T-count:', t_count
print 'Sum of A, T, G, C: ', g_count+c_count+a_count+t_count
print 'Total count: ', total_count
print 'seq length: ', len(seq)
print 'AT/GC: ', atgc_content