import os

from anObject import anObject
from anObjectChild import *

#
# thisIsAList = ["listItem1", "listItem2", "listItem3", "listItem4", "listItem5"]
# 
# thisIsATuple = ("tupleItem1", "tupleItem2", "tupleItem3", "tupleItem4", "tupleItem5")
# 
# thisIsASet = {"setItem1", "setItem2", "setItem3", "setItem4", "setItem5"}
# 
# thisIsADict = {
#     "key1": "value1",
#     "key2": "value2",
#     "key3": "value3",
#     "key4": "value4",
#     "key5": "value5"
# }
# 
# 
# def gen():
#     yield "one"
#     yield "two"
#     yield "three"
# 
# 
# mylist = ['bob', 'amy', 'greg']
# myit = iter(mylist)
# for x in myit:
#     print(x)
# 
# 
# 
# def decoratedAdd(function):
#     def inner(x,y):
#         print(x)
#         print("plus")
#         print(y)
#         print("equals")
#         return function(x, y)
#     return inner
# 
# @decoratedAdd
# def add(x, y):
#     print(x+y)
# 
# add(1, 2)
# add(8, 12)
# 
# obj1 = anObject()
# print(obj1.name)
# print(obj1.property1)
# print(obj1.property2)
# #print(obj1.__secretProperty)
# #print(obj1.__getSecretProperty())
# #print(obj1.proxyGetSecretProperty())
# #print(obj1.property3)
# 
# 
# obj2 = anObjectChild()
# print(obj2.name)
# print(obj2.property3)
# #print(obj2.__secretProperty)
# #print(obj2.proxyGetSecretProperty())
# 

f1 = open("text1.txt", "w")
f1.write("A way of opening")
f1.close()

with open('text2.txt', 'w') as f2:
    f2.write('this is a txt file')
    f2.write('\n')
    f2.write('this is more txt')
    f2.write('\n')

with open('text2.txt', 'r') as f2:
    for line in f2:
        print(line)


if os.path.exists('text2.txt'):
    os.remove('text2.txt')
    print('File removed')
else:
    print('File not found')

mywords = ['one', 'two', 'three', 'four','five', 'six', 'seven', 'eight']
with open('text2.txt', 'a') as f2:
    for word in mywords:
        f2.write(word)
        f2.write('\n')


import camelcase

camel = camelcase.CamelCase()

some_text = "some text that is not camel case"

print(camel.hump(some_text))