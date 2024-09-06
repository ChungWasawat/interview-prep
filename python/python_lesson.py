"""data type"""
a = 10              # int
#print(type(10_000_000))
a = 5.5             # float
a = "hi"            # string
a = True            # boolean
#print( bool(0) == bool(None))
b = [1, 2]          # list
b = (1, 2)          # tuple imputable
b = {'a':1, 'aa':2} # dict
b = {1, 2}          # set

"""built-in math function"""
a = sum([1,2])
a = min([1,2,3])
a = max([1,2,3])
a = abs(-5)
a = round(3.14159, 2)

"""string operation"""
a = "Hello".upper()
a = "Hello".lower()
b = "Hello World".split()
b = ",".join(["a", "b"])
a = "Hola".replace("H", "J")

"""list operation"""
b = [5, 4, 3, 2]
b.append(1)
b.remove(3)
a = b.pop()
b.sort()
b.reverse()

"""error handling"""
try:
    f = open('test.txt') 
    print(f.read())
except Exception as e:
    print(e)
finally:
    f.close()

"""file"""
#with open("test.txt", "a") as file:
#    file.write("\n???")
with open("test.txt", "r") as file:
    content1 = file.readline(1)
    content2 = file.readlines()
    #print(content1, content2)

"""Class"""
class MyClass:
    def __init__(self, greet="Hello"):
        self.greet = greet

    def greetUser(self):
        print(self.greet)
c = MyClass("Hola")
c.greetUser()

"""lambda and list comprehension"""
d = lambda x: [x **2 for x in range(x+3)]
#print(d(2))

"""generator"""
b = (x**2 for x in range(5))

"""loop dictionary"""
b = {'a':1, 'b':3, 'c': 5, 'd': 7, 'e': {'f': {'g': 9}}}
#for i in b.keys():
#    print(i)
#for i in b.values():
#    print(i)
#for i,j in b.items():
#    print(i,j)
print(b.get('e').get('f', 'g'))

"""datetime"""
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

"""json and pandas"""
import json
import pandas as pd

d = {
    "a": { "x": 2, "xx": 3, "xxx": 4 },
    "b": { "x": 7, "xx": 8, "xxx": 9 },
    "c": { "x": 6, "xx": 7, "xxx": 8 }
}
json.dump(d, open("test.json", "w") )

with open("test.json", "r") as file:
    # cannot read string with load
    raw = json.load(file)
    #print(raw)

#print(json.loads('{"a": "loads"}'))

df = pd.read_json("test.json", orient="records")
df = pd.read_json("test.json", orient="index")
## what if have to create dataframe from list of dict, these functions can help to extract data: dict.get(), df.columns = ["",""], df.set_index("")


"""logging"""
import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

path = "path"
ke = "key error"

# different types of log
#logging.debug(f"variable has value {path}")
#logging.info("Data has been transformed and will now be loaded")
#logging.warning("Unexpected number of rows detected")
#logging.error(f"{ke} arose in execution")