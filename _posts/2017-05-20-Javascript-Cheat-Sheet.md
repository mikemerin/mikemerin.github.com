---
layout: post
title:  "A Javascript Cheat Sheet"
date:   2017-05-20 22:46:38 -0400
categories: javascript
---
This is an abbreviated cheat sheet for Javascript. If you want an detailed explanation of how everything you see here works including explanations through the eyes of Ruby you can find that [here](https://mikemerin.github.io/JS-through-Ruby/), which I highly recommend.



### ES6 Notation and Arrow Functions
These mean the same thing:
```javascript
function(x) { console.log(x) }
(x) => { console.log(x) }
x => { console.log(x) }

function(x,i) { console.log(`Element ${x} Index ${i}`) }
(x,i) => { console.log(`Element ${x} Index ${i}`) }
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
### for
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

title("Josh") //=> "Deputy Chief of Staff"

// iterating over a switch statement

names = ["Josh","Jed","Toby","CJ","Sam"]

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


.insert | .splice | add element(s) from array/string

.delete_at / .slice! | .splice | remove element(s) from array/string



.include? | .includes | test if an element is included in an array/string

.keys | Object.keys() | get all keys in a hash

.values | Object.values() | get all values in a hash

.slice | .slice | select element from array (different in Ruby vs. JS)