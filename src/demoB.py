print("晓晓")
print("晓晓")
print("晓晓")
print("晓晓")
print("晓晓")

def hideName(name):
    if len(name)==1:
        return "*"+name[-1:]
    if len(name)==2:
        return "*"+name[-2:]
    if len(name)>=2:
        return "**"+name[-2:]

print(hideName("3"))
print(hideName("23"))
print(hideName("晓晓晓123"))
print(hideName("晓晓晓晓123"))

listTrasaction = [1,3,3,5,6,6]
print(listTrasaction.count(3))
# print(listTrasaction.pop())
# print(listTrasaction)
# print(listTrasaction.pop())
# print(listTrasaction)
# print(listTrasaction.pop())
print(listTrasaction)
print(hideName("晓晓晓晓123"))
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print(queue.popleft())
print(queue)

vec = [2, 4, 6]
print(vec)
vec = [3*x for x in vec]
print(vec)

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a[2:4])
b = (-1, 1, 66.25, 333, 333, 1234.5)
print(b)

myFriend = {"毛","程雨","吴闯"}
maoFriend = {"毛","程","肖"}
xFriend = myFriend - maoFriend
print(xFriend)
print(myFriend & maoFriend)


from datetime import date

print(date.today())
print(date.min)
print(date.max)











