n=9
series = raw_input("sum or fibonacci?: ")
a = 0
b = 0
c = 1
summ = 0

if series == 'fibonacci':
    for i in range(n-1): 
        a = b #sets hold number equal to second hold number
        b = c #sets second hold number equal to the third hold number
        c = a+b #sets third hold number equal to the sum of the first and second hold numbers
    print c #prints the nth fibonacci number
elif series == 'sum':
    for i in range(n+1): #adds all the multiples of 3 up to 3n
        summ = summ + 3*i
    print summ
else:
    print "Invalid string"