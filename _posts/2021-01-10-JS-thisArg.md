---
layout: post
title:  "JavaScript's thisArg"
subtitle: "A Mystical Thing No More"
date:   2021-01-01 21:53:54 -0400
categories: ECMAScript, JS, thisArg
---
In the official docs for methods like [filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) and [forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach), you may have noticed `thisArg` making an appearance:

```js
let newArray = arr.filter(callback(currentValue[, index[, array]]) {
  // return element for newArray, if true
}[, thisArg]);
```

You can think of it simply as 'this' 'argument'. Let's do a classic example of finding all even numbers, and `console.log(this)` inside it:

```js
const arr = [1, 2, 3, 4, 5, 6];
arr.filter(function(n) {
    console.log(this); // outputs 'undefined', or 'Window' in Chrome
    return n % 2 === 0;
}); // [2, 4, 6]
```

This is where `thisArg` comes into play; we can pass in the array to have access to it as `this`!

```js
const arr = [1, 2, 3, 4, 5, 6];
arr.filter(function(n) {
    console.log(this); // outputs [1, 2, 3, 4, 5, 6] each time
    return n % 2 === 0;
}, obj); // [2, 4, 6]
```

In order to take advantage of passing in `thisArg`, we can try adding in other things as well and then use it directly:

```js
const myObject = { even: 0, odd: 1, third: 3 };
arr.filter(function(n) {
    console.log(this); // outputs 'myObject' of { even: 0 }
    return n % 2 === this.even;
}, myObject); // [2, 4, 6]

arr.filter(function(n) { return n % 2 === this.odd }, myObject); // [1, 3, 5]
arr.filter(function(n) { return n % this.thirds === 0 }, myObject); // [3, 6]
```

Lastly, please take note that this doesn't work with arrow functions as it won't bind correctly.

Code On.

-Mike Merin
