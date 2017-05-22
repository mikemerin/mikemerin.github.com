---
layout: post
title:  "Javascript Iteration Cheat Sheet: Understanding JS Through Ruby"
date:   2017-05-20 22:43:38 -0400
categories: javascript
---

If you learned how to program in Ruby, you probably noticed there's a large amount of shortcuts available to cut down on typing (while helping keep your code clean), as well as having a straightforward "English-like" syntax. These shortcuts are very noticable when you get into looping or iterating over objects, and if like me you learned Ruby first, you may not have known what those shortcuts actually do under the hood, so let's dive right in and compare how Ruby and Javascript handle these shortcuts and iterations.

I'll assume you know how to iterate in Ruby already, but if not then look at my [first cryptography post](https://mikemerin.github.io/cryptography/) for a detailed explanation. I'll also be shortening my JS scripts with ES6 JS notation or *arrow functions*, but don't worry I'll explain them as I go along.

We'll be going over these 5 types of loops/iterations:

Type | Description | Languages
:---|:-------------------------------------------------------:|---:
while | loops while condition is true | Ruby/JS
.each | goes over each element | Ruby
for | goes over each element, more used in JS | Ruby/JS
forEach | JS only, more shorthand version of for | JS
.reduce | combines all elements via an operation | Ruby/JS

As well as how to perform these special methods:
Ruby | JS Equivalent | Description
:---|:-------------------------------------------------------:|---:
.keys | Object.keys | get all keys in a hash
.values | Object.values | get all values in a hash
.include? | .includes | test if an element is included in an array
case | switch | shorthand multiple `if` statements



Finally at the end I'll cover how to mimick these are Ruby-only iterations since they're not explicitly used in JS:

Type | Description | Languages
:---|:-------------------------------------------------------:|---:
until | loops until condition is true (opposite of while) | Ruby
.map | same as each, but also modifies the output | Ruby
.map! | goes over each element, changes the output, modifies the original array | Ruby
.each_with_index | goes over each element, also provides an index | Ruby
.each.with_index | same as above | Ruby
.map.with_index | same as above, but changes the output | Ruby
.inject | same as .reduce | Ruby

# looping with `while`
---
Let's start off with the easiest example. These methods are almost identical in both Ruby and Javascript, in fact the only thing that's different is the syntax (using `var` and `{}` ). Here's a quick example:
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
```javascript
// Javascript
var array = []
var x = 1
while (x < 6) {
    array.push(x)
    x += 1
}
array //=> [1,2,3,4,5]
```
Let's do a side-by-side:

Ruby | Javascript | Difference
---|---|---
array = [] | var array = [] | var for JS (can also do let)
x = 1 | var x = 1 | same, doing var (or let)
while x < 6 | while (x < 6) | JS needs its test to be in parenthesis `()`
array.push(x) | { array.push(x) | same, but JS needs to be in a block `{}`
x += 1 | x += 1 | same (but in JS you can also do `x++`)
end | } | JS must ends by closing off the curly bracket
array | array | both #=> [1,2,3,4,5]

While Ruby does much of the work for us, JS we need to manually put in the parentheses and curly brackets. However knowing this means we can more easily do one line solutions (helpful if combining with other complex scripts):
```ruby
# Ruby
array = []
x = 1
while x < 6; array.push(x); x += 1 end
array #=> [1,2,3,4,5]
```
```javascript
// Javascript
array = []
x = 1
while ( x < 6 ) { array.push(x); x++ }
array //=> [1,2,3,4,5]
```
While in this case our JS looks a bit cleaner, this is by no means the cleanest way to do this type of operation. Ruby has quite a few ways to shorten this, including a trick using `.reduce` (also known as `.inject` in Ruby only), but I'll cover that later on.
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
# iterating with `.each`, then `for` and `forEach` with JS!
---
Onto iterations. Flashing back to Ruby let's cover how we can iterate over an array using `.each` beginning with a more lengthy iteration and ending with a shortcut. These first three are the former:
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

for (let i = 0, l = array.length; // declare i and l as variables (separated by commas)
     i < l; // do this while the index is less than the array length
     i++ ) // increment by 1
    { array2.push( array[i] ) }
array2 //=> [1,2,3,4,5]

// shorter and clean version:

for (let i = 0, l = array.length; i < l; i++) { array2.push( array[i] ) }
//=> [1,2,3,4,5]
for (let i = 0, l = array.length; i < l; i++) { array2.unshift( array[i] ) }
//=> [5,4,3,2,1]
```
Hold on though, doesn't Ruby have a better way to iterate over an array that inherently **knows** to go from the start to the end of an array without us telling? It does, and JS does too! In Ruby we'd do:
```ruby
# Ruby
array = [1,2,3,4,5]
array2 = []

array.each { |x| print x }
#=> 12345

array.each { |x| array2.push(x) }
array2 #=> [1,2,3,4,5]

array2 = []
array.each { |x| array2.unshift(x) }
array2 #=> [5,4,3,2,1]
```
This way we're calling on the element itself in the block rather than the index. In JS we'd clean up our ugly `x = 0, l = etc` line with:
```javascript
// Javascript
array = [1,2,3,4,5]
array2 = []

// old way:
for (let i = 0, l = array.length; i < l; i++) { array2.push( array[i] ) }
// new way:
for (let i in array) { array2.push( array[i] ) }
//=> [1,2,3,4,5]
for (let i in array) { array2.unshift( array[i] ) }
//=> [5,4,3,2,1]
```
But wait, we're still calling on the index instead of grabbing the element itself, so we **still** have to do `array[i]` instead of how we were just using `x` in Ruby above! Let's use `forEach` and fix that:
```javascript
// Javascript
array = [1,2,3,4,5]
array2 = []

array.forEach( function(x) { array2.push(x) } )
array2 //=> [1,2,3,4,5]
```
And now to finally tap into that fancy ES6 notation I mentioned way back in the intro. We'll turn our function into a cleaner looking arrow function which does the same exact thing:
```javascript
// Javascript
array.forEach( (x) => { array2.push(x) } )

// and since there's only one thing (x) we're using:
array.forEach( x => { array2.push(x) } )
```
There we go, less characters cluttering up the space, and we finally call on the element in the array rather than the index!
# .reduce
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

In JS however, we don't have these shortcuts available to us, so instead we have to write it out, albeit a little bit. Let's look at the following four Ruby scripts in order to understand their JS counterparts. They all do the same thing, and JS sort of has something to do with all of them. They're similar because in JS:

```ruby
# Ruby
array.reduce(:+)
# reduce takes place inside a single parenthesis

array.reduce(0, :+)
# you can set a default value (JS will be in the 2nd position, not the 1st)

array.reduce { |sum, x| sum + x }
array.reduce(0) { |sum, x| sum + x }
# the operation inside the Ruby block looks almost identical to the JS version.
```
 Here's how these same reduce functions can look in JS, including with the cleaner ES6 notation:
```javascript
// Javascript
array.reduce( function(sum, x) { return sum + x } )
array.reduce( function(sum, x) { return sum + x }, 0 )
array.reduce( (sum, x) => { return sum + x } )
array.reduce( (sum, x) => { return sum + x }, 0 )
```
Again the default value in JS is AFTER the sum variable, not before it. We can make our reduce function cleaner though if we actually make `sum` into a variable (as a constant), and we can also make one for multiplication while we're at it:
```javascript
const sum = (sum,x) => {return sum+x}
const multi = (multi,x) => {return multi*x}

array.reduce(sum) //=> 15
array.reduce(sum, 10) //=> 25

array.reduce(multi) //=> 120
array.reduce(multi, 2) //=> 240
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
# WIP:
---
---
***
---
---
# Ruby: `.include?` | JS: `.includes`
---
# Ruby: `case / when` | JS: `switch / case`
---
# extra iterations:
---
```ruby
# Ruby
(0...array.length).map { |i| array[i] * 10 } #=> [10,20,30,40,50]
array #=> [1,2,3,4,5]
# the output is changed, but the array itself is unchanged after iteration

# shortening the process:

array.map { |x| x*10 } #=> [10,20,30,40,50]
array #=> [1,2,3,4,5]
# array is unchanged after iteration

array.map! { |x| x*2 } #=> [2,4,6,8,10]
array #=> [2,4,6,8,10]
# array is changed

array.map { |x| x = "hi" } #=> ["hi","hi","hi","hi","hi"]
```
