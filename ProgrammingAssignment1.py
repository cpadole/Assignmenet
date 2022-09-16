#Q1:Write a Python program to print "Hello Python"?
print('Hello python')

#Q2:Write a Python program to do arithmetical operations addition and division.?
while True:
    operation=input('for addition press--> a\nfor division press -->d\n')
    if operation=='a' or operation=="d":
        a=int(input('enter 1st value \n'))
        b=int(input('enter 2nd value \n'))
        if operation=='a':
            c=a+b
            print("a+b=",c)
        if operation=='d':
            c=a/b
            print("a/b=",c)
        break

    else:
        pass


#Q3:Write a Python program to find the area of a triangle?
h=int(input("Enter height of triangle\n"))
w=int(input("Enter width of triangle\n"))
A=0.5*h*w

print('Area of triangle =',A)

#Q4:Write a Python program to swap two variables?
a=13
b=20
print("old a=",a,"old b=",b)
c=a
a=b
b=c
print("new a=",a,"new b=",b)

#Q5:Write a Python program to generate a random number?
import random
print(random.random())