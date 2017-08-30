

for
```python
a = [1,2,3,4,5]

for x in a:
  print a*2
```




each with index equivalent
```python
a = ["a","b","c","d","e"]
for i, x in enumerate(a):
  print x + " is at index " + str(i)

''' result:
a is at index 0
b is at index 1
c is at index 2
d is at index 3
e is at index 4
'''
```

map
```python
def double(n):
  return n*2

double(5) #=> 10

a = [1,2,3,4,5]

[n*2 for n in a] #=> [2,4,6,8,10]
map(double, a) #=> [2,4,6,8,10]
```

lambda
```python
a = [1,2,3,4,5]

map(lambda x: x*2, a) #=> [2,4,6,8,10]
```

filter
```python
def even(n):
  return n%2 == 0

even(4) #=> True
even(5) #=> False

a = [1,2,3,4,5]

filter(even, a) #=> [2,4]
```

keys/values
```python
dictionary = {1: "one", 2: "two"}

for key in dictionary:
    print "%s" % key

    #=> 1
    #=> 2

for key in dictionary:
    print "%s" % dictionary[key]

```

slice
```python
# a[low:high:spaces]
a = ["a","b","c","d","e"]
a[1:4] #=> ["b","c","d"]
a[3:] #=> ["d","e"]
a[:3] #=> ["a","b","c"]

a[-1] #=> "e"
a[-2] #=> "d"
a[-2:] #=> ["d","e"]
a[:-2] #=> ["a","b","c"

a[1:4:2] #=> ["b","d"]
a[::2] #=> ["a","c","e"]
a[1::2] #=> ["b","d"]
a[:3:2] #=> ["a","c"]

a[::-1] #=> ["e","d","c","b","a"] (reverse)
```

dup
```python
a = [1,2,3,4,5]
b = a
b #=> [1,2,3,4,5]
a[2] = 9
a #=> [1,2,9,4,5]
b #=> [1,2,9,4,5]

a = [1,2,3,4,5]
b = a[:]
b #=> [1,2,3,4,5]
a[2] = 9
a #=> [1,2,9,4,5]
b #=> [1,2,3,4,5]
```
range
```python
range(4) #=> [0, 1, 2, 3]
range(4, 10) #=> [4, 5, 6, 7, 8, 9]
range(4, 10, 2) #=> [4, 6, 8]
range(0, -10, -3) #=> [0, -3, -6, -9]
```

no need to use procs
```python
def double(n):
  return n*2

def triple(n):
  return n*3

def multi(n, type):
  return type(n)

double(5) #=> 10
triple(5) #=> 15
multi(10, double) #=> 20
```

sort
```python
a = [1, 4, 2, 5, 6, 3, 7]
a2 = ["hello","everyone","how","are","you?"]
d = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

sorted(a) #=> [1, 2, 3, 4, 6, 7]
sorted(a, reverse=True) #=> [7, 6, 4, 3, 2, 1]

sorted(a2)
 #=> ['are', 'everyone', 'hello', 'how', 'you?']
sorted(a2, key=len)
 #=> ['how', 'are', 'you?', 'hello', 'everyone']
sorted(a2, key=len, reverse=True)
 #=> ['everyone', 'hello', 'you?', 'how', 'are']

sorted(d) #=> [1, 2, 3, 4, 5]
#=> sort by value
sorted(d.items(), key=lambda x: x[1])
#=> [(5, 'five'), (4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

class Animal
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

animals = { Animal("dog", 4), Animal("cat", 5), Animal("bat", 3) }
sorted(animals, lambda x: x.breed)
    #=> [<"bat" instance">, <"cat" instance>, <"dog" instance>]
sorted(animals, lambda x: x.age)
    #=> [<"bat" age 3 instance">, <"dog" age 4 instance>, <"cat" age 5 instance>,]

map(lambda x: x.breed, sorted(animal, key=lambda x: x.breed))
    #=> ["bat", "cat", "dog"]
map(lambda x: x.breed, sorted(animal, key=lambda x: x.age))
    #=> ["bat", "dog", "cat"]

```

reduce
```python
a = [1,2,3,4,5]
total = 0

for x in a:
  total += x

reduce(lambda sum, x: sum + x, a)
```
