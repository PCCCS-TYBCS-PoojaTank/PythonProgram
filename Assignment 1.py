Name:Pooja Tank    
Roll no: 4205
PCCCS TY.BSc(CS)


# Arithmetic Operators
a = 6
b = 2
print('Sum:', a + b)
print('Substraction:', a - b)
print('Multiplication:', a * b)
print('Division(float):', a / b)
print('Division(floor):', a // b)
print('Modulus:', a % b)
print('Exponent:', a ** b)

# Comparison operators
a = 10
b = 5
print('a > b is',a > b)
print('a < b is',a < b)
print('a == b is',a == b)
print('a != b is',a != b)
print('a >= b is',a >= b)
print('a <= b is',a <= b)

# Logical Operators
a = 8
b = 3
print('a and b is',a and b)
print('a or b is',a or b)
print('not a is', not a)

# Bitwise Operator
a = 3
b = 5
print('a & b is', a&b)

# Identity Operator
# Using 'is' identity operator
a = 7
if(type(a) is int):
    print('True')
else:
    print('False')

# Using 'is not' identity operator
b = 3.2
if(type(b)is not int):
    print('True')
else:
    print('False')

# Membership Operator
str = 'Python operators'
dict={6:'June',12:'Dec'}
print('P' in str)
print('Python' in str)
print('python' not in str)
print(6 in dict)
print('Dec' in dict)

# Conditional Statements

# Python program to illustrate If statement
i = 10
if(i>15):
    print("10 is less than 15")
print("I am Not in if")

# Python program to illustrate If else statement
i = 20;
if(i<15):
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")
# python program to illustrate nested If statement
i = 10
if(i == 10):
    # First if statement
    if(i<15):
        print("i is smaller than 15")
        #Nested-if statement
        #Will only be executed if statement above
        #it is true
        if(i<12):
            print("i is smaller than 12 too")
        else:
            print("i is greater than 15")

# python program to illustrate if-elif-else ladder
i = 20
if(i == 10):
    print("i is 10")
elif(i == 15):
    print("i is 15")
elif(i == 20):
    print("i is 20")
else:
    print("i is not present")
