#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
while True:
    try:
        a=int(input('Enter a number to check +ve, -ve or Zeor : '))
        if a==0:
            print('Entered number is Zero')
        if a<0:
            print('Entered number is Negatibe')
        if a > 0:
            print('Entered number is Positive')
        break
    except:
        pass

#Q2. Write a Python Program to Check if a Number is Odd or Even?
while True:
    try:
        a=int(input('Enter a number to check Even or Odd : '))
        b=a%2
        if b==0:
            print('Entered number is Even')
        else:
            print('Entered number is Odd')
        break
    except:
        pass

#Q3. Write a Python Program to Check Leap Year?
while True:
    try:
        y=int(input('Enter a year in YYYY to check leap year or not : '))
        if y/1000>1 and y/1000<9:
            if y%4==0:
                print(y,' is a leap year')
            else:
                print(y,' is not a leap year')
            break
        else:
            continue
    except:
        pass

#Q4. Write a Python Program to Check Prime Number?
while True:
    try:
        a=int(input('Enter a number to check prime number or not : '))
        b=2
        while a!=b:
            if a%b==0:
                print(a,' is not prime number')
                break
            else:
                b=b+1
        if a==b:
            print(a, ' is prime number')
            break
        else:
            break
    except:
        pass

#Q5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
a=1
b=1
while b<1000 and a<1000:
    while a!=b:
        if a%b==0:
            a=a+1
            b=2
        else:
            b=b+1
    if a==b and b<1000 and a<1000:
        print(a, end=" ")
        a = a + 1
        b = 2