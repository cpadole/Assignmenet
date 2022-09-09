###1. What are escape characters, and how do you use them?
#Ans: Escape carectors are those charectors which are illegal in string whic we can insert followed by backslash
#ex. \', \", \n, \t etc

###2. What do the escape characters n and t stand for?
#Ans: \n - New line , \t- Tab

###3. What is the way to include backslash characters in a string?
#Ans: we can include \ in a string by write \\ in string

###4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?
#Ans: As we used " " to represent string it will never affect string

###5. How do you write a string of newlines if you don't want to use the n character?
#Ans: we can write multiline string inside """" """
#Ex.
print("""Hi this is 1st line
This is 2nd line""")

###6. What are the values of the given expressions?
#Ans: following expression writtern 1st index charector of string
print('Hello, world'[1])
#following expression writtern 0 to 5th index charector of string
print('Hello, world'[0:5])
#following expression writtern 0 to 5th index charector of string
print('Hello, world'[:5])
#following expression writtern 3rd to last index charector of string
print('Hello, world'[3:])

###7. What are the values of the following expressions?
#Ans: it will convert string into chapital letter
print('Hello'.upper())
#it will written true as first it will convert string into chapital and then check whether string is in chapital letter
print('Hello'.upper().isupper())
#first it will convert string into chapital letter and then converted string into small
print('Hello'.upper().lower())

###8. What are the values of the following expressions?
#Ans: it will spilt string in form of list
print('Remember, remember, the fifth of July.'.split())
#it will join list by given charector
print('-'.join('There can only one.'.split()))

###9. What are the methods for right-justifying, left-justifying, and centering a string?
#Ans: we can use rjust(), center(), ljust() functions
print('right-justifying'.rjust(0)+'centering'.center(20)+'left-justifying'.ljust(0))

###10. What is the best way to remove whitespace characters from the start or end?
#Ans: we can use lstrip() and rstrip() functions
s='     This is a string        '
print(s.lstrip())
print(s.rstrip())
print(s.lstrip().rstrip())
