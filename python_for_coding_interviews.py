# Variable assignment and update
n = 1
print(f"The value of n is: {n}")

n = "abc"
print(f"The updated value of n is: {n}")

# Multiple assignments
a, b, c = 1, "hello", True

print(f"The value of a, b, c is: {a}, {b}, {c}")


# Increment
m = 1
m = m + 1
m += 1
# Cannot use ++ or --
# m++
print(f"Incremented value of m is {m}")


# null in python
# null is None in Python
x = 1
x = None
print(f"The updated value of x is: {x}")

# if statement don't need parantheses or curly braces
x = 1
if x < 2:
    print("Value is less than 2")
elif x > 5:
    print("Value is greater than 5")
else:
    print("Value is in between 2 and 5")


# Parantheses needed for multi-line conditions
# and = &&
# or = ||
t = "abc"
s = True
if (t == "abc" and s):
    print("Welcome to the world")
else:
    print("Bubye")


print("Loops--------------")
# While loops are similar
n = 0
while n < 5:
    print(f"n = {n}")
    n += 1

# Looping from i = 0 to i = 4
for i in range(10,1,-2):
    print(i)

print("Math-----------------")
# Division is decimal by default
print(5 / 2)

# Double slash rounds down
print(5 // 2)


# Most languages round towards 0 but here, negative numbers will round down
print(-3 // 2)


# Type casting - Rounding towards 0
print(int(5/2))


# Modulo operator
print(10 % 3)

# Problem with negative values:
# Here, as we know D - d * q = R
# But here q = ceil of (D/d)
# Ideally q = floor of (D/d)
# Some languages use either of these 2 methods
print(-10 % 3)

# To be consistent with other languages modulo
import math
print(math.fmod(-10,3))


# Using math helpers
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3))

# Max / Min int
float("inf")
float("-inf")

# Python numbers are infinite, so they never overflow
print(math.pow(2, 200))

# This is still less than infinity
print(math.pow(2,200) < float("inf"))


# Arrays/lists
print("Arrays ---------------------------")


arr = [1, 2, 3]
print(arr)

# Can be used as stacks
arr.append(4)
arr.append(5)
arr.append(6)
print(arr)

arr.pop()
print(arr)

arr.insert(1,7)
print(arr)


arr[0] = 0
arr[3] = 0
print(arr)

arrLength = 6
arr = [1] * arrLength
print(arr)

# -1 is not out of bounds 
# it's the last value
arr = [1, 2, 3]
print(arr[-1])
print(arr[-2])


# Sublists - slicing
# Similar to loop ranges, last index is non-inclusive
arr = [1, 2, 3, 4]
print(arr[1:3])
print(arr[0:4])


# Unpacking
a, b, c = [1, 2, 3]
print(f"a: {a}, b: {b}, c: {c}")
# The following produces an error: Too many values to unpack
# p, q = [10, 20, 30]
# print(f"p: {p}, q: {q}")


print("Looping through an array")
nums = [1, 2, 3, 4]

# Looping using just the index
for i in range(len(nums)):
    print(f"Index: {i}")
    print(f"Value: {nums[i]}")

print('---------------')

# Without index
for n in nums:
    print(n)

print('---------------')    

# With index and value
for i, n in enumerate(nums):
    print(f"Index: {i}")
    print(f"Value: {n}")

print('---------------')

print('Looping through multiple arrays simultaneously')

nums1 = [1, 2, 3, 4]
nums2 = ["A", "B", "C", "D"]

for n1, n2 in zip(nums1, nums2):
    print(f"{n1}: {n2}")

print('---------------')

print('Array sorting - ascending')

nums1 = [1, 5, 4, 9, 2, 10]
print(nums1)
nums1.sort()
print(nums1)

print('Array sorting - descending')
nums1 = [1, 5, 4, 9, 2, 10]
print(nums1)
nums1.sort(reverse=True)
print(nums1)

print('Sorting alphabetically - default behaviour')
nums1 = ["bob", "alice", "john", "doe"]
print(nums1)
nums1.sort()
print(nums1)


print('Sorting using length of a string - USing lambda functions')
nums1 = ["bob", "alice", "john", "doe"]
print(nums1)
nums1.sort(key=lambda x: len(x))
print(nums1)


print('---------------')

print('Array reversing')

print(nums1)
nums1.reverse()
print(nums1)

print('---------------')

print('List comprehension')
nums1 = [math.pow(2, i) for i in range(1,5)]
print(nums1)

print('List comprehension - 2D lists')
nums1 = [[math.pow(2, i) for i in range(j,j+5)] for j in range(1,26,5)]
print(nums1)

# Simpler example
nums1 = [[0] * 4 for i in range(4)]
print(nums1)

print('---------------')

print('Strings')
s = "abc"
print(s[0:2])

# Strings are immutable i.e if we edit a string, it creates a new string - this creates a n time operation
s += "def"
print(s)

# Numeric strings can be converted 
print(int("123") + int("456"))

# Numbers can also be converted to strings
print(str(123) + str(123))

print('---------------')

# To get the ASCII value of a character
print(ord("a"))
print(ord("b"))


print('----------------')

strings = ["You", "are", "impeccable"]
print(" ".join(strings))


print('----------------')
print('Queues')

# Queues (Double ended queus)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
print(queue)

queue.pop()
print(queue)


print('----------------')
print('Hash Set')

# Elements in a hash set will be unique
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)
print(mySet)

# List to Set
mySet = set([1, 2, 3])
print(mySet)

# Set comprehension
mySet = {i for i in range(5)}
print(mySet)

print("--------------")
print('Hash Maps')

# HashMap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 99

print(myMap)
print(len(myMap))

myMap["alice"] = 100
print(myMap)

myMap.pop("alice")
print(myMap)

print("alice" in myMap)

myMap = {"alice": 88, "bob": 99}
print(myMap)

# Dict comprehension
myMap = {i: 2*i for i in range(5)}
print(myMap)

# Looping through maps
myMap = {"alice": 88, "bob": 99}
for key in myMap:
    print(key)

for key, value in myMap.items():
    print(key, value)

for value in myMap.values():
    print(value)

print(99 in myMap.values())
print(myMap)
print('alice' in myMap.items())

print('----------------')

# Tuples are like arrays but immutable
tup = (1,2,3)
print(tup)
print(tup[0])
print(tup[1])
print(tup[-1])

# The following will not work as tuples are immutable
# tup[0] = 8

# Tuples can be used as keys for a hash map or hash set
myMap = {(1,2): 5}
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

# Lists are not hashable
# Thus, The following will not work
# myMap[[3,4]] = 5


print('-------------------')
print("Heaps")

# Heaps in Python are minHeaps by default
import heapq

# under the hood, heaps are arrays
print("minHeap")
minHeap = []
heapq.heappush(minHeap, 5)
heapq.heappush(minHeap, 10)
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 7)

while len(minHeap):
    print(heapq.heappop(minHeap))


print("maxHeap")
maxHeap = []
heapq.heappush(maxHeap, -1 * 28)
heapq.heappush(maxHeap, -1 * 4)
heapq.heappush(maxHeap, -1 * 16)
heapq.heappush(maxHeap, -1 * 3)

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap));


print("heapify arrays in a linear fashion")
arr = [2, 1, 8, 4, 4]
heapq.heapify(arr)

while len(arr):
    print(heapq.heappop(arr))


print("---------------------")
print('Functions')

def getSum(a, b):
    return a + b

print(getSum(2,358))


# Nested Functions
def outerFunc(a,b):
    c = "c"

    def inner():
        return a + b + c
    
    return inner()

print(outerFunc("a", "b"))


# Another example
def double(arr,val):
    def helper():
        for i,n in enumerate(arr):
            arr[i] *= 2
        
        # We can't execute the following as it is essentially val = val * 2. This means that we need to assign tha value of val multiplied by 2 to a local variable, val. But we do not know the value of val to multiply it by 2. 
        # val *= 2 
        
        # The following nonlocal keyword ensures that the current val is the parent's variable
        nonlocal val
        val *= 2
    
    helper()
    print(arr,val)

nums = [1, 2]
val = 3
double(nums, val)


# Classes
class MyClass:
    def __init__(self,nums):
        self.nums = nums
        self.length = len(nums)

    def getLength(self):
        return self.length

    def getDoubleLength(self):
        return 2 * self.getLength()
