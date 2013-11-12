import math

def problem_4(n): #takes a list of integers and finds the largest difference between successive elements

    temp = 0
    #n = [0, 1, 4, 5, 6, 15]
    for i in (range(len(n)-1)):
        if (n[i+1]-n[i])>temp:
            temp = abs(n[i+1] - n[i])
        else: continue
    return temp


def problem_10(x, n): #takes two integers and computes x^n
    result = x
    i = 0
    if n>0:
        while i<n-1:
            result = (result*x)
            i += 1
    elif n<0:
        while i>n+1:
            result = result*x
            i -= 1
        result = 1/float(result)
    else:
        result = 1
    return result
    
def problem_16(n): #takes list of numbers and finds minimum value in list
    minimum = n[0]
    for i in range(len(n)-1):
        if n[i]>n[i+1]:
            minimum = n[i+1]
        else: continue
    return minimum

def problem_28(n, element):
    """
    Takes list of increasing integers and an element in that list. Searches list for that element.
    Returns True if element is in the list and False otherwise.
    """
    for i in range(int(math.floor(math.log(len(n))/math.log(4)))): #log base 4 of elements in list
        a = n[0:(len(n)/4)]      
        b = n[(len(n)/4):(len(n)/2)]
        c = n[(len(n)/2):((3*len(n))/4)]
        d = n[((3*len(n))/4):n[len(n)-1]]
    
        if element <= a[len(a)-1]:
            n = a
        elif element <= b[len(b)-1]:
            n = b
        elif element <= c[len(c)-1]:
            n = c
        elif element <= d[len(d)-1]:
            n = d
        else: return False
    for j in n:
        if j == element:
            return True
    return False

def problem_50(n):
    n_copy = n[:]
    for index in range(1,len(n)):
        value = n_copy[index]
        i = index - 1  
        while i>=0:
            if value<n_copy[i]:
                n_copy[i+1] = n_copy[i]
                n_copy[i] = value
                i = i - 1             
            else: break
    return n_copy


result4 = problem_4([0,1,4,7,13,14])
result10 = problem_10(3,0)
result16 = problem_16([4, 3, 7, -9, 1])
result28 = problem_28([1,3,5,6,9,12,16,24],7)
result50 = problem_50([4,2,9,7,9,3,15,1,8])

#print result4
#print result10
#print result16
#print result28
print result50
