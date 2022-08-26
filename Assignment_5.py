####1. What does an empty dictionary's code look like?
#Ans: it will look like {}
from typing import Dict

empty_Dictionary=dict()
print(type(empty_Dictionary))
print(empty_Dictionary)

print('------------------------------------------------------------')
###2. What is the value of a dictionary value with the key 'foo' and the value 42?
#Ans: [42]
d={'foo':42}
print(d.values())

print('------------------------------------------------------------')
###3. What is the most significant distinction between a dictionary and a list?
#Ans: Dictionary : it is having key, value pairs and list having only values.

###4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
#Ans: It will give Keyerror : 'foo'
try:
    spam = {'bar': 100}
    print(spam['foo'])
except Exception as e:
    print(e)

print('------------------------------------------------------------')
###5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
#Ans: both expression return whether 'cat' is availble in keys or not in bool type
spam={'cab':'cat'}
print('cat' in spam)
print('cat' in spam.keys())

print('------------------------------------------------------------')
###6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
#Ans: 'cat' in spam check whether 'cat' is available in keys and 'cat' in spam.values() check whether 'cat' is availble in values in bool type
print('cat' in spam)
print('cat' in spam.values())

print('------------------------------------------------------------')
###7. What is a shortcut for the following code?
#if 'color' not in spam:
#    spam['color'] = 'black'
#Ans:Shortcut will be
spam['color'] = 'black'

print('------------------------------------------------------------')
###8. How do you 'pretty print' dictionary values using which module and function?
import pprint
d=[{'a':133,'b':112,'c':356},{'a':765,'b':34,'c':98},{'a':122,'b':157,'c':987}]
pprint.pprint(d)

print(d)

