---
layout: post
title:  "Object Orientation in Four Languages"
subtitle: "OO 101"
date:   2017-12-11 22:06:15 -0400
categories: Ruby, JavaScript, Python, PHP, tutorial
---
Object Oriented Programing, or OOP is an incredibly important tool that all developers should know. If you know one language and are trying to learn another one, learning Functional Programming of methods, iterations, and basic structures may be easier to learn (shameless plug for my [educational posts](https://mikemerin.github.io/education) on learning them), but the nuances of OOP are slightly more advanced and may be harder to grasp, especially if it's your first language.

Typically when you learn about programming you do so through Functional Programming, e.g. making functions, statements, variables, etc. that can be used at any time in any place inside of your program, interacting freely with one another. However as your program grows, creating more and more functions and variables that are roaming freely throughout your program can cause errors. The possibility of overwriting one another, having bad and erroneous interactions, or most importantly not being able to change as your program grows, limits what you can do with Functional Programming.

In OOP however, we take all of these basic concepts and instead store them **inside** of objects. We can let our objects hold whatever information we want to use at any time. This keeps our code much cleaner, lets customize functions statements and variables in one object without affecting any other, and allows us to share or inherit that information as we choose.

This post will go through Ruby, JavaScript, Python, and PHP, showing the basic similarities between each of the languages to get your feet on the ground. I'll first give a full example from each language including how to initiate the class, create a class function, and modify attributes, then I'll go piece by piece to explain what they actually do.

Note that I won't be talking about basic syntax here, aka Ruby's `def/end` vs. JavaScript/PHP's `{}` vs. Python's `: + whitespace` vs. PHP's `$variables;` etc. Please use my [educational posts](https://mikemerin.github.io/education/) to learn the basics of each language and their functionalities as a primer for this post.

# Overview
---
I find that the best way to figure out how to do OOP is to actually see the working product. That way I can backwards engineer each part to learn what they do.

Say I wanted to create a Dog object `my_dog`. This Dog object would have three attributes: a name, a breed, and an age, and I can either access or change those attributes manually or make them private to be unchangeable. I'd want to give it an `info()` function that can tell me information about the specific Dog object, a `birthday()` function to increase the age by one and wish the dog a happy birthday, and finally a `greet(message)` function to greet the Dog object with a message.

Here's how we'd create this Dog object in Ruby, JavaScript, Python, and PHP, and how we'd interact with it after we create it:

### Ruby
---

```ruby

class Dog

  attr_accessor :name, :breed, :age

  def initialize(name, breed, age)
    @name = name
    @breed = breed
    @age = age
  end

  def info
    puts "#{@name}, the #{@age} year old #{@breed}."
  end

  def birthday
    @age += 1
    puts "Happy birthday #{@name}! You're now #{@age} years old."
  end

  def greet(message)
    puts "#{message} #{@name}!"
  end

end

my_dog = Dog.new("Lily", "Pit Mix", 8)
puts my_dog #=> #<Dog:0x007f8c3d05d630>
puts my_dog.name #=> Lily

my_dog.info #=> Lily, the 8 year old Pit Mix.
my_dog.birthday #=> Happy birthday Lily! You're now 9 years old.
my_dog.greet("Hello") #=> "Hello Lily!"

my_dog.breed = "Pitbull"
my_dog.info #=> Lily, the 9 year old Pitbull.
```

### JavaScript
---

```javascript

class Dog {

  constructor(name, breed, age) {
    this.name = name
    this.breed = breed
    this.age = age
  }

  info() {
    console.log(`${this.name}, the ${this.age} year old ${this.breed}.`)
  }

  birthday() {
    this.age++
    console.log(`"Happy birthday ${this.name}! You're now ${this.age} years old."`)
  }

  greet(message) {
    console.log(`${message} ${this.name}!`)
  }

}

my_dog = new Dog("Lily", "Pit Mix", 8)
console.log(my_dog) //=> Dog { name: 'Lily', breed: 'Pit Mix', age: 8 }
console.log(my_dog.name) //=> Lily

my_dog.info //=> [Function: info]
my_dog.info() ) //=> Lily, the 8 year old Pit Mix.
my_dog.birthday() //=> Happy birthday Lily! You're now 9 years old.
my_dog.greet("Hello") //=> "Hello Lily!"

my_dog.breed = "Pitbull"
my_dog.info() //=> Lily, the 9 year old Pitbull.
```

### Python
---

```python

class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
  def info(self):
    print("{}, the {} year old {}.").format(self.name, self.age, self.breed)
  def birthday(self):
    self.age += 1
    print("Happy birthday {}! You're now {} years old.").format(self.name, self.age)
  def greet(self, message):
    print("{} {}!").format(message, self.name)


my_dog = Dog("Lily", "Pit Mix", 8)
print(my_dog) #=> <__main__.Dog instance at 0x10fe525f0>
print(my_dog.name) #=> Lily

my_dog.info #=> <bound method Dog.info of <__main__.Dog instance at 0x10fe525f0>>
my_dog.info() #=> Lily, the 8 year old Pit Mix.
my_dog.birthday() #=> Happy birthday Lily! You're now 9 years old.
my_dog.greet("Hello") #=> "Hello Lily!"

my_dog.breed = "Pitbull"
my_dog.info() #=> Lily, the 9 year old Pitbull.
```

### PHP
---

```php

class Dog {

  function __construct($name, $breed, $age) {
    $this->name = $name;
    $this->breed = $breed;
    $this->age = $age;
  }

  function info() {
    echo "{$this->name}, the {$this->age} year old {$this->breed}.";
  }

  function birthday() {
    $this->age++;
    echo "Happy birthday {$this->name}! You're now {$this->age} years old.";
  }

  function greet($message) {
    echo "{$message} {$this->name}!";
  }

}

$my_dog = new Dog("Lily", "Pit Mix", 8);
print_r($my_dog);
//=> Dog Object
// (
//     [name] => Lily
//     [breed] => Pit Mix
//     [age] => 8
// )
echo $my_dog->name; //=> Lily

echo $my_dog->info(); //=> Lily, the 8 year old Pit Mix.
$my_dog->birthday(); //=> Happy birthday Lily! You're now 9 years old.
$my_dog->greet("Hello"); //=> "Hello Lily!"

$my_dog->breed = "Pitbull";
$my_dog->info(); //=> Lily, the 9 year old Pitbull.
```

# Breakdown
---

### Initializing / Constructing

Whenever you create a new class, anything inside this pre-defined function will

```ruby
# Ruby
def initialize(name, breed, age)
  @name = name
  @breed = breed
  @age = age
end
```

JavaScript
Python
PHP




# Inheritance
---



---

Hopefully this will let you program much cleaner (and reusable) code.

Code on.

Mike Merin
