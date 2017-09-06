---
layout: post
title:  "A JavaScript Cheat Sheet"
date:   2017-05-20 22:46:38 -0400
categories: python, tutorial
---
This is an abbreviated cheat sheet for JavaScript. If you want an detailed explanation of how everything you see here works including explanations through the eyes of Ruby you can find that [here](https://mikemerin.github.io/JS-through-Ruby/), which I highly recommend.

Note that this is a WIP, will finish Wednesday 9/6

interpolation | structure | type conversions
len | ranges | pop | append
in | while | for | enumerate
map | for..in | lambda | reduce
filter | a[] | sorted | insert
del | remove | callbacks

### String Interpolation
Easily bring objects into a string.

```python
animal = "dog"
name = "Lily"
age = 8

# Type 1
print("{}, the {} year old {}").format(name, age, animal)
#=> "Lily, the 8 year old dog."
print("My {2} {0} is {1} years old. {0} is a very sweet {2}.").format(name, age, animal)
#=> My dog Lily is 8 years old. Lily is a very sweet dog.
print("My {2} {0} is {1:d} years old. {0} is a very {desc} {2}.").format(name, age, animal, desc="silly")
#=> My dog Lily is 8 years old. Lily is a very silly dog.

# Type 2
print "%s, the %d year old %s" % (name, age, animal)
#=> "Lily, the 8 year old dog."

# ways to interpolate with type 2
%s # string, or any type of object that can interpolate as a string instead
%d # integer / digit
 print("%d") % 60 #=> 60
%f # float
 print("%f") % 60 #=> 60.000000
%.<number>f # float out to x digits
 print("%.9f") % 60 #=> 60.000000000
%e # float formatted to exponential
 print("%e") % 60 #=> 6.000000e+01
%g # ingeter formatted to exponential if more than 4 zeroes
 print("%g") % 60 #=> 60
 print("%g") % 600000000 #=> 60e+08
%x # number formatted to hexadecimal
 print("%x") % 60 #=> 3c
%o # number formatted to octal
 print("%o") % 60 #=> 74

# example to use in similar fashion with type 1
print("{0:.5g}").format(1384356) #=> 1.3844e+06
```

### Structure
Whitespace is important, tab after a colon `:` to continue, unindent to move on

```python
x = 5
y = 10
if x < y:
  print "x is smaller than y"
  print "{} - {} = {}".format(y, x, y-x)
else:
  print "x is larger than y"
  print "{} - {} = {}".format(x, y, x-y)

print ("small" if x < y else "large")

class Animal:
  def __init__(self, animal_type, name, age):
    self.animal_type = animal_type
    self.name = name
    self.age = age
  def info(self):
    print "%s, the %d year old %s" % (self.name, self.age, self.animal_type)

class Car
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
  def info(self):
    print "The car is a %d %s %s" % (self.year, self.make, self.model)
```

### Type Conversions

```python
str(150) #=> "150"
int("10") #=> 10
float("10") #=> 10.0
float(10.5) #=> 10.5
```

### Length of an Object

```python
len([1, 2, 3, 4]) #=> 4
len("testing out a string") #=> 20
len({1: "one", 2: "two", 3: "three"}) #=> 3
```

### Ranges
Create arrays from a range of numbers

```python
range(x) #=> go from 0 to x
range(x, y) #=> go from x up until y
range(x, y, z) #=> z is the step, how many in between each number

range(4) #=> [0, 1, 2, 3]
range(1, 5) #=> [1, 2, 3, 4]
range(1, 10, 3) #=> [1, 4, 7] (notice 10's not there, again it's 1 up until 10, not including)
range(-5, 0) #=> [-5, -4, -3, -2, -1]

range(0, -5, -1) #=> [0, -1, -2, -3, -4]
range(1, -10, -3) #=> [1, -2, -5, -8]
range(100, 20, -18) #=> [100, 82, 64, 46, 28]
```

### Push/Append/Pop/Shift/Unshift
Add/remove from beginning/end of an array

```python
# add end
array = [1, 2, 3, 4]
array.append(5) #=> [1, 2, 3, 4, 5]
array = array + [6, 7] #=> [1, 2, 3, 4, 5, 6, 7]

# add beginning
array = [1, 2, 3, 4]
array = [0] + array  #=> [0, 1, 2, 3, 4]
array = [-2, -1] + array #=> [-2, -1, 0, 1, 2, 3, 4]

# remove end
array = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
array.pop() #=> "eight"
array #=> ["one", "two", "three", "four", "five", "six", "seven"]
array.pop(2) #=> "three"
array #=> ["one", "two", "four", "five", "six", "seven"]
array.pop(0) #=> "one"
array #=> ["two", "four", "five", "six", "seven"]

# remove beginning
array = [1, 2, 3, 4, 5]
array = array[1:]
array #=> [2, 3, 4, 5]
```

### in
Test for inclusion

```python
5 in [1, 2, 3, 4, 5] #=> True
7 in [1, 2, 3, 4, 5] #=> False
"t" in "this is a string" #=> True
"is" in "this is a string" #=> True
"e" in "this is a string" #=> False
"t" not in "this is a string" #=> False
```
