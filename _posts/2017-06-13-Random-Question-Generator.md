---
layout: post
title:  "Anatomy of a Random Question Generator"
subtitle: "Creating a dynamic quiz"
date:   2017-06-17 11:54:14 -0400
categories: ruby, javascript, generators
---
Please note that this post is a work in progress. I have noted the point in where I will continue below.
---
***

There are plenty of quizzes online, however if you take it again you'll already know the answers and will get 100%. Sometimes the quiz will randomize the order of the questions, but you'll still know them. Sometimes the quiz have a larger question bank to choose from, but after taking the quiz enough times you'll know all their answers as well.

When it comes to learning new skills through quizzes, this obviously is a problem as you'll end up learning the answers and not actually mastering the subject. The more questions the better, but there's only so many questions someone will manually add before it gets tiring.

With that being said, how was I able to add 200,000 possible questions to a test in only 2 days? No it wasn't from impossibly fast typing. In order to do this I wrote a program that would dynamically generate a question on the spot that could be one of 200,000 possible combinations. The quiz type? If my previous blog posts and projects were any indication of the types of programs I've written so far, of course it would be a programming education quiz.

# Programming Languages
---
I started with the first language I learned: Ruby, with an eye on moving to Javascript afterward. The value of the generator was that eventually you'd be able to use it with any number of programming languages, and the first thing you learn in a new language are methods. These are the building blocks and are key to getting data do what you want, and is extremely pivotal in code challenges or interviews.

I looked for the methods that would be most helpful to master using. The initial list was:

Methods |
---|---
select | reject | find | detect
delete_if | keep_if | pop | shift
push | unshift | insert|

In addition, I wanted there to be three different ways a question could be asked: **Multiple Choice**, **True or False**, and **Enter the Correct Answer**.

I could create separate quizzes for each of these methods, and sure sure it would be good to randomly choose one of these methods and output a question, but this once again comes back to the first problem of making sure each of these questions were different from each other and not having to manually make each of them. Not only that but what if I wanted to do multiple choice? Would I have to create every single wrong choice?

Taking a look at what would need to be done to make a large number of different questions, I had to think about what I'd be calling the methods **on**. Arrays are a good way to teach about selection, manipulation, and iterating, so what if the arrays we used changed every single time we generated a new question?

# Array Generation
---
Dynamically creating arrays would automatically increase the questions asked as it would apply to every single method on the list above, and any new ones added to it. I could easily create an array from 1-6, 2-7, 3-8, and 4-9. They'd look like:
```ruby
[1, 2, 3, 4, 5, 6]
[2, 3, 4, 5, 6, 7]
[3, 4, 5, 6, 7, 8]
[4, 5, 6, 7, 8, 9]
```
Great that's 4 possibilities right off the bat. To actually choose one of these randomly though without having to actually save them I dynamically generated them by choosing a random number from 1-4, then creating an incrementing array with 6 elements:
```ruby
random = rand(1..4)
# start array at this number
array = Array.new(6) { |x| x + random }
# create a 6-element incrementing array
```
***possible questions = 4***

Now that we had our arrays, we could do some really fun stuff with them. How about half of the time we reverse the arrays? Using the `.sample` method along with a ternary operator I randomly (50/50) chose true or false to reverse the array or not:
```ruby
array = [true,false].sample ? array.reverse : array
```
***possible questions = 8***

It may not seem like much, but multiplying the possibilities by 8 right off the bat means any other changes we do will already have a large start.

# Comparisons
---
The first 6 methods on the list use one of 6 comparisons like less than `<`, greater than or equal to `>=`, or not equal to `!=`. I decided not to choose equal or not equal since if I used multiple choice I'd sometimes generate the same answers, which obviously would be a problem. I put all the comparisons in an array then chose one at random.

```ruby
comparisons = ["<",">",">=","<="]
comparison_selection = comparisons.sample
```
***possible questions = 32***

I'll be changing the comparison script further down the line, but wait a second, if I'm calling a comparison on an array, I'll need a number as well. After all if I have an array of numbers between 1 and 6 and I want a number less than `x`, what's `x`? Well I'll just choose one of the six numbers in the array!

```ruby
array_selection = array.sample
```
***possible questions = 192***

Just like that we have almost 200 different combinations *JUST* from making different arrays and comparisons! See, if we didn't start out with that number 8 before we'd only be at 24 by this point. Putting this to the test we have:

```ruby
random = rand(1..4)
# 4
array = Array.new(6) { |x| x + random }
# [4, 5, 6, 7, 8, 9]
array = [true,false].sample ? array.reverse : array
# true => [9, 8, 7, 6, 5, 4]
array_selection = array.sample
# 6
comparisons = ["<",">",">=","<="]
comparison_selection = comparisons.sample
# <
```
If we were using select, we'd get:

```ruby
method = "select"
array.method{ |x| x comparison_selection array_selection}
# this becomes
[4, 5, 6, 7, 8, 9].select{ |x| x < 6 }
```
Obviously the above wouldn't actually work when inputted into Ruby, so let's write something that does, if only to get something showing up.

# Creating a Question and Its Answer
---
What's the answer to the above question? I'll say it shortly so you have a change to guess, however it begs the question: how do I make all of this into workable code to even ask the question? The short and easy answer is "turn it all into a string and output it." To do that we can do something that's a bit messy but it'll serve our purposes just fine:
```ruby
"#{array}.#{method} { |x| x #{comparison_selection} #{array_selection} }"
# which becomes
"[4, 5, 6, 7, 8, 9].select{ |x| x < 6 }"
```
The good thing about this is, our "method" object can be changed to reject, find, detect, keep_if, or delete_if at a moment's notice!
```ruby
method = find
"#{array}.#{method} { |x| x #{comparison_selection} #{array_selection} }"
#=>
"[4, 5, 6, 7, 8, 9].find{ |x| x < 6 }"

method = delete_if
#=>
"[4, 5, 6, 7, 8, 9].delete_if { |x| x < 6 }"
```
And so on for each of those 6 types. So with 8 arrays, 6 methods, 4 comparison selections, and 6 array selections we now have:

***possible questions = 1,152***

What's cool about this as well is even though this is a string, we can get the answer by using `eval`!

```ruby
eval("[4, 5, 6, 7, 8, 9].select { |x| x < 6 }") #=> [4, 5]
eval("[4, 5, 6, 7, 8, 9].find { |x| x < 6 }") #=> 5
eval("[4, 5, 6, 7, 8, 9].delete_if { |x| x < 6 }") #=> [6, 7, 8, 9]
```

Not bad, but of course we can go even farther. We're hard-coding our question but there's some extreme limitations, including the fact that after we ask a question it only exists printed out and the program will never remember it, and therefore we can't use it again down the line. Also there's 5 more methods to go through, and of course these are just the questions without any answers. Actually before we continue, since we have a lot of methods and there are plenty more to come, let's organize them.

# Object Orientation
---
It makes perfect sense to make this program object oriented, as we can then make each question an object, set its attributes like array, method, etc., and then call a quiz type on it. If that question is storing all that information then we can expand it even further to even more types of quizzes or call other methods on it. Let's put everything into a class named `Question`. I'm also going to do a few more things, and I'll explain it as I go along

```ruby
class Question

  # name those four above attributes
  # I only want to be able to manually directly change the method
  # the rest I want read, but only changed through our instance methods
  attr_accessor :method
  attr_reader :array, :array_selection, :comparison_selection

  # we'll start with a chosen method
  # since the four comparison types don't change, we'll also start with them
  def initialize(method)
    @method = method
    @comparisons = ["<",">",">=","<="]
  end

  # put all array creation scripts into one method
  def createArray
    random = rand(1..4)                            # start array at this number
    @array = Array.new(6) { |x| x + random }       # create a 6-element incrementing array
    @array = [true,false].sample ? @array.reverse : @array # 50/50 chance reversing array
    @array_selection = @array.sample                # select one of those elements
  end

  def chooseComparison
    @comparison_selection = @comparison.sample      # choose one comparison
  end

end
```
Now we can create a question by doing `new_question = Question.new("reject")` and the `new_question` object will have all this information stored in it waiting to be used! Let's try that out and see what happens:

```ruby
new_question = Question.new("reject")
#=> <Question:0x007f9ddd926f08 @method="reject", @comparisons=["<", ">", ">=", "<="]>
# initializes with @method of "reject and the @comparisons, nothing else"

new_question.createArray
new_question #=>
# <Question:0x007f9ddd926f08 @method="reject", @comparisons=["<", ">", ">=", "<="],
# @array=[2, 3, 4, 5, 6, 7], @array_selection=3>
# we now have our @array and an @array_selection

new_question.chooseComparison
new_question #=>
# <Question:0x007f9ddd926f08 @method="reject", @comparisons=["<", ">", ">=", "<="],
# @array=[2, 3, 4, 5, 6, 7], @array_selection=3 @comparison_selection="<">
# and now a comparison
```
This info is now all stored in the `new_question` object and can be called at any time, and if we really wanted to we could run the `.createArray` and `.chooseComparison` instance methods on it again to make it into a new question. This would get tedious though so let's create a new method that does this for us, and then let's bring it together by putting it into a string just like before:
```ruby
def createQuestion
  createArray; chooseComparison
  @question = "#{@array}.#{@method} { |x| x #{@comparison_selection} #{@array_selection} }"
end
```
Now we can just use `new_question.createQuestion` and it'll do the above for us. You can see that using object oriented code makes it incredibly easy to add methods to our class and have them be accessible from the start.

# Creating Answers
---
Even though I have the framework for creating a question, I need to make sure there are multiple answers. This is where we're going to REALLY step it up. Our code which has 1,152 possibilities. We can use the prior `eval(string)` trick to create an answer, so let's also add that to our prior code:

```ruby
class Question

  attr_accessor :method
  attr_reader :array, :array_selection, :comparison_selection, :question, :answer

  def initialize(method)
    @method = method
    @comparisons = ["<",">",">=","<="]
  end

  def createArray
    random = rand(1..4)
    @array = Array.new(6) { |x| x + random }
    @array = [true,false].sample ? @array.reverse : @array
    @array_selection = @array.sample
  end

  def chooseComparison
    @comparison_selection = @comparisons.sample
  end

  def createQuestion
    createArray; chooseComparison
    @question = "#{@array}.#{@method} { |x| x #{@comparison_selection} #{@array_selection} }"
  end

  def createAnswer
    @answer = eval(@question)
  end

end

question = Question.new("select")
#=> <Question:0x007f9ddd98c470 @method="select", @comparisons=["<", ">", ">=", "<="]>

question.createQuestion
#=> <Question:0x007f9ddd98c470 @method="select", @comparisons=["<", ">", ">=", "<="],
#    @array=[9, 8, 7, 6, 5, 4], @array_selection=6, @comparison_selection=">=",
#    @question="[9, 8, 7, 6, 5, 4].select { |x| x >= 6 }">

question.createAnswer #=> @answer=[9, 8, 7, 6]
```
Our object now has a question and answer, and notice I have still have them as `attr_reader` not `attr_accessor` as I don't want them to be able to manually be changed, only read.

We also need to prepare for needing a wrong answer for true/false or 3 wrong answers for multiple choice. It's been a while since we mentioned this, so let's just preemptively do this for the 3 question types being randomized:

***possible questions = 3,456***

Let's tackle how we can get four answers for multiple choice, and two answers for true/false (I'll explain why in a bit). Since we need 4 answers for multiple choice, I looked at what also had 4 things to choose from: our comparisons. Since we selected one with `@comparison_selection` why not use the others to generate wrong answers?

If I made a `@mc_answers` array to call on, I could populate it by iterating over the `@comparisons` array and push each answer into it, then shuffle up the choices to give us one of 24 combinations. Basically:
```ruby
  @choices << (eval "#{@array}.#{@method} { |x| x < #{@array_selection} }")
  @choices << (eval "#{@array}.#{@method} { |x| x > #{@array_selection} }")
  @choices << (eval "#{@array}.#{@method} { |x| x >= #{@array_selection} }")
  @choices << (eval "#{@array}.#{@method} { |x| x <= #{@array_selection} }")
  @choices.shuffle!
```
Or more simply:
```ruby
@mc_answers = []
@comparisons.each do |comparison|
    @mc_answers << (eval "#{@array}.#{@method} { |x| x #{comparison} #{@array_selection} }")
end
@mc_answers.shuffle!
```
While we're working our the comparisons, let's redo our `chooseComparison` method. Right now it just picks a random comparison using `@comparison.sample`, but we need to think about how we'll do true/false. It'd be useless if we only gave users a right answer every time as they'd just click true and move on, so we'll also need to give them a wrong answer as well half of the time. If we simply choose a second comparison we'd require a check to make sure it's not the same random sample as before (like using `.include?`) but that would add more lines of code and make it messier. Instead we can simply choose the first comparison as the correct one and the second one as the wrong one! We'll also shuffle our comparisons first to make sure it's not the same every time.

```ruby
def chooseComparison
    @comparison_selection = @comparisons.shuffle[0]  # select correct comparison
    @comparison_rejection = @comparisons[1]          # select wrong comparison
end
```
Yes I'm being cheeky here and using the method names `select` and `reject` as my naming scheme instead of right/wrong. Now that we have a `@comparison_rejection` we can use that to make a false answer:

```ruby
@false_answer = eval "#{@array}.#{@method} { |x| x #{@comparison_rejection} #{@array_selection} }"
```

We'll organize it by adding id to our `createAnswer` instance method. I'm also going to make a method called `generateQuestion` which will run these methods for us. With that, how does our code look now put together?

```ruby
class Question

  attr_accessor :method
  attr_reader :array, :array_selection, :comparison_selection, :comparison_rejection, :question, :answer, :mc_answers

  def initialize(method)
    @method = method
    @comparisons = ["<",">",">=","<="]
  end

  def createArray
    random = rand(1..4)
    @array = Array.new(6) { |x| x + random }
    @array = [true,false].sample ? @array.reverse : @array
    @array_selection = @array.sample
  end

  def chooseComparison
      @comparison_selection = @comparisons.shuffle[0]  # select correct comparison
      @comparison_rejection = @comparisons[1]          # select wrong comparison
  end

  def createQuestion
    @question = "#{@array}.#{@method} { |x| x #{@comparison_selection} #{@array_selection} }"
  end

  def createAnswers
    @answer = eval(@question)
    @wrong_answer = eval "#{@array}.#{@method} { |x| x #{@comparison_rejection} #{@array_selection} }"
    @mc_answers = []
    @comparisons.each do |comparison|
        @mc_answers << (eval "#{@array}.#{@method} { |x| x #{comparison} #{@array_selection} }")
    end
    @mc_answers.shuffle!
  end

  def generateQuestion
    createArray; chooseComparison; createQuestion; createAnswers
  end

end

question = Question.new("select")
question.generateQuestion
#=> <Question:0x007f9ddd90fe70 @method="select", @array=[1, 2, 3, 4, 5, 6],
#   @comparisons=["<", ">", ">=", "<="],
#   @array_selection=3, @comparison_selection=">",
#   @question="[1, 2, 3, 4, 5, 6].select { |x| x > 3 }",
#   @answer=[4, 5, 6], @comparison_rejection=">", @wrong_answer=[4, 5, 6],
#   @mc_answers=[[3, 4, 5, 6], [4, 5, 6], [1, 2, 3], [1, 2]]>
```
Now we have a LOT of information stored in our question object, and this works great for select/reject, however there's a problem if we try to use `.find`/`.detect`, and another major problem if we try to use `.keep_if`/`.delete_if`. Here's a problem that will happen with the former:

```ruby
question = Question.new("find")
question.generateQuestion
#=> <Question:0x007f9ddd8f5778 @method="find", @array=[2, 3, 4, 5, 6, 7],
#   @comparisons=["<", ">", ">=", "<="],
#   @array_selection=4, @comparison_selection="<=",
#   @question="[2, 3, 4, 5, 6, 7].find { |x| x <= 4 }",
#   @answer=2, @comparison_rejection=">", @wrong_answer=5,
#   @mc_answers=[2, 5, 4, 2]>
```
See the issue? Look at the `@mc_answers`. Here's the issue we tried to avoid before when we were talking about comparison selection: we have two answers that are the same. Why? `.find` and `.detect` will find the first number that's valid, so going through all the comparisons:

```ruby
["<", ">", ">=", "<="]
[2, 3, 4, 5, 6, 7].find { |x| x < 4 } #=> 2
[2, 3, 4, 5, 6, 7].find { |x| x > 4 } #=> 5
[2, 3, 4, 5, 6, 7].find { |x| x >= 4 } #=> 4
[2, 3, 4, 5, 6, 7].find { |x| x <= 4 } #=> 2
```
Work in Progress is below, I will update this over the next few days.
***

No matter what array or selection we'll always get duplicate answers. The fix is a simple one, and it goes back to what we wanted to avoid: validation via `include?`. I'll handle that shortly, but now we'll cover the latter methods `.keep_if`/`.delete_if`. These are the exact same things as `.select`/`.reject` respectively, however they're **destructive methods**, meaning that after we call them, they'll permanently alter the array, not just the output. So what happens if we populate the choices?
```ruby
question_keep = QUestion.new("keep_if")
question_keep.generateQuestion
#=> <Question:0x007f9dde01e400 @method="keep_if", @array=[],
#   @comparisons=["<", ">", ">=", "<="],
#   @array_selection=8, @comparison_selection="<=",
#   @question="[9, 8, 7, 6, 5, 4].keep_if { |x| x <= 8 }",
#   @answer=[8, 7, 6, 5, 4], @comparison_rejection=">",
#   @mc_answers=[[], [], [], []],  @wrong_answer=[]>
```
Even though we got our correct answer, you'll notice that there's nothing in our `@mc_answers` or `@wrong_answer` because whenever we run the destructive method, the array we try to call it on has already been changed once before by that same method. We'll fix these both soon!

Code on.

Mike Merin