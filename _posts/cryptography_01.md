---
layout: post
title:  "Making New Code: Ruby and Cryptography"
date:   2017-04-17 13:58:14 -0400
categories: cryptography
---

Want a custom password only you knew how to make? Want to write your own code to customize it even more? How about sending a coded message to another person and encrypting/decrypting it yourselves?

<img src="http://www.youdeparted.com/images/aesencrypt.gif">

Well here’s something you may not already realize: you use encryption every single day. Ever send a text or an email? Once those messages are sent they get encrypted automatically to make them look like a jumble of random characters. That is until the person you sent them to receives them, has them decrypted, and can read what you sent them. This way no one other than you two knows what you said!

I was gifted [The Code Book][simonsingh.net/books/the-code-book/] by Simon Singh over the holidays, and while the “code” in it meant ciphers and cryptography, like Morse Code or using code words, my mind right to the other type of “code” being programming. There were plenty of websites devoted to encrypting and decrypting various ciphers, but the fun is in doing it yourself. Ready to do that?

<i>Fair warning this will be a VERY long blog post because I’ll be explaining things down to the tiniest detail for those just starting to code. My subsequent posts will be more direct, and if you have any questions you can just comment or message me for clarification. That being said I hope even those who are experts in Ruby will enjoy the process!</i>

****putTitleHeaderHere******
<h3>Cipher Types</h3>

Before we get into the ciphers themselves I’ll cover the basic coding part first and then we’ll kick it into high gear quickly. If you don’t know anything about code then this will help you learn, and even if you’re an expert pay attention so you can write your own complex encryptions.

You may have heard of the following types of ciphers: Caesar Shift, Rail-Fence, The Enigma Code, or Public-Key-Cryptography.

****insert images of these types here****

Let’s start simple with a Monoalphabetic Cipher, which simply means we’ll substitute one letter with another, e.g. A = B, B = C, etc. If you’ve seen the puzzle section of the newspaper you may have noticed a cryptoquote puzzle which is in fact a monoalphabetic cipher.

****insert cryptoquote here****

You may not have realized it but Morse Code is also one of these ciphers! In this case we’re substituting a symbol or pattern with a letter: A = .- B = -... etc.

****insert morse code here****

<h3>Writing Your Encryption Program</h3>

So how would we write a program to convert, or “encrypt” letters into Morse Code? Well there are three words you’ll want to keep in mind before we start: <u>hash</u>, <u>object</u>, and <u>iteration</u>. Don’t worry these things are simple and I’ll explain each of these as I go along.

In human terms we have to tell our program: “make A equal .- then make B equal -…“ and so on. A simple way to do this is to use what’s known as a <u>hash</u> which stores data like a dictionary. An example of what this looks like is:

```ruby
{ “Ruby” => “An object oriented language.” }
```

So the word “ruby” is defined as “An object oriented language”. The association here is <b>Word => Definition</b>, or more commonly known to programmers as <b>Key => Value(s)</b>. Let’s take this even further and name this hash:

`my_dictionary = { “Ruby” => “An object oriented language.” }`

And just like that, <b>my_dictionary</b> is an object that stores this information! Great again, but how do we use it? Well it’s simple! We can pull information from the my_dictionary object like this:

`my_dictionary[“Ruby”] #=> “An object oriented language.”`

We call the word (key) “Ruby” on the object my_dictionary and it outputs the desired definition (value). Let’s do the same thing with Morse Code! Here’s our hash stored in an object:

```ruby
Morse_code = { "a" => ".-", "b" => "-...", "c" => "-.-.", "d" => "-..", "e" => ".", "f" => "..-.", "g" => "--.", "h" => "....", "i" => "..", "j" => ".---", "k" => "-.-", "l" => ".-..", "m" => "--", "n" => "-.", "o" => "---", "p" => ".--.", "q" => "--.-", "r" => ".-.", "s" => "...", "t" => "-", "u" => "..-",  "v" => "...-", "w" => ".--", "x" => "-..-", "y" => "-.--", "z" => "--..", " " => " ", "1" => ".----", "2" => "..---", "3" => "...--", "4" => "....-", "5" => ".....", "6" => "-....", "7" => "--...", "8" => "---..", "9" => "----.", "0" => "-----", "?" => "..--.." }
```

Now we can convert our letters by doing the following and calling:

```ruby
Morse_code[“h”] #=> ....
Morse_code[“e”] #=> .
Morse_code[“l”] #=> .-..
Morse_code[“l”] #=> .-..
Morse_code[“o”] #=> ---`
```

We’re basically calling the letter (key) on the object Morse_code to output the Morse Code symbols (value) for each letter!

<h3>Iteration</h3>

Now the final problem: what if you have a sentence to convert? We don’t want to do this for every single letter right? That’d be tedious and unnecessary, so the next step is doing this is our final word we kept in mind from before: iteration. We’ll use a simple “while” statement first to do this before making the entire thing into a short one-line solution, yes, one line. First let’s make our sentence into an object:
sentence = “here is a sentence.”
So let’s once again think about this in human terms:
Start at the first letter in the sentence
Convert that letter to Morse Code
Go to the next letter
Convert that letter to Morse Code
Keep doing this until we reach the end of the sentence.
Now the beautiful thing about code is that there are multiple ways to solve a problem! We’ll end with that short one-line solution, but in order to understand how to do it we’ll start with simple-yet-long way in the above steps:
Start at the first letter in the sentence
In programming we start counting at 0, not 1. Let’s set an object “index” equal to 0.
index = 0
So now if we call the index on our sentence, we’ll get the first letter of “h”
sentence[index] #=> “h”
Convert that letter to Morse Code
So let’s call the letter “h” into our Morse_code object/hash:
Morse_code[sentence[index]] #=> “....“
Go to the next letter
Convert that letter to Morse Code
It’s time for iteration! How do we go to the next letter? Well we have our index of 0 which is the first letter, let’s make that equal 1 which is the second letter. We can do this by
index = index + 1
Or the simpler
index += 1
So now with index equal to 1 we can call the index on our sentence:
sentence[index] #=> “e”
Morse_code[sentence[index]] #=> “.“
Keep doing this until we reach the end of the sentence.
How do we know we’ve reached the end of the sentence? There’s a neat thing we can do to figure out the length of our sentence:
sentence.length #=> 18
So we know the length, or size of the sentence is 18 characters long. (side-note: “length” and “size” are the same thing. I prefer to use size which is shorter). So we basically have to say “wntil the index reaches 18, keep converting the letters to Morse Code,” or “while the index is less than the size of the sentence, keep converting the letters to Morse Code. We’d write both of these as:
until index == sentence.size
while index < sentence.size
And bringing it all together we’d write the entire while loop as:
index = 0
while index < sentence.size
	puts Morse_code[sentence[index]]
	index += 1
end
This will put each letter on a new line. Let’s take this further though and store the Morse Code as a new sentence. We can make an object morsed_sentence and add each Morse Code letter to it:
converted_sentence = ""
index = 0
while index < sentence.size
    converted_sentence += Morse_code[sentence[index]]
    index += 1
end
converted_sentence #=> "......-.. ..... .- ....-.-.-.-.-.."
Oops! While English letters can be read next to one another, Morse Code needs a space between each letter otherwise we can’t discern what they are. Let’s add that space to our code to fix this by using + ” “ at the end of each letter:
converted_sentence = ""
index = 0
while index < sentence.size
    converted_sentence += Morse_code[sentence[index]] + “ “
    index += 1
end
converted_sentence #=> ".... . .-. .   .. ...   .-   ... . -. - . -. -.-. ."
We can also do this using an Array. Side-lesson: arrays stores information like this:
array = [“here”,”is”,”an”,”array”]
and we can push new things into the array by using a shovel:
array << “hooray!”
array #=>  [“here”,”is”,”an”,”array”,”hooray!”]
where each element in the array is split up with a comma. If we use join we can join them together. Using join(“ “) adds a space between each element:
array.join #=> hereisanarrayhooray!
array.join(“ “) #=> here is an array hooray!
array.join(“ :) “) #=> here :) is :) an :) array :) hooray!
So let’s convert into Morse Code using arrays!
converted_sentence = []
index = 0
while index < sentence.size
    converted_sentence << Morse_code[sentence[index]]
    index += 1
end
converted_sentence #=> ["....", ".", ".-.", ".", " ", "..", "...", " ", ".-", " ", "...", ".", "-.", "-", ".", "-.", "-.-.", "."]
converted_sentence.join(“ “) #=> ".... . .-. .   .. ...   .-   ... . -. - . -. -.-. ."
OK so I said there were three words to keep in mind but I’ll add another one into the mix: method. All this means is we’ll be putting all the above into something neat and tidy so we can run it all once. Let’s define our method as convert_to_morse_code and have it take in a sentence:
def convert_to_morse_code(sentence)
converted_sentence = []
index = 0
while index < sentence.size
    converted_sentence << Morse_code[sentence[index]]
    index += 1
end
return converted_sentence
end
The method will return the converted sentence to us and we don’t have to copy down all those long steps every single time we want to convert something to Morse Code! We can simply do:
convert_to_morse_code(“here is a sentence”) #=> ".... . .-. .   .. ...   .-   ... . -. - . -. -.-. ."
convert_to_morse_code(“simple right?”) #=> "... .. -- .--. .-.. .   .-. .. --. .... - ..--.. "
Another side-lesson: in a method you don’t actually have to put the word “return” down for the last line, a method will return the last value no matter what.
Now for true iteration to make this a single line long. To know how to do this we need to know more words. Yes I said you’d have to know three at the start, and we got to four with method. Well that’s true for the simple stuff above, but we’re in the thick of it now and learning more complicated iterations. First up is a range which is easy enough. If you want to go from 0 to 60, we’d use (0..60) where the .. means range. In the case of our sentence which is 18 characters long we’d use:
(0..sentence.size)
Here we’re going from 0 to 18, or (0..18). Something’s wrong though; our sentence is 18 characters long, aka it has 18 characters in it, but If we call sentence[18] we’ll get nil. Why? Remember we start counting at 0 not 1, so even though in English we’d count the letters from 1 to 18, we’d have to count in code from 0 to 17. This means the final letter is at sentence[17] so we’d have to subtract one from the end of our range:
(0..sentence.size - 1)
Or a fancy little trick is to use ... instead of .. for our range, which instead says “go up until the number. So (0…18) says “go from 0 up until 18, or 0 to 17”. We’d then be able to simply say:
(0...sentence.size)
And not get nil or cause errors. As for iterating we’ll use each. Each basically says “do something_I_want for each one”. In this case: (0...sentence.size).each would go over each number from 0 to 17 in our sentence. We can then use blocks to tell the “each” to do something for us! We can do something fancy like this:
(0...6).each do |number|
print number
end
#=> 012345
or: (0...6).each { |number| print number } #=> 012345
The |number| is the item we’ll be using in the block which is either surrounded by “do end” or the curly brackets “{}”. In this case the number is each number in our range of (0..6) which prints out each number. So with this all in mind let’s write our one-liner using our previous code!
def convert_to_morse_code(sentence)
morsed_sentence = []
(0...sentence.size).each { |index| morsed_sentence << Morse_code[sentence[index]] }
morsed_sentence.join(“ “)
end
convert_to_morse_code(“here is a sentence”) #=> ".... . .-. .   .. ...   .-   ... . -. - . -. -.-. ."
But wait that’s three lines, not one! Well if we use map or collect (same thing) instead of each, which maps/collects the values and changes them all at once we can finally do our one-liner:
def convert_to_morse_code(sentence)
(0...sentence.size).map { |index| Morse_code[sentence[index]] }.join(" ")
end
Horray! Oh right we can make this even simpler. Instead of iterating from 0 to 17, let’s just call each on the sentence itself! We can split up the sentence’s characters into an array by using split(“”) or chars:
“hi there”.split #=> [“hi”, ”there”]
“hi there”.split(“”) #=> ["h", "i", " ", "t", "h", "e", "r", "e"]
“hi there”.chars #=> ["h", "i", " ", "t", "h", "e", "r", "e"]
 And then iterate over them like this:
def convert_to_morse_code(sentence)
sentence.chars.map { |letter| Morse_code[letter] }.join(" ")
end
This is less code we’ll have to write! And now that we’ve written this, here’s the fun thing: because Morse Code is a monoalphabetic cipher we can now use this code for ANY of those ciphers! A Caeser Cipher shifts all the letters down, so if we did that by one letter:
Caesar_cipher = { "a" => "b", "b" => "c", "c" => "d", "d" => "e", "e" => "f", "f" => "g", "g" => "h", "h" => "i", "i" => "j", "j" => "k", "k" => "l", "l" => "m", "m" => "n", "n" => "o", "o" => "p", "p" => "q", "q" => "r", "r" => "s", "s" => "t", "t" => "u", "u" => "v",  "v" => "w", "w" => "x", "x" => "y", "y" => "z", "z" => "a", " " => " " }
def convert_to_caesar_cipher(sentence)
sentence.chars.map { |letter| Ceaser_cipher[letter] }.join(" ")
end
convert_to_caesar_cipher(“here is a sentence”) #=> "ifsf jt b tfoufodf"
Or how about an Atbash cipher which reverses A and Z, B and Y, C and X, and so on?
Atbash_cipher = { "a" => "z", "b" => "y", "c" => "x", "d" => "w", "e" => "v", "f" => "u", "g" => "t", "h" => "s", "i" => "r", "j" => "q", "k" => "p", "l" => "o", "m" => "n", "n" => "m", "o" => "l", "p" => "k", "q" => "j", "r" => "i", "s" => "h", "t" => "g", "u" => "f",  "v" => "e", "w" => "d", "x" => "c", "y" => "b", "z" => "a", " " => " " }
def convert_to_atbash_cipher(sentence)
sentence.chars.map { |letter|atbash_cipher[letter] }.join(" ")
end
convert_to_atbash_cipher(“here is a sentence”) #=> "sviv rh z hvmgvmxv"
And so on and so on. With some slight modifications we can even convert Morse Code back to English! Use invert to invert our morse_code object/hash:
Morse_code.invert #=> {".-"=>"a", "-..."=>"b", "-.-."=>"c", "-.."=>"d", "."=>"e", "..-."=>"f", "--."=>"g", "...."=>"h", ".."=>"i", ".---"=>"j", "-.-"=>"k", ".-.."=>"l", "--"=>"m", "-."=>"n", "---"=>"o", ".--."=>"p", "--.-"=>"q", ".-."=>"r", "..."=>"s", "-"=>"t", "..-"=>"u", "...-"=>"v", ".--"=>"w", "-..-"=>"x", "-.--"=>"y", "--.."=>"z", " "=>" ", ".----"=>"1", "..---"=>"2", "...--"=>"3", "....-"=>"4", "....."=>"5", "-...."=>"6", "--..."=>"7", "---.."=>"8", "----."=>"9", "-----"=>"0", "..--.."=>"?"}
def convert_from_morse_code(sentence)
sentence.split.map { |letter|Morse_code.invert[letter] }.join(" ")
end
convert_from_morse_code(".... . .-. .   .. ...   .-   ... . -. - . -. -.-. .") #=> "h e r e i s a s e n t e n c e"
We understand this but we get weird spacing issues since our Morse Code converting adds spaces, but Ruby splits up based on any number of spaces, so with a quick modification:
def convert_from_morse_code(sentence)
words = sentence.split("   ") #=> [".... . .-. .”, “.. ...”, “.-“, “... . -. - . -. -.-. ."]
words.map { |word| word.split(" ").map { |letter| Morse_code.invert[letter] }.join }.join(" ")


end

Basically we break apart the spaces into words:
[".... . .-. .”, “.. ...”, “.-“, “... . -. - . -. -.-. ."]
Then again into individual letters:
[["....", ".", ".-.", "."], ["..", "..."], [".-"], ["...", ".", "-.", "-", ".", "-.", "-.-.", "."]]
Convert each letter to Morse Code, join up the letters directly, and then join up the words with a space. Like I said before, there’s always a different way to make all of these codes work with programming. We can also use gsub to make it look neater . and for example with the atbash cipher we can convert each letter to its ASCII number, change it, and convert it back to a letter:
“hello”.chars.map { |x| ((27-(x.ord - 96))+96).chr }.join #=> "znzav"
We can use regex to scan for which letters we want to change and return:
“hello”.scan(/[a-z]/).map { |x| ((27-(x.ord - 96))+96).chr }.join #=> "znzav"
And we can modify it to only run atbash on letters (ignoring things like punctuation or spaces)
sentence.chars.map { |x| ("a".."z").include?(x) ? ((27-(x.ord - 96))+96).chr : x }.join
And since a Caesar Cipher is simply shifting the alphabet, we can create our hash using rotate and zip without having to painstakingly do it ourselves!
alphabet = ("a".."z").to_a
Hash[alphabet.zip(alphabet.rotate(1))] #=> {"a"=>"b", "b"=>"c", "c"=>"d", etc. Hash[alphabet.zip(alphabet.rotate(2))] #=> {"a"=>"c", "b"=>"d", "c"=>"e", etc. }
And yes that’s right, we can use other things like reverse to recreate atbash:
Hash[alphabet.zip(alphabet.reverse)] #=> {"a"=>"z", "b"=>"y", "c"=>"x", etc. }
The possibilities are endless:
lowercase = ("a".."z").to_a
uppercase = ("A".."Z").to_a
Hash[(lowercase + uppercase).zip((1..52).to_a)] #=> {"a"=>1, "b"=>2, … "Z"=>52}
Letters to their number?
numbers = (1..26).to_a
Hash[alphabet.zip(numbers)] #=> {"a"=>1, "b"=>2, "c"=>3, etc. }
binary = (1..26).map { |x| x.to_s(2).to_i }
Hash[alphabet.zip(binary)] #=> {"a"=>1, "b"=>10, "c"=>11, "d"=>100, etc. }
And just like before with any of these, we’d simply call upon this hash to convert our alphabet to our custom monoalphabetic ciphers!
Again sorry for this long post; next time I’ll get right to the chase without this in-depth tutorial to cover the Vigenère Cipher, including outputting a visual histogram with basic Ruby!


Mike Merin
