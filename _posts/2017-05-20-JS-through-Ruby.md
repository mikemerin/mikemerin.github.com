---
layout: post
title:  "Seeing Javascript Through Rose-Colored Glasses - A JS Cheat Sheet"
date:   2017-05-20 22:43:38 -0400
categories: javascript
---
Note: this is a Work In Progress (I note the break point below)
---

Javascript Iteration Cheat Sheet: Understanding JS Through Ruby

If you learned how to program in Ruby, you probably noticed there's a large amount of shortcuts available to cut down on typing (while helping keep your code clean), as well as having a straightforward "English-like" syntax. JS sort of has these but require more labor to actually get working. These shortcuts are very noticable when you get into looping or iterating over objects, and if like me you learned Ruby first, you may not have known what those shortcuts actually do under the hood, so let's dive right in and compare how Ruby and Javascript handle these shortcuts, iterations, and methods.

**I'll be going into a lot of detail in this post, if you want an abbreviated JS-only cheat sheet you can find that [here](https://mikemerin.github.io/Javascript-Cheat-Sheet/), though I would recommend going through this post if you want a better understanding of how everything works.**

I'll assume you know how to iterate in Ruby already, but if not then look at my [first cryptography post](https://mikemerin.github.io/cryptography/) for a detailed explanation. I'll also be shortening my JS scripts with ES6 JS notation or *arrow functions*, but don't worry I'll explain them as I go along.

We'll be going over these loops, iterations, and global methods:

Ruby | JS Equivalent | Description
---|---|---
`loops`|||
while / until | while | loops while condition is true
`iteration`|||
for | for | iterate over each element, more used in JS
.each | .forEach | iterate over each element
.each.with_index | .forEach | same, but also get the index
.map | .map | iterate over each element, changes the output
.map.with_index | .map | same, but also get the index
`manipulating methods`|||
.reduce / .inject | .reduce | combines all elements via an operation of your choice
.flatten | .concat | merge multi-dimensional / nested arrays
.compact | .filter | remove `nil` or `null` values from an array
case; each | switch; case | shorthand multiple `if` statements
.insert | .splice | add element(s) from array/string
.delete_at / .slice! | .splice | remove element(s) from array/string
`selecting methods`|||
.include? | .includes | test if an element is included in an array/string
.keys | Object.keys() | get all keys in a hash
.values | Object.values() | get all values in a hash
.slice | .slice | select element from array (different in Ruby vs. JS)

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
# iterating with `.each`/`for` then `each`/`forEach`
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
array.forEach( function(x) { console.log(x) } )
array.forEach( function(x) { array2.push(x) } )
```
And now to finally tap into that fancy ES6 notation I mentioned way back in the intro. We'll turn our function into a cleaner looking arrow function which does the same exact thing:
```javascript
// Javascript
array.forEach( (x) => { array2.push(x) } )
// we can remove the () around the "x" since there's only one element we're using,
// and we can also remove the {} since arrow functions can implicitly interpret them:
array.forEach( x => array2.push(x) )
```
There we go, less characters cluttering up the space, and we finally call on the element in the array rather than the index!
# Using Ruby's `.each_with_index` or `.each.with_index` in JS
These are the same thing in Ruby, however JS has neither of these functions available. Thankfuly though JS has a way to easily iterate over both the element **and** the index at the **same time**:
```ruby
# Ruby
array = ["Hello","World"]
array.each_with_index { |x,i| puts "the index is #{i}, the element is #{x}" }
```
```javascript
// Javascript
array.forEach( (x, i) => console.log(`The index is ${i}, the element is ${x}`) )
```
These both print out:

"the index is 0, the element is Hello"

"the index is 1, the element is World"
# Iterating and manipulating with `.map`
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

`names = ["Josh","Jed","Toby","CJ","Sam"]`
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

# Adding to arrays with - Ruby: `.insert` | JS: `.splice`
---

# Removing from arrays with - Ruby: `.delete_at` | JS: `.splice`
---



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







# Ruby: `.include?` | JS: `.includes`
---
# slice
---
Slice is a nice method that goes into an array (or string) and selects the element(s) of your choice. While in Ruby you can directly call on the array/string to get these values using `array[0]` for the first value, or in Ruby only doing more fancy `array[1..4]` to get
```ruby
# Ruby
array = ["Hello","World","How","Are","You?"]
array[0] #=> "Hello"
array[2..4] #=> ["How", "Are", "You?"]
array[2,3] #=> ["How", "Are", "You?"]
```
only the first script `array[0]` can be used in JS. This is where `.slice` comes in, however just like `.reduce` it's used differently. If you're familiar with Ruby, `.slice` is used exactly like the above scripts and has the same exact outputs:
```ruby
# Ruby
array = ["Hello","World","How","Are","You?"]
array.slice(0) # select at index 0
array.slice(2..4) # select from index 2 to index 4
array.slice(2,3) # select from index 2 and go 3 positions further
```
JS operates differently however. Obviously we don't have ranges so the middle script is of no use to us, but what happens if we try the other two scripts?
```javascript
// Javascript
array = ["Hello","World","How","Are","You?"]
array.slice(0) //=> ["Hello","World","How","Are","You?"
array.slice(2,3) //=> ["How"]
```
"How" is right... what is happening here? Well in both languages the slice takes in two instances:
`array.slice( start_index, optional_second_number ) `
The `start_here` is the same in both languages, however the `optional_second_number` is what's different.

Ruby says: `start_index`, `go_this_many_positions_further (default is 0)`
JS says: `start_index (default is 0)`, `end_index (default is array.length)`

Wait a second, `(start_index, end_index)`? that's a range! Specifically it's the three-dotted `(n1...n2)` range where we go **up until** the end index. So with that knowledge:
```javascript
// Javascript
array = ["Hello","World","How","Are","You?"]

array.slice(0) // start at index 0, go to the default end of array.length
array.slice(0, array.length) // same
array.slice(0, 5) // same (array.length is 5, the last index in it is 4)
array.slice(2, 3) // start at index 2, go up until 3 (therefore only index 2)

array.slice() //=> ["Hello","World","How","Are","You?"]
array.slice(2) || array.slice(2,array.length) || array.slice(2, 5)
// all of them //=> ["How", "Are", "You?"]
array.slice(2, 4) //=> ["How", "Are"]
```

So that covers some of the most important JS loops/iterations/methods. If there are any others you'd like added let me know!

Code on.

Mike Merin
