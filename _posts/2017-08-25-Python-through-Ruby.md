---
layout: post
title:  "Seeing Python Through Ruby-Colored Glasses"
subtitle: "A Python Cheat Sheet"
date:   2017-08-25 19:53:26 -0400
categories: python, ruby, tutorial
---

If you learned how to program in Ruby, you probably noticed there's a large amount of shortcuts available to cut down on typing (while helping keep your code clean), as well as having a straightforward "English-like" syntax. While JS has similar but more labor-intensive similarities, the syntax for Python is a little more abstract (at least at first). The lack of Ruby-like shortcuts in Python are very noticeable, and if like me you learned Ruby first you may not have known what those shortcuts actually do under the hood, so let's dive right in and compare how Ruby and Python handle these shortcuts, iterations, and methods.

I also have a [Javascript through Ruby](https://mikemerin.github.io/JS-through-Ruby/) post in the same fashion as this post if you're interested.

Please note that this is a LARGE post just like the above one, and this is a work in progress. I have noted the WIP line below.

**I'll be going into a lot of detail in this post, if you want an abbreviated Python-only cheat sheet you can find that at https://mikemerin.github.io/Python-Cheat-Sheet/ (once I finish this post), though I would recommend going through this post if you want a better understanding of how everything works.**

I'll assume you know how to iterate in Ruby already, but if not then look at my [first cryptography post](https://mikemerin.github.io/cryptography/) for a detailed explanation.

We'll be going over these loops, iterations, and global methods:

Ruby | Python Equivalent | Description
---|---|---
||**naming**
Array | List | [ 1, 2, 3, 4 ]
Hash | Dictionary | { 1: "one", 2: "two", 3: "three" }
N/A | Tuple | (1, 2, 3) (immutable)
N/A | Set | { 1, 2, 3 } (immutable)
||**string interpolation**
`"#{obj}"` | `"{}".format(obj)` / `"%s" % obj` | inserting objects into a string
||**functions**
`n.to_s` | `str(n)` | converts to string
`"10".to_i` | `int("10")` | converts to Integer 10
`"10".to_f` | `float("10")` | converts to Float 10.0
x.length | len(x) | length of an object (str, list, etc.)
push / << | append | add onto the end of an array
pop(x) | pop(x) | remove from the end of the array (different)
unshift | a = [x] + a | add onto the beginning of an array
shift(x) | pop(0) | remove from the beginning of the array
||**loops**
while / until | while | loops while condition is true
||**iteration**
for | for | iterate over each element, more used in Python
.each.with_index | for & enumerate | same, but also get the index
.map | map | iterate over each element, changes the output
.map.with_index | map | same, but also get the index
||**manipulating methods**
.dup | a[:] | duplicates an object rather than copies
.reduce / .inject | reduce() | combines all elements via an operation
.flatten | TBD | merge multi-dimensional / nested arrays
.compact | TBD | remove `nil` or `null` values from an array
.sort / .sort_by | sorted(a, opt_arg) | sort an array or hash/Object
case; each | if/elif or dict | shorthand multiple `if` statements
.insert | .insert(idx, elem) | add element(s) from array/string
.delete_at | del a[idx:idx2] | remove element(s) from array/string
.delete(e) | .remove(e) | remove element by element
.
||**selecting methods**
.keys | for %s % k | get all keys in a hash
.values | for %s % d[k] | get all values in a hash
.slice | a[l:h:s] | select element(s) from array
||**more functions**
call/procs | no need | function called within a function

# Names of data types
---
Before we begin we'll need to just cover some basic terminology to avoid confusion when talking about Ruby vs. Python. There are a few data types that are the same in both Ruby and Python but have different names:

Ruby | Python
array = list = [1, 2, 3]
hash = dictionary = { 1: "one", 2: "two", 3: "three" }

In addition Python has a few immutable data types:

tuple = (1, 2, 3)
set = { 1, 2, 3 }

While tuples are used in Ruby they don't really have a name. It's basically used when taking in arguments such as `Time.local(2017, 8, 25)`. In Python that would be called a tuple but it's just arguments in Ruby. In order to use sets in Ruby you must `require 'set'` before you can `Set.new [1, 2, 3]`, and een then sets aren't commonly used in Ruby. More explanations of tuples and sets will be for another time, but when we reference things in Python arrays are lists and hashes are dictionaries.

# String Interpolation
---
Ruby and Javascript's only difference when it comes to string interpolation is a pound `#` sign vs. a dollar `$` sign respectively. While Python's quite different and a bit more complex, it lets you do **much** more customization. Here's what I mean, in Ruby you can do something like this:

```ruby
# Ruby
animal = "dog"
name = "Lily"
age = 8

puts "#{name}, the #{age} year old #{animal}."
#=> "Lily, the 8 year old dog."
```

As you can see, whenever you want to interpolate something in your string, if you have double quotes `""` you can wrap your object in `#{this}` to get it working. There are two ways to do this in Python. The first uses `.format`:

```python
# Python
animal = "dog"
name = "Lily"
age = 8

print("{}, the {} year old {}").format(name, age, animal)
#=> "Lily, the 8 year old dog."
```

While using curly brackets are similar, what Python does is go through the string and any time it finds a placeholder `{}` it goes through an argument to format the string accordingly. If we wanted to, we can put numbers in our `{}` brackets to choose which argument to format our strings in, and this will also let us repeatedly use an argument without having to put it into the tuple over and over again.

```python
# Python
animal = "dog"
name = "Lily"
age = 8

print("My {2} {0} is {1} years old. {0} is a very sweet {2}.").format(name, age, animal)
#=> My dog Lily is 8 years old. Lily is a very sweet dog.
```

You can see how this can be useful in very long sentences. There's MUCH more you can do as well, but I'll just cover two quick things:

```python
# Python
animal = "dog"
name = "Lily"
age = 8

print("My {2} {0} is {1:d} years old. {0} is a very {desc} {2}.").format(name, age, animal, desc="silly")
#=> My dog Lily is 8 years old. Lily is a very silly dog.
```

I did two things here: the `{1:d}` denotes that argument as an integer, and the `{desc}` searches for which argument has the name of "desc". Again there's MUCH more we can do but we'll talk about them in another post. For now, while the placeholder `{}` works alright we can do things another way as well that's built off the data types:

```python
# Python
animal = "dog"
name = "Lily"
age = 8

print "%s, the %d year old %s" % (name, age, animal)
#=> "Lily, the 8 year old dog."
```

What Python does is go through the string, and if you put a `%` after the string it will go through the string searching for `%` and match them up to the argument(s) you put after it, matching each argument in order that it appears. You'll also notice I use both `%s` and `%d`, which is for string and integer respectively (I believe the d stands for digit). I can technically use `%s` for all of them since they'll all end up as a string.

Here's some of the ways you can choose to interpolate:

```python
# Python
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
```

Please note that ALL of the above also works with the `{}` format from before, aka `print("{0:.5g}").format(1384356)` would output `1.3844e+06`.

Last up is breaking out of an interpolation. In Ruby if you wanted to use the same type of quote you'd use a slash `\` to break out of the string, aka `"He said \"wow\" that's useful."` and it wouldn't break. In Python you'd simply put a double `%` to put in a percentage sign without breaking the string. For example if I wanted to say "The tank is 50% full" I'd do:

```python
print("The tank is %d%% full.") % 50
#=>  The tank is 50% full.
```

# Structure
---
One of the biggest, and possibly my favorite parts so far about Python is the way the language is structured. In Ruby you need to use `end` after you `do` something or declare something, however you won't see `end` when looking at Python scripts. Why? Python uses whitespace to structure scripts which makes it arguably much easier to read. If you're doing something inside a function, if you end a line with a colon `:`, just add some whitespace on the next line and Python will know you're inside it. Once you return to the left-most side Python will know you're moving on. Here's what I mean:

```ruby
# Ruby
x = 5
y = 10
if x < y
  puts "x is smaller than y"
  puts "#{y} - #{x} = #{y-x}"
else
  puts "x is larger than y"
  puts "#{x} - #{y} = #{x-y}"
end
```

```python
# Python
x = 5
y = 10
if x < y:
  print "x is smaller than y"
  print "{} - {} = {}".format(y, x, y-x)
else:
  print "x is larger than y"
  print "{} - {} = {}".format(x, y, x-y)
```

So there are two things that are different here: the colon after `x < 10` and `else`, and there's no `end`. It doesn't look like much here, but when our programs grow and we have more and more functions or objects then Python looks much, much neater. As far as working towards one liners, Ruby basically simply uses semi-colons `;`, and Python uses those same colons `:` to declare and then and semi-colons `;` to use our scripts:

```ruby
# Ruby
x = 5
y = 10
if x < y; puts "small"; else puts "large" end
# or
puts (if x < y; "small"; else "large" end)
# or the ternary
puts (x < y ? "small" : "large")
```

```python
# Python
x = 5
y = 10
# mainly use this first example when writing code
print ("small" if x < y else "large")
# or a pseudo ternary (not used as much)
print( ("large", "small") [x < y] )
#=> aka print( ("F", "T")[True])
# or the more explicit using a dictionary (however it evaluates both)
print ( {False: "large", True: "small"} [x<y] )
```

Let's take a look at some Object Oriented programming to see what we mean. Don't worry if this is confusing, we're merely taking a look at how the scripts are structured:

```ruby
# Ruby
class Animal

  attr_accessor :animal_type, :name, :age

  def initialize(animal_type, name, age)
    @animal_type = animal_type
    @name = name
    @age = age
  end

  def info
    puts "#{name}, the #{age} year old #{animal_type}"
  end

end

class Car

  attr_accessor :name, :age

  def initialize(make, model, year)
    @make = make
    @model = model
    @year = year
  end

  def info
    puts "The car is a #{year} #{make} #{model}"
  end

end
```

Now we have two classes, and can make a new animal by typing in `my_pet = Animal.new("dog", "Lily", 8)`. Here's how the same thing looks in Python:

```python
# python
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

The use of indenting the whitespace is very neat and makes the code much more readable. You can clearly see the cascade of where one part starts and the next continues. It's very much like a bulleted list. You can make a new animal by typing in `my_pet = Animal("dog", "Lily", 8)`.


# Functions to change data types
---
Ruby has quite a few types of `.to_something` that can change the data types. This section will be short and sweet as it's fairly direct:

Converting to strings:

```ruby
# Ruby
150.to_s #=> "150"
```
```python
# Python
str(150) #=> "150"
```

Converting to an integer:

```ruby
# Ruby
"10".to_i #=> 10
```
```python
# Python
int("10") #=> 10
```

Converting to a float:

```ruby
# Ruby
"10".to_f #=> 10.0
10.to_f #=> 10.0
```
```python
# Python
float("10") #=> 10.0
float(10) #=> 10.0
```

# Length of a string, array/list, or hash/dictionary
---
You've probably noticed by now that Ruby has a lot more emphasis on calling functions on an object via `object.do_something` versus Python calling objects inside a function via `do_something(object)`. This is the same for for the length function:

```ruby
# Ruby
[1, 2, 3, 4].size #=> 4
[1, 2, 3, 4].length #=> 4
"hey everyone".size #=> 12
"hey everyone".length #=> 12
```
```python
# Python
len([1, 2, 3, 4]) #=> 4
len("hey everyone") #=> 12
```

# Modifying an Array
---
While Ruby and JS have the same push/pop/unshift/shift methods for modifying arrays, only Python's `.append` is the exact same as `.push`. Let's quickly go through them and how we can both directly and indirectly handle the same types of functions.

#### Ruby: push / << | Python: append

Ruby's `push` or shovel `<<` operator works the same as Python's `append`, which adds element(s) onto the end of an array.

```ruby
# Ruby
array = [1, 2, 3, 4]
array.push(5) #=> [1, 2, 3, 4, 5]
array.push(6, 7) #=> [1, 2, 3, 4, 5, 6, 7]
array << 8 #=> [1, 2, 3, 4, 5, 6, 7, 8]
```

Unlike `push` though, Python's `append` is much more limited and works more like the shovel operator which can only handle a single argument.

```python
# Python
array = [1, 2, 3, 4]
array.append(5) #=> [1, 2, 3, 4, 5]
array = array + [6, 7] #=> [1, 2, 3, 4, 5, 6, 7]
```

#### Ruby: unshift | Python: a = [x] + a

There's no direct `unshift` in Python, so we have to manually add it together:

```ruby
# Ruby
array = [1, 2, 3, 4]
array.unshift(0) #=> [0, 1, 2, 3, 4]
array.unshift(-2, -1) #=> [-2, -1, 0, 1, 2, 3, 4]
```

```python
# Python
array = [1, 2, 3, 4]
array = [0] + array  #=> [0, 1, 2, 3, 4]
array = [-2, -1] + array #=> [-2, -1, 0, 1, 2, 3, 4]
```

#### Ruby: pop/shift | Python: pop

While Python doesn't have `shift`, it's `pop` method does both jobs here. Why? Pop works differently in Python than it does in Ruby. In both languages, these functions return the removed item(s), not the changed array. But how they remove them is what makes the difference.

In Ruby, both shift and pop can either be called without taking in a number and it'll remove the first or last element respectively.

Here's where the difference lies: in Ruby if you have it take in an argument it will remove x elements from the beginning or the end.

```ruby
# Ruby
array = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
array.pop #=> "eight"
array #=> ["one", "two", "three", "four", "five", "six", "seven"]
array.pop(2) #=> ["six", "seven"]
array = ["one", "two", "three", "four", "five"]

array.shift #=> "one"
array #=> ["two", "three", "four", "five"]
array.shift(2) #=> ["two", "three"]
array #=> ["four", "five"]
```

In Python, if you take in an element it will remove the element at the **index** put in. That means to imitate `shift` we'll simply say "pop at index 0"

```python
# Python
array = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
array.pop() #=> "eight"
array #=> ["one", "two", "three", "four", "five", "six", "seven"]
array.pop(2) #=> "three"
array #=> ["one", "two", "four", "five", "six", "seven"]

array.pop(0) #=> "one"
array #=> ["two", "four", "five", "six", "seven"]
```

However this operation is very slow when talking about Big O notation as operationally it's going through each bit of memory to shift the elements down by one. Instead we can create a new array from index 1 until the end:

```python
# Python
array = [1, 2, 3, 4, 5]
array = array[1:len(array)]
array #=> [2, 3, 4, 5]
```

Right let's quickly cover that as well:

```ruby
# Ruby
array = [1, 2, 3, 4, 5]
array.length #=> 5
array.size #=> 5
"testing out a string".length #=> 20
```

```python
# Python
array = [1, 2, 3, 4, 5]
len(array) #=> 5
len("testing out a string") #=> 20
```

Easy enough.

# While / until
---

Onto loops! Let's start off with the easiest example of the while loop.

```ruby
# Ruby
array = []
x = 1
while x < 6
    array.push(x)
    x += 1
end
array #=> [1,2,3,4,5]
```

```python
# Python
array = []
x = 1
while x < 6:
    array.append(x)
    x += 1

array #=> [1,2,3,4,5]
```

Let's do a side-by-side:

Ruby | Python | Difference
---|---|---
array = [] | array = [] | N/A
x = 1 | x = 1 | N/A
while x < 6 | while x < 6: | Python needs a colon `:` to go to the next line
array.push(x) | array.append(x) | push is append and the lines needs to be indented
x += 1 | x += 1 | same (but indented)
end |  | only Ruby needs `end`, Python just needs to be un-indented
array | array | both #=> [1,2,3,4,5]

They're almost identical, but Python needs the colon `:` to say we're going to use the lines under the original one, and then those lines need to be indented. Once the lines un-indent Python knows that we're done working with the original line. However there are some tricks to doing one line solutions (helpful if combining with other complex scripts):
```ruby
# Ruby
array = []
x = 1
while x < 6; array.push(x); x += 1 end
array #=> [1,2,3,4,5]
```
```python
# Python
array = []
x = 1
while x < 6: a.append(x); x += 1
array #=> [1,2,3,4,5]
```

While in this case our Python script looks a bit cleaner, this is by no means the cleanest way to do this type of operation. There are quite a few ways to shorten this, including a trick using `.reduce` (also known as `.inject` in Ruby only), but I'll cover that later on.

# WORK IN PROGRESS BELOW
---


# Using `for`
---
While `for` isn't used much in Ruby (since `while`, `until`, or other iterations can do much more, are cleaner, and get the job done easier), it's very important in JS. While this is a nice trick in Ruby:
```ruby
# Ruby
array = []
for x in 1..5
    array.push(x)
end
array #=> [1,2,3,4,5]
```
Unfortunately there's no quick way to do a range iterator in Javascript (the `(1..5)` above), ***however*** `for` is still very useful if we use it another way. Remember that while loop from before? Here's how we'd cleanly do it in JS:
```javascript
// Javascript
array = []
for (let x = 1;
    x < 6;
    x++ )
    { array.push(x) }
array #=> [1,2,3,4,5]
```
Or the MUCH cleaner one-liner:
```javascript
// Javascript
array = []
for (let x = 1; x < 6; x++) { array.push(x) }
array //=> [1,2,3,4,5]
```
We basically include what we want our number `x` to do all in one neat place (our parenthesis), and then operate on it within our block. As you'd expect, we can do this with other things too, like iterating over an array!
# iterating with `.each`/`for`/`for..in` then `each`/`forEach`
---
Onto iterations. As I said before, `.each` in Ruby is incredibly useful, and does what both `for` and `.forEach` does in JS. Before we get to the latter, let's flash back to Ruby and cover how we can iterate over an array using `.each` beginning with a more lengthy iteration (similar to JS's `for`) and ending with a shortcut (similar to JS's `.forEach`). These first three examples are the former:
```ruby
# ruby
array = [1,2,3,4,5]
array2 = []

(0...array.length).each { |i| print array[i] }
#=> 12345

(0...array.length).each { |i| array2.push( array[i] ) }
array2 #=> [1,2,3,4,5]

array2 = []
(0...array.length).each { |i| array2.unshift( array[i] ) }
array2 #=> [5,4,3,2,1]
```
Now let's finally do that fancy JS iteration using `for` but this time over an array. To spoof the range we'll set our index to 0, limit it to the array.length, and add up by 1:
```javascript
// Javascript
array = [1,2,3,4,5]
array2 = []

// long version for clarification:

for (let i = 0, l = array.length; // declare i, l as variables
     i < l; // while index is less than the array length
     i++ ) // increment by 1
    { array2.push( array[i] ) }
array2 //=> [1,2,3,4,5]

// shorter and clean version:

for (let i = 0, l = array.length; i < l; i++) { array2.push( array[i] ) }
//=> [1,2,3,4,5]
for (let i = 0, l = array.length; i < l; i++) { array2.unshift( array[i] ) }
//=> [5,4,3,2,1]
```
This is how `.each` directly correlates with `for`, but there's a better way to iterate over an array that inherently **knows** to go from the start to the end of an array without us needing to tell it. Doing this in Ruby:
```ruby
# Ruby
for x in array; puts x end
for x in array; array2.push(x) end
```
In JS we'll introduce `in`:
```javascript
// Javascript
for (let i in array) { console.log( array[i] ) }
for (let i in array) { array2.push( array[i] ) }
```
We're obtaining the index `i` from the `array`, then using it in our code block.

This is as far we can go using `for` in JS. You'll notice that there's a very important difference in how Ruby handles `for` compared to JS: while Ruby calls on the element, JS calls on the index, and we can't grab the element directly, therefore we **still** have to do `array[i]` instead of how we were just using `x` in Ruby above. Time to break out `forEach` and fix that:
```ruby
# Ruby
array.each { |x| puts x }
array.each { |x| array2.push2.push( array[i] ) }
```
```javascript
// Javascript
array.forEach( x => { console.log(x) } )
array.forEach( x => { array2.push(x) } )
```
# Using Ruby's `.each_with_index` or `.each.with_index` in JS
These are the same thing in Ruby, however JS has neither of these functions available. Thankfuly though JS has a way to easily iterate over both the element **and** the index at the **same time**:
```ruby
# Ruby
array = ["Hello", "World"]
array.each_with_index { |x,i| puts "the index is #{i}, the element is #{x}" }
```
```javascript
// Javascript
array.forEach( (x, i) => console.log(`The index is ${i}, the element is ${x}`) )
```
These both print out:

"the index is 0, the element is Hello"

"the index is 1, the element is World" -->


while / until | while | loops while condition is true
||**iteration**
for | for | iterate over each element, more used in Python
.each.with_index | for & enumerate | same, but also get the index
.map | map | iterate over each element, changes the output
.map.with_index | map | same, but also get the index
||**manipulating methods**
.dup |
.reduce / .inject | reduce() | combines all elements via an operation
.flatten | TBD | merge multi-dimensional / nested arrays
.compact | TBD | remove `nil` or `null` values from an array
.sort / .sort_by | sorted(a, opt_arg) | sort an array or hash/Object
case; each | if/elif or dict | shorthand multiple `if` statements
.insert | .insert(idx, elem) | add element(s) from array/string
.delete | del a[idx:idx2] | remove element(s) from array/string
||**selecting methods**
.keys | for %s % k | get all keys in a hash
.values | for %s % d[k] | get all values in a hash
.slice | a[l:h:s] | select element(s) from array
||**more functions**
call/procs | no need | function called within a function


# Iterating and manipulating with - Ruby: `.map`, Python: `map()`
---
Our newfound `.forEach` is great, but there's a problem: what if we want to return a new array without having to perform the arduous task of creating a blank array and then appending it to that array, then having to set it up again each time? In comes `.map` which simply outputs our answer each time we call it! It's used in the same way we use `.forEach`. For example if we have `array = [1,2,3,4,5]` and compare `.each/.forEach` vs. `.map`:
```ruby
# Ruby
array.each { |x| x * 2 } #=> [1,2,3,4,5] unchanged output
array.map { |x| x * 2 } #=> [2,4,6,8,10] changed output
```
```javascript
// Javascript
array.forEach(x => x * 2) //=> undefined (no output)
array.map(x => x) //=> [1,2,3,4,5] unchanged output (technically spoofs the input like Ruby .each)
array.map(x => x * 2) //=> [2,4,6,8,10] changed output
```
`.map` is great for shortening your code and making them one-liners, which cleans up your code and makes it much more readable.
# Using Ruby's `.map.with_index` in JS
Just like with `.each.with_index`, JS has a way to easily iterate over both the element **and** the index at the **same time** and output the value you want:
```ruby
# Ruby
array = [10,20,30,40,50]
array.map.with_index { |x,i| i } #=> [0,1,2,3,4]
array.map.with_index { |x,i| x * i } #=> [0,20,60,120,200]
```
```javascript
// Javascript
array.map((x, i) => i) //=> [0,1,2,3,4]
array.map((x, i) => x * i) //=> [0,20,60,120,200]
```
# Manipulating arrays with `.reduce`
---
Now let's go over what `.reduce` does (also known as `.inject` in ruby) and add up all values in the array, starting with the shortcut then expanding out to see what's under the hood. Note that all of these will produce the correct answer of 15:

```ruby
# ruby
array = [1,2,3,4,5]

array.reduce(:+)
# reduce takes in an addition symbol
# note: (:+) is also a smiley face

array.reduce(0, :+)
# start at 0, then perform the reducing

array.reduce(0) { |sum, x| sum + x }
# what the (:+) is actually doing

sum = 0
array.each { |x| sum += x }
sum #=> 15
# an even more literal example
```
As you can see, what reduce does is:
start at 0 (default), add 1, now sum = 1
start at sum (1), add 2, now sum = 3
start at sum (3), add 3, now sum = 6
etc. until the end.

In JS however, we don't have these shortcuts available to us, so instead we have to write it out, albeit a little bit. Let's look at the following four Ruby scripts in order to understand their JS counterparts. They all do the same thing, and JS sort of has something to do with all of them. Let's go through them and build up our `.reduce` statement:

#### 1. reduce takes place inside a single parenthesis

```ruby
# Ruby
array.reduce(:+)
```
```javascript
// Javascript
array.reduce( "sum script" )
```
#### 2. you can set a default value (JS will be in the 2nd position, not the 1st)
```ruby
# Ruby
array.reduce(0, :+)
```
```javascript
// Javascript
array.reduce( "sum script", 0 )
```
#### 3. the operation inside the Ruby block looks almost identical to the JS version.
```ruby
# Ruby
array.reduce { |sum, x| sum + x }
array.reduce(0) { |sum, x| sum + x }
```
```javascript
// Javascript
array.reduce( function(sum, x) { return sum + x } , 0)
```
 Here's how these same reduce functions can look in JS, including with the cleaner ES6 notation:
```javascript
// Javascript
array.reduce( function(sum, x) { return sum + x } )
array.reduce( function(sum, x) { return sum + x }, 0 )
// vs ES6:
array.reduce( (sum, x) => sum + x )
array.reduce( (sum, x) => sum + x, 0 )
```
Again the default value in JS is AFTER the sum variable, not before it. So here's the answer to what that `(:+)` symbol (smiley) was doing under the hood in Ruby, but we'll explain it through JS! We can make our reduce function cleaner though by making `sum` into a variable (using `const`), and we can also make one for multiplication while we're at it:
```javascript
const sum = (sum,x) => sum + x
const multi = (multi,x) => multi * x

array.reduce(sum) //=> 15
array.reduce(sum, 10) //=> 25

array.reduce(multi) //=> 120
array.reduce(multi, 2) //=> 240
```
# Making arrays neater with - Ruby: `.flatten` | JS: `.concat`
---
What happens when you have an array nested within an array (a multi-dimensional array) and want to make it look neater (into a single-dimensional array)? For example we want this ugly nested array:

`array = [1, 2, [[3, 4], 5], [6, nil, 7], 8, 9]`

to look like this neat one:

`array = [1, 2, 3, 4, 5, 6, nil, 7, 8, 9]`

In Ruby it's simple enough as we'd simply call `.flatten` on the array (Ruby once again takes care of the behind-the-scenes code for us)
```ruby
# Ruby
array.flatten #=> [1, 2, 3, 4, 5, 6, nil, 7, 8, 9]
```
In JS it's a bit more complicated, though only by a bit when you get used to it. I'll explain each of these in detail along with what goes into both of these methods.

The first way is the easiest (and my preferred) way: use `.concat` to append each element onto a blank array along with a neat little JS trick:
```javascript
// javascript
[].concat(...array) //=> [1, 2, 3, 4, 5, 6, null, 7, 8, 9]
[].concat(0, ...array) //=> [0, 1, 2, 3, 4, 5, 6, null, 7, 8, 9]
[].concat(...[-1,0], ...array, "woo!") //=> [-1, 0, 1, 2, 3, 4, 5, 6, null, 7, 8, 9, "woo!"]
```
I'll explain the `...` in a second, but the important part about this `.concat` method is that you can combine **any number of arrays or values** and it will combine them all! Meanwhile, in the `(...array)`, that `...` is what's known in JS as a `spread operator` which, well, spreads out an array. It's used during creation or changing of arrays to expand the array and call on all elements in it. For your understanding, here is an example of what this operator does:
```javascript
// Javascript
a1 = [1,2,3]
a2 = [4,5,6]
[a1,a2] //=> [ [1,2,3], [4,5,6] ]
[...a1,a2] //=> [1,2,3, [4,5,6] ]
[...a1,...a2] //=> [1,2,3,4,5,6]
```
The second way is by using `.apply`, which, well, applies what you want into an array. We can either do this to an empty array or to an existing one. Note that unlike the first way you cannot combine more than one array or value:
```javascript
// Javascript
[].concat.apply([],array) //=> [1, 2, 3, 4, 5, 6, null, 7, 8, 9]
[].concat.apply([-1,0],array) //=> [-1, 0, 1, 2, 3, 4, 5, 6, null, 7, 8, 9]
```
Again though, the first method is shorter and is much more useful especially for multiple arrays. It's good to know though what `.apply` can do.

# Removing unwanted values with - Ruby: `.compact` | JS: `.filter`
---
Hold on though, in the above example, even though we ran `flatten`/`concat` on our array, we still have a `nil`/`null` value in there. To get rid of them we simply run the following in Ruby:
```ruby
# Ruby
[1, 2, nil, 3, 4, 5, "hey"].compact #=> [1, 2, 3, 4, 5, "hey"]
```
Which basically iterates over the array and removes `nil` whenever it finds it (non-destructively). To destructively do this just use `.compact!` or `array.delete(nil)`. The syntax will look very similar to the latter where we'll tell our program to delete any element that doesn't pass our test, aka keeping elements that pass. This brings us to how `.filter` is used in JS:
```javascript
// Javascript
[1, 2, null, 3, 4, 5, "hey"].filter(x => x) //=> [1, 2, 3, 4, 5, "hey"]
[1, 2, null, 3, 4, 5, "hey"].filter(Number) //=> [1, 2, 3, 4, 5]
[1, 2, null, 3, 4, 5, "hey"].filter(x => x % 2 === 0) //=> [2, null, 4]
[1, 2, null, 3, 4, 5, "hey"].filter(x => x % 2 === 1) //=> [1, 3, 5]
```
The first basically says: "filter this array by calling the element, and if it's true then it passes through the filter" which gets rid of all `null` values. The second says "filter this array, and if it's a number then it passes through the filter." Note that the second only works if all elements are numbers, but the first works even if you have a mixture of numbers, strings, or otherwise!

The third/fourth filters show the usefulness of filtering out our array as we can test if certain things are true, in this case testing which elements are even or odd respectively. Notice that `null` still passes as `null % 2` is 0, weird right?

# Sorting an array/string/hash/Object with `.sort`

Let's start off simple and we'll end with some neat tricks. Say you have an array of strings that you want to sort alphabetically:

```ruby
# Ruby
array_string = "hey everyone how's it going?".split
array_string #=> ["hey", "everyone", "how's", "it", "going?"]
array_string.sort #=> ["everyone", "going?", "hey", "how's", "it"]
array_string.sort.reverse #=> ["it", "how's", "hey", "going?", "everyone"]
```

```javascript
// Javascript
var array_string = ["hey", "everyone", "how's", "it", "going?"]
array_string.sort() //=> [ "everyone", "going?", "hey", "how's", "it" ]
array_string.sort().reverse() //=> [ "it", "how's", "hey", "going?", "everyone" ]
```

Great easy enough, so let's move onto an array of integers:

```ruby
# Ruby
array = [14, 25, 16, 22, 5]
array.sort #=> [5, 14, 16, 22, 25]
array.sort.reverse #=> [25, 22, 16, 14, 5]
```

```javascript
// Javascript
var array = [14, 25, 16, 22, 5]
array.sort() //=> [ 14, 16, 22, 25, 5 ]
array.sort().reverse() //=> [ 5, 25, 22, 16, 14 ]
```

Oh that's strange, Ruby's smart enough to sort numbers normally but Javascript isn't. Why? Javascript first converts everything to a string first before sorting, then does the actual sort, so it sorts it "alphabetically" instead of numerically. Here's what it's doing from the viewpoint of Ruby:

```ruby
# Ruby
array = [14, 25, 16, 22, 5]
array_string = array.map(&:to_s) #=> ["14", "25", "16", "22", "5"]
array_string.sort #=> ["14", "16", "22", "25", "5"]
array_string.sort.map(&:to_i) #=> [14, 16, 22, 25, 5]
```

The number "1" in 14 appears before the number "5", just like how the "h" in hey appears before the "i" in it, even though "it" is two letters long and "hey" is three letters long, like how 5 is one digits long and 14 is two digits long. So how do we fix this? There's a little trick and it involves forcing Javascript to compare values of adjacent elements. I'll explain this after we do it:

```javascript
// Javascript
var array = [14, 25, 16, 22, 5]
array.sort( function(a,b) { return a - b } ) //=> [ 5, 14, 16, 22, 25 ]
array.sort( function(a,b) { return a > b } ) //=> [ 5, 14, 16, 22, 25 ]
// and reverse:
array.sort( function(a,b) { return b - a } ) //=> [ 25, 22, 16, 14, 5 ]
array.sort( function(a,b) { return a < b } ) //=> [ 25, 22, 16, 14, 5 ]

// ES6 notation

array.sort( (a,b) => a - b ) //=> [ 5, 14, 16, 22, 25 ]
array.sort( (a,b) => a > b ) //=> [ 5, 14, 16, 22, 25 ]
// and reverse:
array.sort( (a,b) => b - a ) //=> [ 25, 22, 16, 14, 5 ]
array.sort( (a,b) => b < a ) //=> [ 25, 22, 16, 14, 5 ]
```

Basically we have to inputs, `a` and `b`. When we return `a - b` or `a > b` we're telling our script to first return smaller values and then larger values, and vice-versa for `a < b` where we tell our script to first return larger values. Remember this trick because it will be used **everywhere**. Let's first try and sort our old string by string length instead of alphabetically. We'll do this by introducing `.sort_by` in Ruby, and just using our prior trick for Javascript:

```ruby
# Ruby
array_string = ["hey", "everyone", "how's", "it", "going?"]
array_string.sort_by { |x| x.length } #=> ["it", "hey", "how's", "going?", "everyone"]
array_string.sort_by { |x| x.length }.reverse #=>  ["everyone", "going?", "how's", "hey", "it"]
```

For Javascript, we'll use that trick from before but instead of comparing each element `a` to `b`, we'll compare their *lengths*:

```javascript
// Javascript
var array_string = ["hey", "everyone", "how's", "it", "going?"]
array_string.sort( (a,b) => a.length - b.length ) //=> [ "it", "hey", "how's", "going?", "everyone" ]
array_string.sort( (a,b) => a.length > b.length ) //=> [ "it", "hey", "how's", "going?", "everyone" ]
array_string.sort( (a,b) => b.length - a.length ) //=> [ "everyone", "going?", "how's", "hey", "it" ]
array_string.sort( (a,b) => a.length < b.length ) //=> [ "everyone", "going?", "how's", "hey", "it" ]
```

This is for an array of elements or object, but what if we have an array of Ruby hashes also known in JS as Objects?

```ruby
# Ruby
array_hash = [ {borough: 'Manhattan', population: 1585874},
               {borough: 'Brooklyn', population: 2504706},
               {borough: 'Queens', population: 2230545},
               {borough: 'Bronx', population: 1385107},
               {borough: 'Staten_Island', population: 486730} ]

array_hash.sort_by { |x| x[:borough] }
#=> [{:borough=>"Bronx", :population=>1385107},
   # {:borough=>"Brooklyn", :population=>2504706},
   # {:borough=>"Manhattan", :population=>1585874},
   # {:borough=>"Queens", :population=>2230545},
   # {:borough=>"Staten_Island", :population=>486730}]

array_hash.sort_by { |x| x[:population] }
#=> [{:borough=>"Staten_Island", :population=>486730},
   # {:borough=>"Bronx",        :population=>1385107},
   # {:borough=>"Manhattan",    :population=>1585874},
   # {:borough=>"Queens",       :population=>2230545},
   # {:borough=>"Brooklyn",     :population=>2504706}]
```

We call on the attribute in ruby, however in JS we call it the exact same way as we would the length, but as the attribute!

```javascript
// Javascript
var array_hash = [ {borough: 'Manhattan', population: 1585874},
                   {borough: 'Brooklyn', population: 2504706},
                   {borough: 'Queens', population: 2230545},
                   {borough: 'Bronx', population: 1385107},
                   {borough: 'Staten_Island', population: 486730} ]

array_hash.sort( (a,b) => a.borough > b.borough )
//=> [ { burough: 'Bronx', population: 1385107 },
    // { burough: 'Brooklyn', population: 2504706 },
    // { burough: 'Manhattan', population: 1585874 },
    // { burough: 'Queens', population: 2230545 },
    // { burough: 'Staten_Island', population: 486730 } ]

// By the length of the borough name
array_hash.sort((a,b) => a.borough.length - b.borough.length ) // or
array_hash.sort((a,b) => a.borough.length > b.borough.length )
//=> [ { borough: 'Bronx', population: 1385107 },
    // { borough: 'Queens', population: 2230545 },
    // { borough: 'Brooklyn', population: 2504706 },
    // { borough: 'Manhattan', population: 1585874 },
    // { borough: 'Staten_Island', population: 486730 } ]

array_hash.sort( (a,b) => a.population - b.population ) // or
array_hash.sort( (a,b) => a.population > b.population )
//=> [ { borough: 'Staten_Island',  population: 486730 },
    // { borough: 'Bronx',         population: 1385107 },
    // { borough: 'Queens',        population: 2230545 },
    // { borough: 'Brooklyn',      population: 2504706 },
    // { borough: 'Manhattan',     population: 1585874 } ]
```

Last up is fairly useless and therefore a but more tricky: sorting a Ruby hash/JS object by its values. This usually isn't *ever* done because a hash/object by nature isn't actually in an order like an array is, it's just **presented** to us visually in an order. In fact if you try to reorder a hash/object you won't get a hash/object back, you'll get an *array*.

```ruby
# Ruby
hash = {Manhattan: 1585874, Brooklyn: 2504706, Queens: 2230545, Bronx: 1385107, Staten_Island: 486730}

# by key
hash.sort # or
hash.sort_by { |key, value| key }
#=> [[:Bronx, 1385107], [:Brooklyn, 2504706], [:Manhattan, 1585874], [:Queens, 2230545], [:Staten_Island, 486730]]

# by value
hash.sort_by { |key, value| value }
#=> [[:Staten_Island, 486730], [:Bronx, 1385107], [:Manhattan, 1585874], [:Queens, 2230545], [:Brooklyn, 2504706]]
```

Javascript can't actually directly do this using sort, only indirectly, in fact it will give you the error "hash.sort is not a function". So we have to use a trick called `Object.values()`, which I'll explain when we get to that section! For now I'll just show you what it looks like:

```javascript
// Javascript
var object = {Manhattan: 1585874, Brooklyn: 2504706, Queens: 2230545, Bronx: 1385107, Staten_Island: 486730}
object.sort() //=> error, not a function

Object.keys(object).sort( (a,b) => object[a] - object[b] ).map(x => `${x}: ${hash[x]}`)
//=> [ 'Staten_Island: 486730',
    // 'Bronx:        1385107',
    // 'Manhattan:    1585874',
    // 'Queens:       2230545',
    // 'Brooklyn:     2504706' ]
```

In basic terms, we sort the values by descending order but we can only get an array of keys back, then we just map that key on itself to get the values.

# Easier if/else/etc with - Ruby: `Case; each` | JS: `Switch; case`
---
The thing about `if/else/elsif/else if` statements is that they can get very repetitive, especially when going through multiple conditions. Say we're watching West Wing and want to get a main character's White House title. We *could* do a series of if statements:

```ruby
# Ruby
def title(name)
  if name == "CJ"; "Press Secretary"
  elsif name == "Donna"; "Assistant to the DCoS"
  elsif name == "Abbey"; "First Lady"
  elsif name == "Jed"; "President"
  elsif name == "Josh"; "Deputy Chief of Staff"
  elsif name == "Sam"; "Deputy Communications Director"
  elsif name == "Toby"; "Communications Director"
  end
end
```
```javascript
// Javascript
function title(name) {
  if (name === "CJ") { return "Press Secretary" }
  else if (name === "Donna") { return "Assistant to the DCoS"}
  else if (name === "Abbey") { return "First Lady"}
  else if (name === "Jed") { return "President"}
  else if (name === "Josh") { return "Deputy Chief of Staff"}
  else if (name === "Sam") { return "Deputy Communications Director"}
  else if (name === "Toby") { return "Communications Director"}
}
```
If we call `title("CJ")` we'll get "Press Secretary", or `title("Jed")` we'll get "President" which is great! But in our code we have to call on `name ===` every. single. time. In addition to a few other things in the code, they're repetitive and constrictive, so instead we can use a `case statement` in Ruby or a `switch statement` in JS.

```ruby
# Ruby
def title(name)
  case name;
    when "CJ"; "Press Secretary"
    when "Donna"; "Assistant to the DCoS"
    when "Abbey"; "First Lady"
    when "Jed"; "President"
    when "Josh"; "Deputy Chief of Staff"
    when "Sam"; "Deputy Communications Director"
    when "Toby"; "Communications Director"
    else "Name Not Found"
  end
end
```
```javascript
// Javascript
function title(name) {
  switch(name) {
    case "CJ": return "Press Secretary"
    case "Donna": return "Assistant to the DCoS"
    case "Abbey": return "First Lady"
    case "Jed": return "President"
    case "Josh": return "Deputy Chief of Staff"
    case "Sam": return "Deputy Communications Director"
    case "Toby": return "Communications Director"
    default: return "Name Not Found"
  }
}
```
**SO** much better! We can even link this to our `.map` method if we'd like to call on an array

`names = ["Josh", "Jed", "Toby", "CJ", "Sam"]`
```ruby
# Ruby
names.map do |name|
  case name;
    when "CJ"; "Press Secretary"
    when "Donna"; "Assistant to the DCoS"
    when "Abbey"; "First Lady"
    when "Jed"; "President"
    when "Josh"; "Deputy Chief of Staff"
    when "Sam"; "Deputy Communications Director"
    when "Toby"; "Communications Director"
    else "Name Not Found"
  end
end
```
```javascript
// Javascript
names.map(name => {
  switch(name) {
    case "CJ": return "Press Secretary"
    case "Donna": return "Assistant to the DCoS"
    case "Abbey": return "First Lady"
    case "Jed": return "President"
    case "Josh": return "Deputy Chief of Staff"
    case "Sam": return "Deputy Communications Director"
    case "Toby": return "Communications Director"
    default: return "Name Not Found"
  }
})
```
Both of these output:

`[ 'Deputy Chief of Staff', 'President',
  'Communications Director', 'Press Secretary',
  'Deputy Communications Director' ]`

Let's do one more example with an array of grades someone got on their tests:

`grades = [95, 83, 68, 99, 75, 60]`

And we want to map those into basic letter grades, aka an A is 90-100, B is in the 80's, etc. Unfortunately JS doesn't have ranges like Ruby does, so it may only be *slightly* better than a series of if statements, but we can still make it work by simply testing to see which case is `true`:
```ruby
# Ruby
grades.map do |grade|
  case grade;
    when 90..100; "A"
    when 80..89; "B"
    when 70..79; "C"
    when 65..69; "D"
    when 0..64; "F"
    else "That grade is impossible!"
  end
end
```
```javascript
// Javascript
grades.map(grade => {
  switch(true) {
    case grade >= 90: return "A"
    case grade >= 80: return "B"
    case grade >= 70: return "C"
    case grade >= 65: return "D"
    case grade >= 0: return "F"
    default: return "That grade is impossible!"
  }
})
```
Both of these output `["A", "B", "D", "A", "C", "F"]`, great!

# Adding to / removing from arrays with:
# Ruby: `.insert` / `.delete_at` / `.slice!` /  | JS: `.splice`
---
It's easy to use `.unshift`/`.shift`/`.push`/`.pop` to add/remove items from the beginning/end of arrays respectively, but what about when we have to add/remove items at certain points *within* the array? Ruby uses `.insert` and `.delete_at`/`.slice!` to do these separately.

`.insert` takes in an index along with a value (or values) you'd like to add, while `.delete_at` takes in just an index:

```ruby
# Ruby
array = ["Hello", "World", "How", "Are", "You?"]

array.insert(2, "!") #=> ["Hello", "World", "!", "How", "Are", "You?"]

array.insert(1,"Everyone", "In", "The")
#=> ["Hello", "Everyone", "In", "The", "World", "!", "How", "Are", "You?"]

array.delete_at(5) #=> ["Hello", "Everyone", "In", "The", "World", "How", "Are", "You?"]
array.slice!(0) # array #=> ["Everyone", "In", "The", "World", "How", "Are", "You?"]
```
JS can do both of these with one method, `.splice`! Splice like `.insert` or `.delete_at` takes in an index, and while the rest are optional they change splice's behavior entirely. Splice's default behavior is to delete, and we need those extra values in there to instead insert. Here's how it looks:

`array.splice(index, how_many_positions_out_to_delete, add_element(s) )`

Since `.splice` is destructive (changes the array permanently), in these examples I'll be remaking the array quite a bit. Let's test it out bit by bit:

```javascript
// Javascript
array = ["Hello", "World", "How", "Are", "You?"]

array.splice(2)
array //=> ["Hello", "World"]
```
If we just put in one value (the index), it will delete all elements starting at that index until the end of the array. It works the same as if we put in a second value:
```javascript
// Javascript
array = ["Hello", "World", "How", "Are", "You?"]

array.splice(2, 100)
array //=> ["Hello", "World"]
```
In this case we're deleting all elements starting at index 2 and going 100 elements out, which covers the end of the array. Let's try deleting just a few at a time instead:
```javascript
// Javascript
array = ["Hello", "World", "How", "Are", "You?"]

array.splice(2, 0)
array //=> ["Hello", "World", "How", "Are", "You?"]
// start at index 2, then delete 0 elements out (which is none!)

array.splice(2, 1) //=> ["How"] removed
array //=> ["Hello", "World", "Are", "You?"]
// start at index 2, then delete 1 element out (just 2)

array = ["Hello", "World", "How", "Are", "You?"]
array.splice(1, 3) //=> ["World", "How", "Are"] removed
array //=> ["Hello", "You?"]
// start at index 1, then delete 3 elements out (1-3)
```
Anything after these two numbers is **added** to the array, so let's mimic what we did in Ruby:
```javascript
// Javascript
array = ["Hello", "World", "How", "Are", "You?"]

array.splice(2, 0, "!") //=> ["Hello", "World", "!", "How", "Are", "You?"]
// start at index 2, delete nothing, then add "!" at index 2

array.splice(1, 0, "Everyone", "In", "The")
//=> ["Hello", "Everyone", "In", "The", "World", "!", "How", "Are", "You?"]
// start at index 1, delete nothing, then add "Everyone", "In", and "The" at index 1

array.splice(4, 1, "Universe")
//=> ["Hello", "Everyone", "In", "The", "Universe", "!", "How", "Are", "You?"]
// start at index 4, delete 1 element out, then add "Universe" at index 4
```
# Test if something's included - Ruby: `.include?` | JS: `.includes`
---
There's a great way to test for inclusion which can be utilized in many ways, and surprisingly JS is the one here that can do more! While Ruby's `.include?` can only test to see if something is included:

```ruby
# Ruby
array = [1, 2, 3, "hello", "world"]
array.include?(3) #=> true
array.include?("hello") #=> true
array.include?(7) #=> false
```
JS can do this, but in addition it can even test for inclusion at a specific index!
```javascript
// Javascript
array = [1, 2, 3, "hello", "world"]
array.includes(3) //=> true
array.includes("hello") //=> true
array.includes(7) //=> false
array.includes("world", 4) //=> true
array.includes(1, 3) //=> false
```
# Keys and Values
---
If you have a Hash in ruby you can simply call `.keys` or `.values` on it to easily get their information:
```ruby
# Ruby
pets = { dogs: 3, cats: 2, birds: 1 }
pets.keys #=> [:dogs, :cats, :birds]
pets.values #=> [3, 2, 1]
```
Under the hood, these methods are basically going through each element in the hash and pulling out the chosen value and putting them in an array. These shortcuts work a bit different in JS. First off, a **hash in Ruby** is known as an **object in JS**. So we'll have to call `.keys` or `.values` on a blank `Object` class and have it take in the Object pets:
```javascript
// JavaScript
Object.keys(pets) //=> ["dogs", "cats", "birds"]
Object.values(pets) //=> [3, 2, 1]
```
# slice
---
Slice is a nice method that goes into an array (or string) and selects the element(s) of your choice. While in Ruby you can directly call on the array/string to get these values using `array[0]` for the first value, or in Ruby only doing more fancy `array[1..4]` to get
```ruby
# Ruby
array = ["Hello", "World", "How", "Are", "You?"]
array[0] #=> "Hello"
array[2..4] #=> ["How", "Are", "You?"]
array[2, 3] #=> ["How", "Are", "You?"]
```
only the first script `array[0]` can be used in JS. This is where `.slice` comes in, however just like `.reduce` it's used differently. If you're familiar with Ruby, `.slice` is used exactly like the above scripts and has the same exact outputs:
```ruby
# Ruby
array = ["Hello", "World", "How", "Are", "You?"]
array.slice(0) # select at index 0
array.slice(2..4) # select from index 2 to index 4
array.slice(2, 3) # select from index 2 and go 3 positions further
```
JS operates differently however. Obviously we don't have ranges so the middle script is of no use to us, but what happens if we try the other two scripts?
```javascript
// Javascript
array = ["Hello", "World", "How", "Are", "You?"]
array.slice(0) //=> ["Hello", "World", "How", "Are", "You?"]
array.slice(2, 3) //=> ["How"]
```
"How" is right... what is happening here? Well in both languages the slice takes in two instances:
`array.slice( start_index, optional_second_number ) `
The `start_here` is the same in both languages, however the `optional_second_number` is what's different.

Ruby says: `start_index`, `go_this_many_positions_further (default is 0)`
JS says: `start_index (default is 0)`, `end_index (default is array.length)`

Wait a second, `(start_index, end_index)`? that's a range! Specifically it's the three-dotted `(n1...n2)` range where we go **up until** the end index. So with that knowledge:
```javascript
// Javascript
array = ["Hello", "World", "How", "Are", "You?"]

array.slice(0) // start at index 0, go to the default end of array.length
array.slice(0, array.length) // same
array.slice(0, 5) // same (array.length is 5, the last index in it is 4)
array.slice(2, 3) // start at index 2, go up until 3 (therefore only index 2)

array.slice() //=> ["Hello", "World", "How", "Are", "You?"]
array.slice(2) || array.slice(2,array.length) || array.slice(2, 5)
// all of them //=> ["How", "Are", "You?"]
array.slice(2, 4) //=> ["How", "Are"]
```

# Ruby: `.call` / `.proc` | JS: `callbacks`
---
Finally, what if we had a function inside of another function? Let's come back to that question shortly.

Say we were writing a function that did a few complicated things within it, but then wanted to easily change them or call on them again? For example, what if we wanted to multiply two numbers but have them squared first? We *could* do something like write it all out:

```ruby
# Ruby
def multiply_squared(x, y)
  x*x * y*y
end

multiply_squared(2, 3) #=> 2*2 * 3*3 = 4 * 9 = 36
```
```javascript
// Javascript
function multiply_squared(x, y) { x*x * y*y }

multiply_squared(2, 3) //=> 2*2 * 3*3 = 4 * 9 = 36
```
Great, but what if instead of squaring these I wanted to cube them? What if I wanted to have `x` equal another equation? Sure for cubing I could simply change the equation to `2*2*2 * 3*3*3` but that'd get messy especially if I wanted to add another one to the exponent, or I could change the equation to `2**3 * 3**3` and just simply change the exponent that way, but that'd get tedious and I also wouldn't be able to call that as its own function. For `x` as another equation that'd also get ugly as for example `multiply_squared(2, (32/8) + 4)`. `.call` / `.proc` in Ruby and `callbacks` in Javascript fix this.

In Ruby, we can first make a `Proc` which is a function that can be called on in the future. For example:

```ruby
# Ruby
say_hello = Proc.new { puts "hello" }
#=> <Proc:0x007fbf7019b270@(irb):41>

# we then can call on this Proc object

say_hello.call #=> "hello"

say_hello()
```
A proc is an object that has its own set of variables. If you know about classes, then the `<Proc:0x007fbf7019b270@(irb):41>` looks very similar:
```ruby
# Ruby
class Dog

  def initialize(name, breed)
    @name = name
    @breed = breed
  end

end

dog = Dog.new("Lily", "Pit Mix")
#=> <Dog:0x007fbf701290d0 @name="Lily", @breed="Pit Mix">
```
So what can we do with Procs? Here's an example of what a basic function, and then a proc function does:
```ruby
# Ruby
def multi_basic(x, y)
  x * y
end

multi_basic(2, 3) #=> 6

def multi_proc(x, y)
  Proc.new { x * y }
end

multi_proc(2, 3) #=> <Proc:0x007fbf701808d0@(irb):47>
multi_proc(2, 3).call #=> 6
```
Why is this so special? Our proc isn't simply the answer to `2*3`, it's an **object** that stores that answer, and we can call on it at any point or even do more with it. In the very simplest form we can create an object that simply can output the answer:

```ruby
# Ruby
multiply_5_6 = multi_proc(5, 6) #=> <Proc:0x007fbf7016adf0@(irb):48>
multiply_5_6.call #=> 30

say_hello_to_someone = Proc.new { |name| puts "Hello #{name}!" }
say_hello_to_someone #=> <Proc:0x007fb0d20b4ca0@(irb):49>
say_hello_to_someone.call("Mike") #=> "Hello Mike!"
```
OR, we can get to the real reason why calls and procs are great: the ability to create an open-ended proc function that can be completed with a call:

```ruby
# Ruby
def multiply(n)
    Proc.new { |x| x * n }
end

multiply_by_six = multiply(6)
multiply_by_six.call(5) #=> 30
multiply_by_six.call(10) #=> 60

multiply_by_thirty = multiply(30)
multiply_by_thirty.call(5) #=> 150
multiply_by_thirty.call(25) #=> 750
```
If we wrote these same scripts out as functions within a function it would get pretty messy. Going back to what we did before:
```ruby
# Ruby
def multiply_squared(x, y)
  x**2 * y**2
end

multiply_squared(multiply_by_six.call(2), 2) #=> 12*12 * 2*2 = 144 * 4 = 576

# instead with callbacks

multiply_six_squared = Proc.new { |x,y| multiply_by_six.call(x)**2 * y**2 }
multiply_six_squared.call(2, 2) #=> 576
```
We have our object to call on, and can change it any way we want. Why did I take a long time to go through what these do? Because this is one of those times where Javascript makes things easier than Ruby and it's important to be able to visualize what goes on under the hood. Here's how a callback would work in Javascript; see if you can see the similarities:

```javascript
// Javascript
var say_hello = function() { console.log("Hello") }
say_hello() //=> "Hello"

// The same in ES6 notation:

var say_hello = () => { console.log("Hello") }
say_hello() //=> "Hello"

// as a callback:

var say_hello_callback = function(callback) { callback }
say_hello_callback(console.log("Hello")) //=> "Hello"

// ES6
var say_hello_callback = callback => { callback }
say_hello_callback(console.log("Hello")) //=> "Hello"

// extract "hello" as another callback

function hello() { return "Hello" }
say_hello_callback(console.log( hello() )) //=> "Hello"
```
As you can see, Javascript handles our "proc" by just naming a function. Let's callback even further:
```javascript
// Javascript
var say_hello_to_someone = function(name) { console.log(`Hello ${name}!`) }
say_hello_to_someone("Mike") //=> "Hello Mike!"

//ES6:
var say_hello_to_someone = name => { console.log(`Hello ${name}!`) }
say_hello_to_someone("Mike") //=> "Hello Mike!"

// extract "hello" again

function hello() { return "Hello" }
var say_hello_to_someone = name => { console.log(`${hello()} ${name}!`) }
say_hello_to_someone("Mike") //=> "Hello Mike!"

// and name

function hello() { return "Hello" }
function name() { return "Mike" }
var say_hello_to_someone = () => { console.log(`${hello()} ${name()}!`) }
say_hello_to_someone() //=> "Hello Mike!"

// with a callback

var say_hello_to_someone_callback = (callback) => { callback }
say_hello_to_someone_callback(console.log(`${hello()} ${name()}!`))

// double callback!

function greeting() { return "Hello" }
function name() { return "Mike" }
function log() { console.log(`${hello()} ${name()}!`) }
var say_hello_to_someone_callback_callback(callback_2) = (callback) => { callback }
say_hello_to_someone_callback_callback(log()) //=> "Hello Mike!"

// another way with multiple inputs

var say_hello_to_someone_input = (greeting, name) => { console.log(`${greeting} ${name}!`) }
say_hello_to_someone_input("Hello", "Mike") //=> "Hello Mike!"
say_hello_to_someone_input(greeting(), name()) //=> "Hello Mike!"
```
We can even call our function and do things before we callback:
```javascript
// Javascript
var lastly_say_hello_callback = callback => {
  console.log("Loading greeting...")
  callback
}
lastly_say_hello_callback(console.log("Hello"))
//=> "Hello"
//=> "Loading greeting..."
```
Oops our greeting callback loaded before our loading message because this is asynchronous. Let's add a `timeout` to our callback:
```javascript
// Javascript
var lastly_say_hello_callback = callback => {
  console.log("Loading greeting...")
  setTimeout(callback, 1000)
}
lastly_say_hello_callback(()=>console.log("Hello"))
//=> "Loading greeting..."
// sleep for 1 second
//=> "Hello"
```
And to be really cheeky, let's have some callbacks that also take in inputs:
```javascript
// Javascript
function log(greeting, name) { console.log(`${greeting} ${name}!`) }
function say_hello_to_someone_callback_inputs(callback) { callback(arguments[1], arguments[2]) }
say_hello_to_someone_callback_inputs(log, "Hello", "Mike")
```
There's so much more you can do with this, try it out yourselves!

---

So that covers some of the most important JS loops/iterations/methods. If there are any others you'd like added let me know!

Code on.

Mike Merin
