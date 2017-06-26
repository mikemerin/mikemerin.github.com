---
layout: post
title:  "A Javascript Cheat Sheet"
date:   2017-05-20 22:46:38 -0400
categories: javascript, tutorial
---
This is an abbreviated cheat sheet for Javascript. If you want an detailed explanation of how everything you see here works including explanations through the eyes of Ruby you can find that [here](https://mikemerin.github.io/JS-through-Ruby/), which I highly recommend.


ES6 Notation | Arrow Functions | while | for
for..in | .forEach | .map | .reduce
.concat | .filter | switch; case | .splice
.includes | Object.keys() | Object.values() | .slice
call/proc (Ruby) callbacks (JS) |

### ES6 Notation, Arrow Functions, and Implicit Returns
Shorten/clean up your functions. These all do the same thing:
```javascript
function(x) { console.log(x) }
(x) => { console.log(x) }
x => { console.log(x) }

function(x,i) { console.log(`Element ${x} Index ${i}`) }
(x,i) => { console.log(`Element ${x} Index ${i}`) }
```
These all do the same thing as well (implicit returns)
```javascript
function(x) { return x * 2 }
(x) => { return x * 2 }
x => { return x * 2 }
(x) => x * 2   // without the {} this implicitly returns
x => x * 2     // same here
(x) => (x * 2) // same here
```
### while
Perform a piece of code while a loop is active.

```javascript
while (condition) { code block }

x = 3
while ( x > 0 ) { console.log(`${x} to go`; x--)

x = 1
array = []
while ( x < 6 ) { array.push(x); x++ }
array //=> [1,2,3,4,5]
```
### for / for..in
Iterate over an array (or string) and perform code on each element
```javascript
for ( initialization; condition (optional); expression ) { code block }
for ( variable in object) { code block }

array = []
array2 = []

for (let x = 1; x < 6; x++) { array.push(x) }
array //=> [1,2,3,4,5]

for (let i = 0, l = array.length; i < l; i++) { array2.push( array[i] ) }
for (let i in array) { array2.push( array[i] ) }

// array2 in both becomes [1,2,3,4,5]
```
### .forEach
Iterate over an array (or string) and perform code on each element
```javascript
array.forEach( function(callback) { code block } )

array = [1,2,3,4,5]
array2 = []
array.forEach( function(x) { array2.push(x) } )
array.forEach( x => array2.push(x) )
array.forEach( (x, i) => console.log(`The index is ${i}, the element is ${x}`) )
```
### .map
iterates over each element, but also changes the output
```javascript
array.map( function(callback) { code block } )

array = [1,2,3,4,5]
array.map(function(x) => {return x * 2} ) //=> [2,4,6,8,10]
array.map(x => x * 2) //=> [2,4,6,8,10]
array.map((x, i) => i) //=> [0,1,2,3,4]
array.map((x, i) => x * i) //=> [0,2,6,12,20]
```
### .reduce
Reduce each element in the array to a single value
```javascript
array.reduce(callback, default value (optional) )

array = [1,2,3,4,5]

// all add up to 15
array.reduce( function(sum, x) { return sum + x } )
array.reduce( function(sum, x) { return sum + x }, 0 )
array.reduce( (sum, x) => { return sum + x } )
array.reduce( (sum, x) => { return sum + x }, 0 )


const sum = (sum,x) => {return sum+x}
const multi = (multi,x) => {return multi*x}

array.reduce(sum) //=> 15
array.reduce(sum, 10) //=> 25

array.reduce(multi) //=> 120
array.reduce(multi, 2) //=> 240
```
### Spread operator
Spreads out an array to call on all individual elements
```javascript
a1 = [1,2,3]
a2 = [4,5,6]

[a1,a2] //=> [ [1,2,3], [4,5,6] ]
[...a1,a2] //=> [1,2,3, [4,5,6] ]
[...a1,...a2] //=> [1,2,3,4,5,6]
```
### .concat
Turn one (or more) multi-dimensional array(s) into a single-dimensional array  
```javascript
[].concat(*values_or_arrays)

array = [1, 2, [[3, 4], 5], [6, 7], 8, 9]

[].concat(...array) //=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
[].concat(0, ...array) //=> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[].concat(...[-1,0], ...array, "woo!") //=> [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "woo!"]
```
### Filter
Filter the values you want to keep
```javascript
array.filter(callback)

[1, 2, 3, null, 4, 5].filter(x => x) //=> [1, 2, 3, 4, 5]
[1, 2, 3, null, 4, 5].filter(Number) //=> [1, 2, 3, 4, 5]
[1, 2, 3, null, 4, 5].filter(x => x % 2 === 0) //=> [2, 4, null]
[1, 2, 3, null, 4, 5].filter(x => x % 2 === 1) //=> [1, 3, 5]
```
### Switch; case
Simplifying multiple `if/else if/else` statements
```javascript
switch(value_or_expression) {
  case x: code_block
  case y: code_block
  default: code_block
}

name = "Josh"

switch(name) {
  case "CJ": return "Press Secretary"
  case "Donna": return "Assistant to the DCoS"
  case "Jed": return "President"
  case "Josh": return "Deputy Chief of Staff"
  case "Sam": return "Deputy Communications Director"
  case "Toby": return "Communications Director"
  default: return "Name Not Found"
}

//=> "Deputy Chief of Staff"

// iterating over a switch statement

names = ["Josh","Jed","Toby","CJ","Sam"]

names.map(name => {
  switch(name) {
    case "CJ": return "Press Secretary"
    case "Donna": return "Assistant to the DCoS"
    case "Jed": return "President"
    case "Josh": return "Deputy Chief of Staff"
    case "Sam": return "Deputy Communications Director"
    case "Toby": return "Communications Director"
    default: return "Name Not Found"
  }
}) //=> [ 'Deputy Chief of Staff', 'President', 'Communications Director', 'Press Secretary', 'Deputy Communications Director' ]

grades = [95, 83, 68, 99, 75, 60]

grades.map(grade => {
  switch(true) {
    case grade >= 90: return "A"
    case grade >= 80: return "B"
    case grade >= 70: return "C"
    case grade >= 65: return "D"
    case grade >= 0: return "F"
    default: return "That grade is impossible!"
  }
}) //=> ["A", "B", "D", "A", "C", "F"]
```
### .splice
Add or remove elements from an array/string
```javascript
array.splice(index, how_many_positions_out_to_delete, add_element(s) )

array = ["Hello", "World", "How", "Are", "You?"]
array.splice(2) //=> removes from index 2 to the end
array //=> ["Hello", "World"]

array = ["Hello", "World", "How", "Are", "You?"]
array.splice(0, 2) //=> starts at index 0, then delete 2 elements out
array //=> ["How", "Are", "You?"]

array = ["Hello", "World", "How", "Are", "You?"]
array.splice(2, 0, "!") //=> start at index 2, delete nothing, then add "!" at index 2
array //=> ["Hello", "World", "!", "How", "Are", "You?"]

array.splice(1, 0, "Everyone", "In", "The")
//=> ["Hello", "Everyone", "In", "The", "World", "!", "How", "Are", "You?"]
// start at index 1, delete nothing, then add "Everyone", "In", and "The" at index 1
```
### .includes
Test if a something is included in an array
```javascript
array.includes(element, index)

array = [1, 2, 3, "hello", "world"]

array.includes(3) //=> true
array.includes("hello") //=> true
array.includes(7) //=> false
array.includes("world", 4) //=> true
array.includes(1, 3) //=> false
```
### Object.keys() / Object.values()
Get all keys or values in a hash
```javascript
Object.keys(pets) //=> ["dogs", "cats", "birds"]
Object.values(pets) //=> [3, 2, 1]
```
### .slice
Select element(s) from an array, from a start_index up until an end_index
The start_index's default is 0, the end_index's default is the end of the array
```javascript
array.slice(start_index, end_index)

array = ["Hello", "World", "How", "Are", "You?"]

array.slice() || array.slice(0) || array.slice(0, array.length)
// all of them //=> ["Hello", "World", "How", "Are", "You?"]

array.slice(2, 3) //=> ["How"]
// start at index 2, go up until 3 (therefore only index 2)

array.slice(2, 4) //=> ["How", "Are"]

array.slice(2) || array.slice(2,array.length) || array.slice(2, 5)
// all of them //=> ["How", "Are", "You?"]
```
