---
layout: post
title:  "Object Orientation in Four Languages"
subtitle: "OO 101"
date:   2017-12-11 22:06:15 -0400
categories: Ruby, JavaScript, Python, PHP, tutorial
---
Object Oriented Programing, or OOP is an incredibly important tool for developers to know. If you know one language and are trying to learn another, learning methods, iterations, and basic structure may be easier to learn (shameless plug for my [educational posts](https://mikemerin.github.io/education) on learning them), but the nuances of OOP may be harder to grasp, especially if it's your first language.

This post will go through Ruby, JavaScript, Python, and PHP, showing the basic similarities between each of the languages to get your feet on the ground. I'll first give a full example from each language, then I'll go piece by piece to explain what they actually do.

# Ruby
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

end

dog = Dog.new("Lily", "Pit Mix", 8)
puts dog #=> #<Dog:0x007f8c3d05d630>
puts dog.name #=> Lily
puts dog.info #=> Lily, the 8 year old Pit Mix.
```

# JavaScript
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

}

dog = new Dog("Lily", "Pit Mix", 8)
console.log(dog) //=> Dog { name: 'Lily', breed: 'Pit Mix', age: 8 }
console.log(dog.name) //=> Lily
console.log(dog.info) //=> [Function: info]
console.log( dog.info() ) //=> Lily, the 8 year old Pit Mix.
```

# Python
---

```python

class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
  def info(self):
    print("{}, the {} year old {}.").format(self.name, self.age, self.breed)

dog = Dog("Lily", "Pit Mix", 8)
print(dog) #=> <__main__.Dog instance at 0x10fe525f0>
print(dog.name) #=> Lily
print(dog.info) #=> <bound method Dog.info of <__main__.Dog instance at 0x10fe525f0>>
print( dog.info() ) #=> Lily, the 8 year old Pit Mix.
```

# PHP
---

```php

class Dog {

  public function __construct($name, $breed, $age) {
    $this->_name = $name;
    $this->_breed = $breed;
    $this->_age = $age;
  }

  public function info() {
    echo "{$this->_name}, the {$this->_age} year old {$this->_breed}.";
  }

}

$dog = new Dog("Lily", "Pit Mix", 8);
print_r($dog);
//=> Dog Object
// (
//     [_name] => Lily
//     [_breed] => Pit Mix
//     [_age] => 8
// )
echo $dog->_name; //=> Lily
echo $dog->info(); //=> Lily, the 8 year old Pit Mix.
```

Code on.

Mike Merin
