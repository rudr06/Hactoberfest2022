'''
This program prompts the user to enter the number of digits(range) of the fibonacci series to be printed
Eg. input: 5
    output: 0 1 1 2 3 
    
    input: 7
    output: 0 1 1 2 3 5 8
'''


print("fibonacci series!")

# 'rang' here is the range 
rang = int(input("enter a range: "))

# fibonacci series = 0,1,1,2,3,5,8...

a = 0
b = 1
print(a,b, end = '')
print(" ", end = '') #this line gives a space after printing b

for i in range (1, rang-1, 1): 
    c = a + b
    print(c, end = '')
    a = b
    b = c
    print(" ", end = '') #this line gives a space after entering a character (number) in the loop
    
