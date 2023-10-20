# 1. sum two numbers from keyboard
'''x=int(input("a="))
y=int(input("b="))
c=x+y
print("sum =",c)

# 2. multiple vales from keyboard
name=input("enter values:").split()
print(name)

# 3.number is divisible by 7 or not
A=21
if A%7==0:
    print("number is divisible by 7")
else:
    print("number is not divisible by 7")

# 4. number is multiple of 3 or not
B=26
if B%3==0:
    print("number is multiple of 3")
else:
    print("number is not multiple of 3")
    
# 5. number is p+ or n-
num=int(input("enter number:"))
if num>=0:
    print("number is positive")
else :
    print("number is negative")

# 7.number is 3 digit or not
n=int(input("enter number:"))    
if n>=100 and n<=999:
    print("number is 3 digit")
else:
    print("number is not 3 digit")
    
# 8.number is even or odd by cmd
number=int(input("enter value:"))
if number%2==0:
    print("number is even")
else:
    print("number is odd")
# 9.greatest num in given two numbers
num1, num2 = 60 , 30
if num1>num2:
  print(num1)
else:
  print(num2)
# 10.small num in 2 numbers
N1 ,N2 = 20,34
if N1<N2:
    print(N1)
else:
    print(N2)'''
#11.greatest num in 3 numbers
n1,n2,n3 = 65,94,54
if n1>= n2 and n1 >= n3:
    print( n1)
elif n2 >= n1 and n2 >= n3:
    print(n2)
else:
    print(n3)
#12. 3 numbers in ascending order     
numA=int(input("Enter First number : "))
numB=int(input("Enter Second number : "))
numC=int(input("Enter Third number : "))
if numA<numB and numA<numC:
    if numB<numC:
        x,y,z=numA,numB,numC
    else:
        x,y,z=numA,numC,numB
elif numB<numA and numB<numC:
    if numA<numC:
        x,y,z=numB, numA, numC
    else:
        x,y,z=numB, numC, numA
else:
    if num1<num2:
        x,y,z= numC,numA,numB
    else:
        x,y,z= numC,numB, numA
print("Numbers in ascending order are : ",x,y,z)    
    