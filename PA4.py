#Q1. Write a Python Program to Find the Factorial of a Number?
while True:
    try:
        a=int(input('Enter the number to find out factorial\n'))
        i=1
        k=1
        while a>=i:
            k=k*i
            i=i+1

        print('factorial of',a,' is ',k )
        break
    except:
        pass

#Q2. Write a Python Program to Display the multiplication Table?
while True:
    try:
        a=int(input('provide a number to get its multiplication table\n'))
        i=1
        while i<=10:
            k=a*i
            print(a,'x',i,'=',k,end='\n')
            i=i+1
        break
    except:
        pass

#Q3. Write a Python Program to Print the Fibonacci sequence?
while True:
    try:
        a=int(input('provide a number to get Fibonacci sequence\n'))
        n1=0
        n2=1
        count =0
        while a>count:
            print(n1)
            m=n1+n2
            n1=n2
            n2=m
            count=count+1
        break
    except:
        pass

#Q4. Write a Python Program to Check Armstrong Number?
while True:
    try:
        a= int(input('Enter a number to check Armstrong Number\n'))
        temp=a
        m=0
        while temp>0:
            k = temp%10
            m=m+k**3
            temp= int(temp/10)
        if a==m:
            print(a, 'is Armstrong Number')
        else:
            print(a, 'is not Armstrong Number')
        break
    except:
        pass

#Q5. Write a Python Program to Find Armstrong Number in an Interval?
while True:
    try:
        h=int(input('write a interval to get amstrong number\n'))
        a=0
        while h>a:
            temp = a
            m = 0
            while temp > 0:
                k = temp % 10
                m = m + k ** 3
                temp = int(temp / 10)
            if a == m:
                print(a,end='\n')
            a=a+1
        break
    except:
        pass

#Q6. Write a Python Program to Find the Sum of Natural Numbers?
while True:
    try:
        a=int(input('Enter the number to calculate natural number sum'))
        n=1
        sum=0
        while n<=a:
            sum=sum+n
            n=n+1
        print('Sum of ',a,' natural number is ', sum)
        break
    except:
        pass