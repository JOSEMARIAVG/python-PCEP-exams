#------------------------------------------------------------------------------------------------------
# QUESTION 1

list = [False, True, "2", 3, 4, 5]
# -> Insert Code Here
print(b)

# Options:
b = 0 not in list #1
b = list[0] #2
b = 0 in list #3 
b = False #4

# CORRECT OPTION: 3 - 0 considered as False. And False option is present in list

#------------------------------------------------------------------------------------------------------
# QUESTION 2
# Assuming that the tuple is a correctly created tuple, the fact that tuples are immutable means that the following instruction:

my_tuple[1] = my_tuple[1] + my_tuple[0]

# Options:
Is illegal #1
May be illegal if the tuple contains strings #2
Can be executed if and only if the tuple contains at least two elements #3
Is fully correct #4

# CORRECT OPTION: 3 - tuples are immutable, which means you cannot change their elements after creation

#------------------------------------------------------------------------------------------------------
# QUESTION 3
# What is the expected output of the following code?

x = [0,1,2]
x.insert(0,1)
del x[1]
print(sum(x))

# Options:
2  #1
4  #2
5  #3
3  #4

# CORRECT OPTION: 2 - Insert(index,value)

#------------------------------------------------------------------------------------------------------
# QUESTION 4
# What is the expected output of the following code?

list1 = [1,3]
list2 = list1
list1[0] = 4
print(list2)

# Options:
[1,3]  #1
[1,4]  #2
[4,3]  #3
[1,3,4]  #4

# CORRECT OPTION: 3 - list2 refers to the same list as list1

#------------------------------------------------------------------------------------------------------
# QUESTION 5
# What is the expected output of the following code?

data = ['Peter', 404, 4.03, 'Wellert', 33.3]
print(data[1:3])

# Options:
['Peter', 404, 3.03, 'Wellert', 33.3] #1
None of the above #2
[404, 3.03]  #3
['Peter', 'Wellert']  #4

# CORRECT OPTION: 3 - Arrays (or lists) in Python start at index 0.
# The slice [1:3] means: start at index 1 and stop before index 3 (index 3 is not included).

#------------------------------------------------------------------------------------------------------
# QUESTION 6
# Take a look at the snippet and choose the true statements (Choose two)

nums = [1, 2, 3]
vals = nums
del vals[1:2]

# Options:
nums is longer than vals  #1
nums and vals are of the same length  #2
vals is longer than nums  #3
nums and vals refer to the same list  #4

# CORRECT OPTION: 2, 4 - They refer to the same list, therefore both have the same length.

#------------------------------------------------------------------------------------------------------
# QUESTION 7
# What is the ouput of the following snippet?

dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)
for x in dct.keys():
  print(dct[x][1], end = '')

# Options:
12  #1
(2,1)  #2
(1,2)  #3
21  #4

# CORRECT OPTION: 4 - When we use end = '', print does not add a newline character (\n) after each output.

#------------------------------------------------------------------------------------------------------
# QUESTION 8
# What is the expected output of the following code?

print(list('hello'))

# Options:
hello  #1
[h,e,l,l,o]  #2
['h','e','l','l','o']  #3
None of the above  #4

# CORRECT OPTION: 3 - The list() function takes any iterable object and creates a list containing each of its elements.

#------------------------------------------------------------------------------------------------------
# QUESTION 9
# What will be the output of the following code snippet?

a = [1,2,3,4,5,6,7,8,9]
print(a[::2])
# Options:
[1,3,5,7,9]  #1
[8,9]  #2
[1,2,3]  #3
[1,2]  #4

# CORRECT OPTION: 1 - # CORRECT OPTION: 1 - The slice [::2] (list[start:end:step]) selects every second element from the list, starting from index 0.

#------------------------------------------------------------------------------------------------------
# QUESTION 10
# What will be the output of the following code snippet?

d = {}
d[1] = 1
d['1'] = 2
d[1] += 1

sum = 0

for k in d:
  sum += d[k]

print(sum)

# Options:
3  #1
2  #2
4  #3
1  #4

# CORRECT OPTION: 4 

#------------------------------------------------------------------------------------------------------
# QUESTION 11
# What is the output of the following snippet?

dictionary = {'one': 'two','three':'one','two':'three'}
v = dictionary['one']

for k in range(len(dictionary)):
  v = dictionary[v]

print(v)

# Options:
two  #1
one  #2
('one','two','three')  #3
three  #4

# CORRECT OPTION: 1 - The variable v changes in each loop iteration following the dictionary values,
# and after 3 iterations it returns to 'two'.

#------------------------------------------------------------------------------------------------------
# QUESTION 12
# What os the expected output of the following code?

nums = [3, 4, 5, 20, 5, 25, 1, 3]
nums.pop(1)
print(nums)

# Options:
[3, 1, 25, 5, 20, 5, 4]  #1
[1, 3, 4, 5, 20, 5, 25]  #2
[3, 5, 20, 5, 25, 1, 3]  #3
[1, 3, 3, 4, 5, 5, 20, 25]  #4
[3, 4, 5, 20, 5, 25, 1, 3]  #5

# CORRECT OPTION: 3 - The pop() function removes an item at a given position (index) in the list and returns the item that was removed

#------------------------------------------------------------------------------------------------------
# QUESTION 13
# Which of the following sentences is true?

str1= 'Peter'
str2= str1[:]

# Options:
str1 and str2 are different (but equal) strings  #1
str1 and str2 are different names of the same strings  #2
str1 is longer than str2  #3
str2 is longer than str1  #4

# CORRECT OPTION: 1 - Create a copy of str1. str2 is a new string with the same content but a different object

#------------------------------------------------------------------------------------------------------
# QUESTION 14
# The fact that tuples belong to sequence types means:

# Options:
they can be modified using the del instruction  #1 You can't delete an element of a tuple because tuples are immutable.
they can be extended using the .append() method  #2 Tuples are immutable, so they can't be modified after being created.
they are actually lists  #3 Tuples are immutable, whereas lists are not.
they can be indexed and sliced like lists  #4 Same as 3 answer

# CORRECT OPTION: 4

#------------------------------------------------------------------------------------------------------
# QUESTION 15
# What is the output of the following code?

my_list = [3,1,-1]
my_list[-1] = my_list[-2]
print(my_list)

# Options:
[1,1,1]  #1
[3,-1,1]  #2
[3,1,1]  #3

# CORRECT OPTION: 3 - The index [-1] accesses the last item, and [-2] accesses the second-to-last item. 
# Therefore, the last element is replaced by the value of the second-to-last element

#------------------------------------------------------------------------------------------------------
# QUESTION 16
# What is the expected output of the following code?

data= ((1,2),) * 7
print(len(data[3:8]))

# Options:
6  #1
5  #2
4  #3

# CORRECT OPTION: 3 - Slicing includes the start index but excludes the end index.
# Python does not raise an error if the end index is out of range. 
# So data[3:8] has 4 elements.

#------------------------------------------------------------------------------------------------------
# QUESTION 17
# What is the expected output of the following code?

data = {'Peter': 30, 'Paul': 31}
print(list(data.keys()))

# Options:
('Peter': 30, 'Paul': 31)  #1
('Peter', 'Paul')  #2
['Peter': 30, 'Paul': 31]  #3
['Peter', 'Paul']  #4

# CORRECT OPTION: 4 - data.keys() returns all the keys of the dictionary. 
# Wrapping it with list() converts the keys into a list.

#------------------------------------------------------------------------------------------------------
# QUESTION 18
# What is the output of the following snippet?

tup = (1,) + (1,)
tup = tup + tup
print (len(tup))

# Options:
2  #1
4  #2
The snippet is erroneous (invalid syntax)  #3

# CORRECT OPTION: 2 - Tuples are immutable, but here a new tuple is created and reassigned each time, so no syntax error occurs.

#------------------------------------------------------------------------------------------------------
# QUESTION 19
# What is the expected output of the following code?

data = (1,2,4,8)
data = data [-2:-1]
data = data[-1]
print(data)

# Options:
(4)  #1
4  #2
(4,)  #3
44  #4

# CORRECT OPTION: 2 - First, slicing [-2:-1] gives a tuple with one element (4,).
# Then accessing [-1] extracts the single value 4 from that tuple

#------------------------------------------------------------------------------------------------------
# QUESTION 20
# What is the output of the following snippet?

my_list = [1,2]

for v in range(2):
  my_list.insert(-1,my_list[v])

print(my_list)

# Options:
[1, 1, 2, 2]  #1
[1, 1, 1, 2]  #2
[1, 2, 1, 2]  #3
[1, 2, 2, 2]  #4

# CORRECT OPTION: 2 - Using insert(-1, ...) adds a new element before the last item in the list.

#------------------------------------------------------------------------------------------------------
# QUESTION 21
# What is the output of the following snippet?

x = [1, 2, 3, 4]
x[1:3] = [9,9]
print(x)

# Options:
[1, 9, 9, 4]  #1
[9, 9, 3, 4]  #2
[1, 2, 3, 4]  #3
Error  #4

# CORRECT OPTION: 1 - Slicing assignment replaces the selected elements with the new values.

#------------------------------------------------------------------------------------------------------
# QUESTION 22
# What is the output of the following snippet?

a = [1,2,3]
b = a
b = b + [4]
print(a)

# Options:
[1,2,3]  #1
[1,2,3,4]  #2
[4]  #3
Error  #4

# CORRECT OPTION: 1 - a is unchanged because b + [4] creates a new list; a still points to the original list.

#------------------------------------------------------------------------------------------------------
# QUESTION 23
# What is the output of the following snippet?

t = (1, 2)
t += (3,)
print(t)

# Options:
(1, 2)  #1
(1, 2, 3)  #2
(3,)  #3
Error  #4

# CORRECT OPTION: 2 - Concatenation creates a new tuple which is reassigned to t.

#------------------------------------------------------------------------------------------------------
# QUESTION 24
# What is the output of the following snippet?

my_list = [1,2,3,4]
print(my_list[::3])

# Options:
[1,2]  #1
[1,4]  #2
[1,3]  #3
[3,4]  #4

# CORRECT OPTION: 2 - Step 3 in slicing takes every third element, starting from index 0.

#------------------------------------------------------------------------------------------------------
# QUESTION 25
# What is the output of the following snippet?

d = {'a':1, 'b':2, 'c':3}
print(d.get('d', 4))

# Options:
1  #1
4  #2
None  #3
Error  #4

# CORRECT OPTION: 2 - get() returns the default value if the key is not present.

#------------------------------------------------------------------------------------------------------
# QUESTION 26
# What is the output of the following snippet?

x = [1,2,3]
x.append([4,5])
print(len(x))

# Options:
3  #1
4  #2
5  #3
2  #4

# CORRECT OPTION: 2 - append() adds a single new element (a list) at the end, so length becomes 4.

#------------------------------------------------------------------------------------------------------
# QUESTION 27
# What is the output of the following snippet?

x = [1,2,3,4]
x.insert(2, 9)
print(x)

# Options:
[1,2,9,3,4]  #1
[1,9,2,3,4]  #2
[9,1,2,3,4]  #3
[1,2,3,4,9]  #4

# CORRECT OPTION: 1 - insert(index, value) adds the value at the specified index, shifting the rest to the right.

#------------------------------------------------------------------------------------------------------
# QUESTION 28
# What is the output of the following snippet?

x = [1,2,3]
y = x[:]
y[0] = 9
print(x)

# Options:
[9,2,3]  #1
[1,2,3]  #2
[9,1,2,3]  #3
Error  #4

# CORRECT OPTION: 2 - x[:] creates a new copy; modifying y does not affect x.

#------------------------------------------------------------------------------------------------------
# QUESTION 29
# What is the output of the following snippet?

x = [1,2,3,4]
print(x[-3:-1])

# Options:
[1,2]  #1
[2,3]  #2
[3,4]  #3
[2,3,4]  #4

# CORRECT OPTION: 2 - Slicing from -3 to -1 includes indices 1 and 2 → [2,3].

#------------------------------------------------------------------------------------------------------
# QUESTION 30
# What is the output of the following snippet?

x = "Python"
print(x[:3])

# Options:
"Pyt"  #1
"tho"  #2
"on"  #3
"Python"  #4

# CORRECT OPTION: 1 - Slicing up to index 3 (exclusive) gives first three characters.

#------------------------------------------------------------------------------------------------------
# QUESTION 31
# What is the output of the following snippet?

x = [1,2]
for v in range(2):
    x.append(x[v])
print(x)

# Options:
[1,2,1,2]  #1
[1,2,2,2]  #2
[1,1,2,2]  #3
[1,2,1,1]  #4

# CORRECT OPTION: 1 - append() adds elements at the end; loop takes x[0]=1 and x[1]=2.

#------------------------------------------------------------------------------------------------------
# QUESTION 32
# What is the output of the following snippet?

x = (1,2,3,4)
print(x[1:5])

# Options:
(2,3,4)  #1
(2,3,4,5)  #2
(1,2,3,4)  #3
Error  #4

# CORRECT OPTION: 1 - Slicing stops at the end if the stop index exceeds length.

#------------------------------------------------------------------------------------------------------
# QUESTION 33
# What is the output of the following snippet?

x = [1,2,3,4]
x[1:3] = []
print(x)

# Options:
[1,4]  #1
[1,2,3,4]  #2
[1,3,4]  #3
[1,2,4]  #4

# CORRECT OPTION: 1 - Assigning an empty list deletes the elements in the slice.

#------------------------------------------------------------------------------------------------------
# QUESTION 34
# What is the output of the following snippet?

x = [1,2,3]
x.extend([4,5])
print(x)

# Options:
[1,2,3,4,5]  #1
[1,2,3,[4,5]]  #2
[4,5,1,2,3]  #3
[1,2,3]  #4

# CORRECT OPTION: 1 - extend() adds elements of the iterable individually at the end.

#------------------------------------------------------------------------------------------------------
# QUESTION 35
# What is the output of the following snippet?

x = [1,2,3,4]
x.remove(3)
print(x)

# Options:
[1,2,3,4]  #1
[1,2,4]  #2
[3,4]  #3
Error  #4

# CORRECT OPTION: 2 - remove(value) deletes the first occurrence of the value.

#------------------------------------------------------------------------------------------------------
# QUESTION 36
# What is the output of the following snippet?

x = [1,2,3,4]
print(x[::-1])

# Options:
[1,2,3,4]  #1
[4,3,2,1]  #2
[2,1,4,3]  #3
[1,3,2,4]  #4

# CORRECT OPTION: 2 - Step -1 reverses the list.

#------------------------------------------------------------------------------------------------------
# QUESTION 37
# What is the output of the following snippet?

x = {"a":1, "b":2}
print(list(x.values()))

# Options:
[1,2]  #1
['a','b']  #2
[('a',1),('b',2)]  #3
Error  #4

# CORRECT OPTION: 1 - values() returns all dictionary values; list() converts them to a list.

#------------------------------------------------------------------------------------------------------
# QUESTION 38
# What is the output of the following snippet?

x = [1,2,3,4]
x *= 2
print(x)

# Options:
[1,2,3,4]  #1
[1,2,3,4,1,2,3,4]  #2
[2,4,6,8]  #3
Error  #4

# CORRECT OPTION: 2 - Multiplying a list by 2 repeats its elements.

#------------------------------------------------------------------------------------------------------
# QUESTION 39
# What is the output of the following snippet?

x = [1,2,3]
print(x.index(2))

# Options:
1  #1
2  #2
0  #3
Error  #4

# CORRECT OPTION: 1 - index(value) returns the first index of the specified value.

#------------------------------------------------------------------------------------------------------
# QUESTION 40
# What is the output of the following snippet?

x = [1,2,3,4]
print(x.count(2))

# Options:
1  #1
2  #2
0  #3
Error  #4

# CORRECT OPTION: 1 - count(value) returns the number of occurrences of the value in the list.

#------------------------------------------------------------------------------------------------------
# QUESTION 41
# What is the output of the following snippet?

x = [1,2,3]
y = [i**2 for i in x if i%2==1]
print(y)

# Options:
[1,4,9]  #1
[1,9]  #2
[4]  #3
[2]  #4

# CORRECT OPTION: 2 - List comprehension squares only the odd numbers (1 and 3).

#------------------------------------------------------------------------------------------------------
# QUESTION 42
# What is the output of the following snippet?

a = (1,2,3)
b = a * 2
print(b)

# Options:
(1,2,3)  #1
(1,2,3,1,2,3)  #2
(2,4,6)  #3
Error  #4

# CORRECT OPTION: 2 - Tuples can be multiplied to repeat elements.

#------------------------------------------------------------------------------------------------------
# QUESTION 43
# What is the output of the following snippet?

x = {"a":1,"b":2,"c":3}
x["d"] = x.get("b") + x.get("c")
print(x)

# Options:
{'a':1,'b':2,'c':3,'d':5}  #1
{'a':1,'b':2,'c':3,'d':6}  #2
{'a':1,'b':2,'c':3}  #3
Error  #4

# CORRECT OPTION: 1 - 'd' is added as the sum of 'b' and 'c'.

#------------------------------------------------------------------------------------------------------
# QUESTION 44
# What is the output of the following snippet?

x = [1,2,3,4]
print(x[::-2])

# Options:
[4,2]  #1
[4,3,2,1]  #2
[4,2,0]  #3
[3,1]  #4

# CORRECT OPTION: 1 - Step -2 slices the list in reverse, taking every second element.

#------------------------------------------------------------------------------------------------------
# QUESTION 45
# What is the output of the following snippet?

x = [1,2,3]
x.insert(len(x), 4)
print(x)

# Options:
[1,2,3,4]  #1
[4,1,2,3]  #2
[1,4,2,3]  #3
Error  #4

# CORRECT OPTION: 1 - Inserting at len(x) appends at the end.

#------------------------------------------------------------------------------------------------------
# QUESTION 46
# What is the output of the following snippet?

x = [1,2,3]
y = x
y *= 2
print(x)

# Options:
[1,2,3]  #1
[1,2,3,1,2,3]  #2
[2,4,6]  #3
Error  #4

# CORRECT OPTION: 2 - *= modifies the list in place; x and y point to the same object.

#------------------------------------------------------------------------------------------------------
# QUESTION 47
# What is the output of the following snippet?

x = [1,2,3]
y = x.copy()
y[0] = 9
print(x)

# Options:
[9,2,3]  #1
[1,2,3]  #2
[9,1,2,3]  #3
Error  #4

# CORRECT OPTION: 2 - copy() creates a shallow copy; modifying y does not affect x.

#------------------------------------------------------------------------------------------------------
# QUESTION 48
# What is the output of the following snippet?

x = [1,2,3,4]
print(x[1:4:2])

# Options:
[2,4]  #1
[2,3]  #2
[1,3]  #3
[3,4]  #4

# CORRECT OPTION: 1 - Slice from index 1 to 4 with step 2 → [2,4].

#------------------------------------------------------------------------------------------------------
# QUESTION 49
# What is the output of the following snippet?

x = [1,2,3,4]
x[1:3] = [9,9,9]
print(x)

# Options:
[1,9,9,9,4]  #1
[1,9,9,4]  #2
[9,9,9,4]  #3
Error  #4

# CORRECT OPTION: 1 - Slice assignment replaces the selected elements; extra elements are inserted.

#------------------------------------------------------------------------------------------------------
# QUESTION 50
# What is the output of the following snippet?

x = {'a':1,'b':2}
y = {'b':3,'c':4}
x.update(y)
print(x)

# Options:
{'a':1,'b':2,'c':4}  #1
{'a':1,'b':3,'c':4}  #2
{'b':3,'c':4}  #3
Error  #4

# CORRECT OPTION: 2 - update() replaces existing keys and adds new ones.

#------------------------------------------------------------------------------------------------------
# QUESTION 51
# What is the output of the following snippet?

x = [1,2,3,4]
print([i*2 for i in x if i%2==0])

# Options:
[2,4]  #1
[4,8]  #2
[1,3]  #3
[2,4,6,8]  #4

# CORRECT OPTION: 2 - Comprehension doubles only the even numbers (2 and 4).

#------------------------------------------------------------------------------------------------------
# QUESTION 52
# What is the output of the following snippet?

x = (1,2,3)
print(x[-1::-1])

# Options:
(3,2,1)  #1
(1,2,3)  #2
(3,1,2)  #3
Error  #4

# CORRECT OPTION: 1 - Step -1 reverses the tuple.

#------------------------------------------------------------------------------------------------------
# QUESTION 53
# What is the output of the following snippet?

x = [1,2,3,4]
y = x.pop(1)
print(x, y)

# Options:
([1,3,4],2)  #1
([1,2,3,4],2)  #2
([1,3,4],1)  #3
([2,3,4],1)  #4

# CORRECT OPTION: 1 - pop(index) removes and returns the element at index 1.

#------------------------------------------------------------------------------------------------------
# QUESTION 54
# What is the output of the following snippet?

x = [1,2,3]
x[1:2] = []
print(x)

# Options:
[1,3]  #1
[1,2,3]  #2
[2,3]  #3
Error  #4

# CORRECT OPTION: 1 - Assigning an empty list deletes the elements in the slice.

#------------------------------------------------------------------------------------------------------
# QUESTION 55
# What is the output of the following snippet?

x = [1,2,3,4]
x.remove(3)
print(x)

# Options:
[1,2,3,4]  #1
[1,2,4]  #2
[3,4]  #3
Error  #4

# CORRECT OPTION: 2 - remove(value) deletes the first occurrence of the value.

#------------------------------------------------------------------------------------------------------
# QUESTION 56
# What is the output of the following snippet?

x = {1,2,3,2,1}
print(len(x))

# Options:
5  #1
3  #2
4  #3
Error  #4

# CORRECT OPTION: 2 - Sets remove duplicates automatically; length is 3.

#------------------------------------------------------------------------------------------------------
# QUESTION 57
# What is the output of the following snippet?

x = [1,2,3]
print(sum([i*2 for i in x]))

# Options:
12  #1
6  #2
9  #3
10  #4

# CORRECT OPTION: 1 - Each element is doubled → [2,4,6]; sum = 12.

#------------------------------------------------------------------------------------------------------
# QUESTION 58
# What is the output of the following snippet?

x = [1,2,3,4]
print(list(filter(lambda i:i%2==0,x)))

# Options:
[2,4]  #1
[1,3]  #2
[1,2,3,4]  #3
[2]  #4

# CORRECT OPTION: 1 - filter keeps only the even numbers.

#------------------------------------------------------------------------------------------------------
# QUESTION 59
# What is the output of the following snippet?

x = [1,2,3]
y = [i**2 for i in x]
print(y)

# Options:
[1,2,3]  #1
[1,4,9]  #2
[2,4,6]  #3
[1,1,1]  #4

# CORRECT OPTION: 2 - Each element is squared in the comprehension.

#------------------------------------------------------------------------------------------------------
# QUESTION 60
# What is the output of the following snippet?

x = [1,2,3,4]
print([i for i in x if i not in (2,3)])

# Options:
[1,4]  #1
[2,3]  #2
[1,2,3,4]  #3
[4]  #4

# CORRECT OPTION: 1 - Comprehension filters out elements 2 and 3.

#------------------------------------------------------------------------------------------------------
# QUESTION 61
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3,4])
print(arr[1:3])

# Options:
[2,3]  #1
[1,2]  #2
[3,4]  #3
[1,2,3,4]  #4

# CORRECT OPTION: 1 - Slicing a NumPy array works like Python lists, start included, stop excluded.

#------------------------------------------------------------------------------------------------------
# QUESTION 62
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3,4])
print(arr[[0,2]])

# Options:
[1,3]  #1
[1,2]  #2
[2,4]  #3
[1,2,3,4]  #4

# CORRECT OPTION: 1 - Fancy indexing returns elements at positions 0 and 2.

#------------------------------------------------------------------------------------------------------
# QUESTION 63
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2], "B":[3,4]})
print(df["B"])

# Options:
0 3
1 4  #1
[3,4]  #2
{'B':[3,4]}  #3
Error  #4

# CORRECT OPTION: 1 - df["B"] returns a Series with the column values.

#------------------------------------------------------------------------------------------------------
# QUESTION 64
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
print(df.iloc[1,1])

# Options:
5  #1
2  #2
4  #3
Error  #4

# CORRECT OPTION: 1 - iloc[1,1] accesses row 1, column 1 (0-based).

#------------------------------------------------------------------------------------------------------
# QUESTION 65
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3,4])
arr[arr%2==0] = 0
print(arr)

# Options:
[1,0,3,0]  #1
[0,0,0,0]  #2
[1,2,3,4]  #3
[2,4]  #4

# CORRECT OPTION: 1 - Boolean indexing replaces even numbers with 0.

#------------------------------------------------------------------------------------------------------
# QUESTION 66
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
print(df[df["A"]>1])

# Options:
   A  B
1  2  5
2  3  6  #1
[2,3]  #2
Error  #3
   A  B
0  1  4  #4

# CORRECT OPTION: 1 - Boolean indexing selects rows where A>1.

#------------------------------------------------------------------------------------------------------
# QUESTION 67
# What is the output of the following snippet?

import numpy as np
arr = np.array([[1,2],[3,4]])
print(arr.shape)

# Options:
(2,2)  #1
[2,2]  #2
(4,)  #3
Error  #4

# CORRECT OPTION: 1 - The shape of a 2x2 array is (2,2).

#------------------------------------------------------------------------------------------------------
# QUESTION 68
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3,4])
print(arr.sum())

# Options:
10  #1
4  #2
[1,2,3,4]  #3
Error  #4

# CORRECT OPTION: 1 - sum() returns the sum of all elements in the array.

#------------------------------------------------------------------------------------------------------
# QUESTION 69
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
print(df["A"]+df["B"])

# Options:
0 5
1 7
2 9  #1
0 5
1 7
2 9  #2
[5,7,9]  #3
Error  #4

# CORRECT OPTION: 3 - Adding two Series adds element-wise → [5,7,9].

#------------------------------------------------------------------------------------------------------
# QUESTION 70
# What is the output of the following snippet?

import numpy as np
arr = np.arange(5)
print(arr[::2])

# Options:
[0,2,4]  #1
[1,3,5]  #2
[0,1,2,3,4]  #3
[2,4]  #4

# CORRECT OPTION: 1 - Step 2 slicing returns every second element.

#------------------------------------------------------------------------------------------------------
# QUESTION 71
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
print(df.iloc[:,1])

# Options:
0 4
1 5
2 6  #1
[4,5,6]  #2
Error  #3
0 4
1 5
2 6  #4

# CORRECT OPTION: 2 - iloc[:,1] selects all rows in column 1 as a Series → [4,5,6].

#------------------------------------------------------------------------------------------------------
# QUESTION 72
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3,4])
print(arr*2)

# Options:
[2,4,6,8]  #1
[1,4,9,16]  #2
[1,2,3,4]  #3
Error  #4

# CORRECT OPTION: 1 - NumPy arrays support element-wise operations.

#------------------------------------------------------------------------------------------------------
# QUESTION 73
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
print(df[df["B"]%2==0])

# Options:
   A  B
0  1  4
1  2  5
2  3  6  #1
   A  B
0  1  4
2  3  6  #2
   A  B
1  2  5  #3
Error  #4

# CORRECT OPTION: 2 - Boolean indexing selects rows where B%2==0 → rows 0 and 2.

#------------------------------------------------------------------------------------------------------
# QUESTION 74
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3])
print(arr.shape, arr.ndim)

# Options:
(3,) 1  #1
(3,1) 2  #2
(1,3) 2  #3
(3,) 2  #4

# CORRECT OPTION: 1 - 1D array has shape (3,) and ndim=1.

#------------------------------------------------------------------------------------------------------
# QUESTION 75
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,3]})
print(df.iloc[1:3])

# Options:
   A
1  2
2  3  #1
[2,3]  #2
   A
0  1
1  2  #3
Error  #4

# CORRECT OPTION: 1 - iloc[1:3] selects rows 1 and 2.

#------------------------------------------------------------------------------------------------------
# QUESTION 76
# What is the output of the following snippet?

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
print(arr[:,1])

# Options:
[2,5]  #1
[1,4]  #2
[2,5,3,6]  #3
Error  #4

# CORRECT OPTION: 1 - arr[:,1] selects all rows in column 1.

#------------------------------------------------------------------------------------------------------
# QUESTION 77
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,3], "B":[4,5,6]})
print(df.sum(axis=0))

# Options:
A 6
B 15  #1
A 3
B 4  #2
[6,15]  #3
Error  #4

# CORRECT OPTION: 1 - sum(axis=0) sums column-wise.

#------------------------------------------------------------------------------------------------------
# QUESTION 78
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3,4])
print(np.where(arr%2==0, 10, arr))

# Options:
[1,10,3,10]  #1
[2,4,6,8]  #2
[10,10,10,10]  #3
[1,2,3,4]  #4

# CORRECT OPTION: 1 - np.where replaces even numbers with 10, odd numbers stay.

#------------------------------------------------------------------------------------------------------
# QUESTION 79
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
print(df.describe().loc["mean","B"])

# Options:
5  #1
4  #2
6  #3
Error  #4

# CORRECT OPTION: 1 - describe() gives statistics; loc["mean","B"] accesses mean of column B.

#------------------------------------------------------------------------------------------------------
# QUESTION 80
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3])
print(arr.astype(float))

# Options:
[1.0,2.0,3.0]  #1
[1,2,3]  #2
[1.0,2,0]  #3
Error  #4

# CORRECT OPTION: 1 - astype(float) converts integers to floats.

#------------------------------------------------------------------------------------------------------
# QUESTION 81
# What is the output of the following snippet?

def func(x=[]):
    x.append(1)
    return x

print(func())
print(func())

# Options:
[1] [1]  #1
[1] [1,1]  #2
[1,1] [1,1]  #3
Error  #4

# CORRECT OPTION: 2 - Default mutable arguments retain changes between calls.

#------------------------------------------------------------------------------------------------------
# QUESTION 82
# What is the output of the following snippet?

x = [1,2,[3,4]]
y = x.copy()
y[2][0] = 9
print(x)

# Options:
[1,2,[3,4]]  #1
[1,2,[9,4]]  #2
[1,2,[9,9]]  #3
Error  #4

# CORRECT OPTION: 2 - copy() is shallow; modifying nested list affects original.

#------------------------------------------------------------------------------------------------------
# QUESTION 83
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3])
print(arr.mean())

# Options:
2.0  #1
1.5  #2
3  #3
Error  #4

# CORRECT OPTION: 1 - mean() computes the average of the array elements.

#------------------------------------------------------------------------------------------------------
# QUESTION 84
# What is the output of the following snippet?

x = [1,2,3,4]
print([i for i in x if i**2 > 4])

# Options:
[3,4]  #1
[2,3,4]  #2
[1,2]  #3
[4]  #4

# CORRECT OPTION: 2 - List comprehension filters elements whose square > 4.

#------------------------------------------------------------------------------------------------------
# QUESTION 85
# What is the output of the following snippet?

nested = [[1,2],[3,4],[5,6]]
flat = [i for sub in nested for i in sub]
print(flat)

# Options:
[[1,2],[3,4],[5,6]]  #1
[1,2,3,4,5,6]  #2
[1,3,5]  #3
[2,4,6]  #4

# CORRECT OPTION: 2 - Nested list comprehension flattens the list.

#------------------------------------------------------------------------------------------------------
# QUESTION 86
# What is the output of the following snippet?

d = {k:v**2 for k,v in zip(['a','b','c'], [1,2,3])}
print(d)

# Options:
{'a':1,'b':2,'c':3}  #1
{'a':1,'b':4,'c':9}  #2
{'a':1,'b':1,'c':1}  #3
Error  #4

# CORRECT OPTION: 2 - Dictionary comprehension squares the values.

#------------------------------------------------------------------------------------------------------
# QUESTION 87
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,2],"B":[10,20,30]})
print(df.groupby("A").sum())

# Options:
    B
A       
1  10
2  50  #1
    B
A       
1  10
2  20  #2
Error  #3
    B
A       
0  10
1  50  #4

# CORRECT OPTION: 1 - groupby("A").sum() sums values of B for each unique A.

#------------------------------------------------------------------------------------------------------
# QUESTION 88
# What is the output of the following snippet?

import numpy as np
arr = np.arange(1,10).reshape(3,3)
print(arr[1:,1:])

# Options:
[[5,6],[8,9]]  #1
[[4,5],[7,8]]  #2
[[2,3],[5,6]]  #3
Error  #4

# CORRECT OPTION: 1 - Slicing 2D NumPy arrays selects rows and columns.

#------------------------------------------------------------------------------------------------------
# QUESTION 89
# What is the output of the following snippet?

def f(a, b=[]):
    b.append(a)
    return b

print(f(1))
print(f(2))

# Options:
[1] [2]  #1
[1] [1,2]  #2
[1,2] [1,2]  #3
Error  #4

# CORRECT OPTION: 2 - Default mutable list retains previous values.

#------------------------------------------------------------------------------------------------------
# QUESTION 90
# What is the output of the following snippet?

x = [[0]*3]*3
x[0][0] = 1
print(x)

# Options:
[[1,0,0],[0,0,0],[0,0,0]]  #1
[[1,0,0],[1,0,0],[1,0,0]]  #2
[[0,0,0],[0,0,0],[0,0,0]]  #3
Error  #4

# CORRECT OPTION: 2 - Multiplying lists replicates references; changing one affects all rows.

#------------------------------------------------------------------------------------------------------
# QUESTION 91
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
print(df.iloc[[0,2],[1,0]])

# Options:
   B  A
0  4  1
2  6  3  #1
   A  B
0  1  4
2  3  6  #2
Error  #3
   B  A
1  5  2
2  6  3  #4

# CORRECT OPTION: 1 - iloc allows selecting specific rows and columns by position.

#------------------------------------------------------------------------------------------------------
# QUESTION 92
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3,4])
arr2 = arr[arr>2]
print(arr2)

# Options:
[3,4]  #1
[1,2]  #2
[2,3,4]  #3
Error  #4

# CORRECT OPTION: 1 - Boolean indexing selects elements greater than 2.

#------------------------------------------------------------------------------------------------------
# QUESTION 93
# What is the output of the following snippet?

x = [1,2,3]
y = x
y += [4,5]
print(x)

# Options:
[1,2,3]  #1
[1,2,3,4,5]  #2
[4,5]  #3
Error  #4

# CORRECT OPTION: 2 - += modifies the list in place; x and y reference the same object.

#------------------------------------------------------------------------------------------------------
# QUESTION 94
# What is the output of the following snippet?

x = [[1,2],[3,4]]
print([sum(i) for i in x])

# Options:
[3,7]  #1
[1,2,3,4]  #2
[1,2]  #3
Error  #4

# CORRECT OPTION: 1 - List comprehension sums each sublist.

#------------------------------------------------------------------------------------------------------
# QUESTION 95
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,3,2],"B":[10,20,30,40]})
print(df.groupby("A")["B"].mean())

# Options:
A
1  10.0
2  30.0
3  30.0  #1
A
1  10.0
2  30.0  #2
A
1  10
2  30
3  30  #3
Error  #4

# CORRECT OPTION: 2 - groupby with column selection computes mean per group.

#------------------------------------------------------------------------------------------------------
# QUESTION 96
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3,4])
print(np.cumsum(arr))

# Options:
[1,3,6,10]  #1
[1,2,3,4]  #2
[4,6,9,10]  #3
Error  #4

# CORRECT OPTION: 1 - cumsum computes cumulative sum.

#------------------------------------------------------------------------------------------------------
# QUESTION 97
# What is the output of the following snippet?

x = [[1,2],[3,4],[5,6]]
flat = sum(x, [])
print(flat)

# Options:
[1,2,3,4,5,6]  #1
[[1,2],[3,4],[5,6]]  #2
[1,3,5]  #3
Error  #4

# CORRECT OPTION: 1 - sum() with an empty list flattens nested lists.

#------------------------------------------------------------------------------------------------------
# QUESTION 98
# What is the output of the following snippet?

def f(a,b=5):
    return a*b

print(f(2))
print(f(2,3))

# Options:
10 6  #1
10 5  #2
6 10  #3
Error  #4

# CORRECT OPTION: 1 - Default arguments are used unless explicitly provided.

#------------------------------------------------------------------------------------------------------
# QUESTION 99
# What is the output of the following snippet?

import pandas as pd
df = pd.DataFrame({"A":[1,2,3],"B":[4,5,6]})
print(df.apply(lambda x:x*2))

# Options:
   A  B
0  2  8
1  4  10
2  6  12  #1
   A  B
0  1  4
1  2  5
2  3  6  #2
Error  #3
[2,4,6,8,10,12]  #4

# CORRECT OPTION: 1 - apply with lambda multiplies all elements by 2.

#------------------------------------------------------------------------------------------------------
# QUESTION 100
# What is the output of the following snippet?

import numpy as np
arr = np.array([1,2,3])
print(arr.reshape(3,1))

# Options:
[[1],[2],[3]]  #1
[[1,2,3]]  #2
[1,2,3]  #3
Error  #4

# CORRECT OPTION: 1 - reshape(3,1) converts 1D array into 3x1 column vector.
