


'''

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
'''
