"""-----------------------------data type-----------------------------"""
a = 10              # int
#print(type(10_000_000))
a = 5.5             # float
a = "hi"            # string
a = True            # boolean
#print( bool(0) == bool(None))
b = [3, 1, 2]       # list
b = (1, 2)          # tuple imputable
b = {'a':1, 'aa':2} # dict
b = {1, 2}          # set

a, b = 5, "txt"
#print(f"{b} is string, {a} is integer")
#print("%s is string, %d is integer" %(b, a))

"""-----------------------------set-----------------------------"""
b = set(["ant", "bird", "cat", "bird"])
c = set(["bird", "cat", "dog", "cat"])

if b & c == b.intersection(c):
    #print("intersect")
    pass
if b | c == b.union(c):
    #print("union")
    pass
#print(b.difference(c), c.difference(b))
#print(b.symmetric_difference(c), c.symmetric_difference(b))

"""-----------------------------built-in math function-----------------------------"""
a = sum([1,2])
a = min([1,2,3])
a = max([1,2,3])
a = abs(-5)
a = round(3.14159, 2)

"""-----------------------------string-----------------------------"""
a = "Hello".upper()
a = "Hello".lower()
b = "Hello World".split()
b = ",".join(["a", "b"])
a = "Hola".replace("H", "J")
a = "hello" + " World" * 2
a = a[:7]

import string
if ' a' in string.whitespace:
    print(1)
elif '2s' in string.digits:
    print(2)
elif '/e' in string.punctuation:
    print(3)
elif 'a3' in string.ascii_letters:
    print(4)

"""-----------------------------list operation-----------------------------"""
b = [5, 4, 3, 2]
b.append(1)
b.remove(3)
a = b.pop()
b.sort()
b.reverse()

# sorted() is compatible with set(), tuple and return to list
# but using sorted() with sentence can be slightly annoying because of whitespace, so use split() and ' '.join() to help 
#print(sorted([3,2,1]), sorted((3,2,1)), sorted(set([3,2,1])))

"""-----------------------------dictionary operation-----------------------------"""
b = {'a':1, 'b':3, 'c': 5, 'd': 7, 'e': {'f': {'g': 9}}}
#for i in b.keys():
#    print(i)
#for i in b.values():
#    print(i)
#for i,j in b.items():
#    print(i,j)
#print(b.get('e').get('f', 'g'))

del b["b"]
b.pop("c")

"""-----------------------------enumerate-----------------------------"""
b = ['a', 'b', 'c', 'd']
for index, value in enumerate(b):
    #print(index, value)
    pass

first = ["a", "b", "c"]
second = ("d", "e", "f")
third = "ghi"
pairs = [('a', 'd'), ('b', 'e'), ('c', 'f')]
first_new, second_new = zip(*pairs)

# is check instance-level, == check value-level
if second is second_new:
    print(True)
elif second == second_new:
    print(True, True)
    
# strict False=Default, tuple and list are okay
#print(tuple(zip(first, second, third, strict=True)))

for count, (one, two, three) in enumerate(zip(first, second, third)):
    #print(count, one, two, three)
    pass

import itertools
for count, one, two, three in zip(itertools.count(), first, second, third):
    #print(count, one, two, three)    
    pass

b = ['name', 'last_name', 'age', 'job']
c = ['John', 'Doe', '45', 'Python Developer']
d = dict(zip(b, c))
#print(d)
d.update(zip(['job'], ['Python Consultant']))
#print(d)

"""-----------------------------regular expression-----------------------------"""
import re
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")
pattern = r"^[\w][\w\W]*@[\w]+.[\w]{1,9}" 
#test_email(pattern)

"""-----------------------------error handling-----------------------------"""
try:
    f = open('test.txt') 
    print(f.read())
except Exception as e:
    print(e)
finally:
    f.close()

"""-----------------------------logging-----------------------------"""
import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

path = "path"
ke = "key error"

# different types of log
#logging.debug(f"variable has value {path}")
#logging.info("Data has been transformed and will now be loaded")
#logging.warning("Unexpected number of rows detected")
#logging.error(f"{ke} arose in execution")

"""-----------------------------Class and Enum-----------------------------"""
class MyClass:
    def __init__(self, greet="Hello"):
        self.greet = greet

    def greetUser(self):
        return self.greet
c = MyClass("Hola")
a = c.greetUser()

from enum import Enum
class HTTPStatusCode(Enum):
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500

for i in (HTTPStatusCode):
    if 200 == i.value:
        print(i.name, i)

"""-----------------------------function-----------------------------"""
""" *,** in front of parameter"""
# learn more about positional parameter (*, /)
def f(a, b, *c):
    print(list(c))
#f(1, 2, 3, 4 ,5)
def f(a, b, **option):
    if option.get("c") == 0:
        print(a+a)
    elif option.get('c') == 1:
        print(b+b)
    else:
        print(a+b)
#f('op', 'tion')
#f('op', 'tion', c=1)
#def f():

def repeater(old_function):                 #function as parameter here
    # See learnpython.org/en/Multiple%20Function%20Arguments for how *args and **kwds works (kwds is just optional here)
    def new_function(*args, **kwds): 
        old_function(*args, **kwds) 
        old_function(*args, **kwds) 
    return new_function 
@repeater
def multiply(num1, num2):
    print(num1 * num2)
#multiply(5, 3)

def multiply(multiplier):                   #variable for decorator's parameter
    def multiply_generator(old_function):   #function as parameter here
        def new_function(*args, **kwds):    
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num): #as old function
    return num
# Now return_num is decorated and reassigned into itself
return_num(5) # should return 15

"""map"""
my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = list(map(str.capitalize, my_pets))       #this function needs one parameter
#print(uppered_pets)
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344]
result = list(map(round, circle_areas, range(1, 6)))    #this function needs two parameter

"""filter"""
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk", "tenet")
palindromes = list(filter(lambda word: word == word[::-1], dromes))
#print(palindromes)

"""reduce"""
from functools import reduce
d = ['a', 'b', 'c', 'd']
def custom_sum(a, b):
    return a + b
e = reduce(custom_sum, d, 'e')
#print(e)

"""call from other directory"""
from py_modules.function import plus
#print( plus(2,3) )

"""lambda and list comprehension"""
d = lambda x: [x **2 if x%2==0 else x for x in range(x+3)]
#print(d(2))

"""-----------------------------partial(for parameter)-----------------------------"""
from functools import partial
e = partial(plus, 2)
#print(e(3))

"""-----------------------------Counter-----------------------------"""
from collections import Counter
#print(Counter(['a','b','a','c','d','c']))

"""-----------------------------generator-----------------------------"""
# used for iteration
b = (x**2 for x in range(5))
for i in b:
    #print(i)
    pass

def f():
    for x in range(0, 5):
        # 'yield' store data in memory, not just return value and force to stop the remaining lines in the function like 'return'
        yield x **2
for i in f():
    #print(i)
    pass

def f():
    yield('Hi')
    yield(12)
for i in f():
    #print(i)
    pass

"""-----------------------------datetime-----------------------------"""
import datetime
import time

#date_in_ISOFormat
todays_Date = datetime.date.fromtimestamp(time.time())
a = todays_Date.isoformat()

#DateTime_in_ISOFormat
todays_Date = datetime.datetime.now()
a = todays_Date.isoformat()

#print(todays_Date.strftime("%Y-%m-%d"))

from datetime import timedelta
#print(todays_Date + timedelta(days=1))

"""-----------------------------file-----------------------------"""
#with open("test.txt", "a") as file:
#    file.write("\n???")
with open("test.txt", "r") as file:
    content1 = file.readline(1)
    content2 = file.readlines()
    #print(content1, content2)

"""-----------------------------json and pandas-----------------------------"""
import json
import pandas as pd

d = {
    "a": { "x": 2, "xx": 3, "xxx": 4 },
    "b": { "x": 7, "xx": 8, "xxx": 9 },
    "c": { "x": 6, "xx": 7, "xxx": 8 }
}
json_d = json.dumps(d, indent=2)        # serializing json
json.dump(d, open("test.json", "w") )   # write dictionary to json file

with open("test.json", "r") as file:
    # cannot read string with load because it reads only json type (serialization)
    raw = json.load(file)
    #print(raw)

#print(json.loads('{"a": "loads"}'))
df = pd.read_json("test.json", orient="records")
df = pd.read_json("test.json", orient="index")
## what if have to create dataframe from list of dict, these functions can help to extract data: dict.get(), df.columns = ["",""], df.set_index("")

"""-----------------------------Code introspection-----------------------------"""
#help(dir)
#print( dir(plus))