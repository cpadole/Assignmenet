#Q1. Write a Python program to convert kilometers to miles?
while True:
    try:
        Km=int(input('Enter value in Km : '))
        Mile=Km*0.621371
        print(Km, 'Km = ',Mile,' Mile')
        break
    except:
        pass

#Q2. Write a Python program to convert Celsius to Fahrenheit?
def CTF(C):
    F=C*9/5+32
    return F
while True:
    try:
        C=int(input('Enter value of tempretaure in Celsius : '))
        print(C,'Celsius = ',CTF(C),' Fahrenheit')
        break
    except:
        pass

#Q3. Write a Python program to display calendar?
import calendar
yy=int(input('Enter year in yy: '))
mm=int(input('Enter month in mm: '))
print(calendar.month(yy,mm))

#Q4. Write a Python program to solve quadratic equation?
import cmath
try:
    print('Enter the value of a, b, c to solve quadralic equetion ax2+bx+c=0')
    a=int(input('a = '))
    b=int(input('b = '))
    c=int(input('c = '))
    d=(b**2)-(4*a*c)

    x1=(-b-cmath.sqrt(d))/(2*a)
    x2=(-b+cmath.sqrt(d))/(2*a)
    print('the solutions are\n','Solution1=',x1,'\n Solution2=',x2,)
except:
    pass

#Q5. Write a Python program to swap two variables without temp variable?
a='i am a'
b='i am b'
print('original','\na = ',a,'\nb = ',b)
a,b=b,a
print('after swap','\na = ',a,'\nb = ',b)