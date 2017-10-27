---
layout: post
title:  "Creating a Rails API and fixing CORS issues"
date:   2017-10-25 13:58:14 -0400
categories: ruby, rails, API, CORS, cross-origin
---

I recently tried to recreate an API for my random question generator, this time letting the front end handle the question creation. I ran into the infamous CORS issue `No 'Access-Control-Allow-Origin' header is present on the requested resource.` I ran into this issue before and it took a litle while to find the answer to it again, so I figure I'd go through the simple steps of how to create a rails API from scratch and fix the issue as I go.

If you're just interested in how to fix a CORS issue you can skip ahead to [here](https://mikemerin.github.io/Rails-API-cors#CORS).

# Tools

Ruby: There are a few ways to get Ruby installed on your computer but many roads lead [here](https://www.ruby-lang.org/en/documentation/installation/)

Rails: Connecting Ruby to the online world. You can find the guide to installing Rails [here](http://installrails.com/)

Database: Since you're creating an API you'll need to have a database program on your computer. You can use the clean and useful [DB Browser for SQLite](http://sqlitebrowser.org/), or my preferred [postgresql](https://www.postgresql.org/) which is much faster and advanced.

IDE: a way to view your files. IDE stands for "integrated development environment" and it's what developers use to create and edit their files, in fact I'm using one right now for this blog post! My favorite is [Atom](https://atom.io/), others like [Sublime](https://www.sublimetext.com/).

# Creating the application

Rails makes it incredibly easy to create a basic application from scratch. No needing to manually configure the little things like you need to with Sinatra, just type in the terminal commands and you're good to go. We're going to create a new API called `test_api`. The easiest way to do this is type in:

`rails new test_api --api`

or if like me you like Postgresql better you can instead type in:

`rails new test_api --api --database=postgresql -T`

Once the flurry of text finishes, you'll notice a new folder called `test_api`. If you `cd test_api` to go into the folder you'll see it contains files like a Gemfile, Rakefile, config, readme, etc. I won't go into detail about what each of them do right now, but technically you just made an API! Grats, now to get it working correctly.

# MVC

A quick note about the framework that Rails uses before we continue: MVC stands for "model, view, controller":

* Models: the data of your app, objects where you can store and retrieve information
* Views: as the name says, this is what a user will see and interact with
* Controllers: the logic that dictates how your app will behave

Since this is an API we won't be working with views. After all we're just after data and don't need to build a website for a user to interact with. That can either be later down the line, or more preferrably handled in a separate app on the front end.

# Model generation

We're going to make a little music API that has artists and songs. Rails once again makes this part easy for us. We can type in the terminal the following to create our two models:

`rails generate resource Artist _________`

or the shorter

`rails g resource Artist _________`

We can generate many things this way: a migration, a model, a controller, etc., but we use `resource` in this case since it will create the model, controller, and the routes we need to connect to. We'll want our Artist to contain certain information like the artist's name, origin, and its genre. We'll also want the songs to have a name, artist_id (since we have an artist model to link it to), album name, and length. Here's how we'll generate our models:

`rails g resource Artist name origin genre`
`rails g resource Song name artist_id:integer album length`

If you noticed our `artist_id` has an integer attached to it. All of these attributes will default to a string, but if we wanted to we can make them into other data types like an integer like the `artist_id:integer` above, or a boolean `active:boolean`.

Once you type these in you'll get another bit of text, including invoking active_record, controller, and routes along with creating the necessary files which I'll cover shortly. A quick note that **ActiveRecord** is very important in making your API work and you'll see its name pop up quite a bit in your program, but getting into that will take a much longer time so I'll leave that for another post.

If you'd like to see where this model generation occurs, look at the `create    db/migrate/20171025192202_create_artists.rb` line. The `/db/migrate` folder contains files with a string of numbers (the date and time you did your `rails g` model generation), create, and then the model you made. Opening up the artists file:

```ruby
class CreateArtists < ActiveRecord::Migration[5.1]
  def change
    create_table :artists do |t|
      t.string :name
      t.string :origin
      t.string :genre

      t.timestamps
    end
  end
end
```

you'll see the class `CreateArtists` that inherits an Active Record migration. Inside this class is a change method, then the artists table creation which includes your name origin and genre strings as the columns to your table, along with some timestamps which give you info about the creation time and last modified time of any row you add to your table.

You now have your models!

# Model relationships

Onto the `create    app/models/artist.rb` line. Here is where we can add some logic to the models such as validations, keys, aliases, or what we'll be focusing on: relationships. Relationships are ways that you can make different tables interact with one another in a variety of ways.

Opening up the `app/models` folder there will be an `application_record.rb` which we don't need to worry about, just to keep in mind that it connects to Active Record once again, this time to the base to handle how the tables behave. If you open up `artist.rb` and `song.rb` you'll see:

```ruby
# app/models/artist.rb
class Artist < ApplicationRecord
end

# app/models/song.rb
class Song < ApplicationRecord
end
```

Here's where we'll add in some relationships. Thinking about it logically, an artist can have many songs, which means that songs belong to an artist. This is known appropriately as a **has-many belongs-to** relationship, and it's easy enough to put into our models:

```ruby
# app/models/artist.rb
class Artist < ApplicationRecord
  has_many :songs
end

# app/models/song.rb
class Song < ApplicationRecord
  belongs_to :artist
end
```

Other relationships include many-to-many, one-to-one, etc., examples which you can find [here](https://code.tutsplus.com/articles/sql-for-beginners-part-3-database-relationships--net-8561). The thing to keep in mind is that if you have many of something then the table name will be plural, like `has_many :songs` above, and if there's only one thing it will be singular like `belongs_to :artist` above or `has_one :artist`.

I'll cover how we can use these relationships later on, but bascially this allows us to say "give me an artist's songs", or "give me the artist this song belongs to". I mentioned before when talking about **artist_id** that we had the artist model to link it to. We just made that link using relationships so an artist with an ID of 1 and a song with an artist_id of 1 will automatically be linked together!

# Migrating your models into tables

We have our models set up but no actual tables are made. We have to run a few commands to actually make your table but again it's very simple to do. The `rake` commands will help us through the process and handle everything for us. Here are the strings of commands to type in:

`rake db:create` (creates the basic databases)

```bash
Created database 'test_api_development'
Created database 'test_api_test'
```

`rake db:migrate` (puts the models you generated into the database)

```bash
== 20171025192202 CreateArtists: migrating ====================================
-- create_table(:artists)
   -> 0.0337s
== 20171025192202 CreateArtists: migrated (0.0338s) ===========================

== 20171025192209 CreateSongs: migrating ======================================
-- create_table(:songs)
   -> 0.0111s
== 20171025192209 CreateSongs: migrated (0.0112s) =============================
```

`rake db:migrate RAILS_ENV=development` (same thing, but migrates into the dev database)

Now you can load up your Rails console by typing in `rails c` and see your database and models! Type in `Artist` or `Song` to see your tables (you may have to do Artist.connection first to connect to the database)

```ruby
# Artist
Artist(id: integer, name: string, origin: string, genre: string, created_at: datetime, updated_at: datetime)

# Song
Song(id: integer, name: string, artist_id: integer, album: string, length: string, created_at: datetime, updated_at: datetime)
```

FYI it's our friend Active Record that's allowing us to simply type in Artist or Song to tap into the database.

For the many rake commands above, it's a hassle to always type them in especially if you have to change tables, seed new data, etc., so here's a shortcut that allows you to type in one command. If you go into your `Rakefile` you can copy and paste this at the bottom:

```ruby
namespace :db do

  desc "reload and prep for scraping"
  task :reload => :environment do
    system("rake db:drop")
    system("rake db:create")
    system("rake db:migrate")
    system("rake db:migrate RAILS_ENV=development")
    puts 'Database Ready'
  end

end
```

Namespace lets us say "type `db` first" then the task of `:reload` is what it acts on. Put together in your terminal you can simply type in `rake db:reload` and it will first drop your database then do all the commands above for you!

# RESTful routes

In our rails console we can manage our database by viewing rows, creating new rows, editing existing rows, or deleting rows. These are part of what's known as the 7 RESTful routes which from the standpoint of our artists table are:

route | explanation
---|---
index | display a list of all artists
new | HTML form for creating a new artist
create | create a new artist
show | display a specific artist
edit | return an HTML form for editing a artist
update | update a specific artist
destroy | delete a specific artist

You can visit [this site](http://restfulrouting.com/#introduction) for an intro to RESTful routes, and I also made a [cheat sheet](https://docs.google.com/spreadsheets/d/1YWPb6BsZjMorn4XGMA5o7qGKvgYNLJTgtrbhoceZvkw/edit?usp=sharing) with controller actions, usage, SQL, and more. In fact let's add the SQL to the table above:

route | explanation | SQL
---|---|---
index | display a list of all artists | SELECT * FROM song
new | HTML form for creating a new artist | N/A
create | create a new artist | INSERT INTO song (column) VALUES (?)
show | display a specific artist | SELECT * FROM song WHERE id = ?
edit | return an HTML form for editing a artist | SELECT * FROM song WHERE id = ?
update | update a specific artist | UPDATE song SET column = ? WHERE id = ?
destroy | delete a specific artist | DELETE FROM song WHERE id = ?

So how do we actually use these RESTful routes? Once again we have our favorite recurring theme of this post: using Active Record to help us out. Open up your Rails console again, and just like before when we typed in Artist or Song to see the tables, we can type in `Artist.all` or `Song.all` to get a list of all songs (they're empty for now but they're there)

```ruby
# Artist.all
Artist Load (2.6ms)  SELECT  "artists".* FROM "artists" LIMIT $1  [["LIMIT", 11]]
=> #<ActiveRecord::Relation []>

# Song.all
Song Load (2.7ms)  SELECT  "songs".* FROM "songs" LIMIT $1  [["LIMIT", 11]]
=> #<ActiveRecord::Relation []>
```

Notice something on the return? It's giving us the SQL that `Artist.all` points to, specifically `SELECT * FROM artists`. With that knowledge, let's add Active Record to the table above:

route | AR | SQL
---|---|---
index | Artist.all | SELECT * FROM song
new | Artist.new(params) | N/A
create | @artist.save | INSERT INTO song (column) VALUES (?)
show | Artist.find(id) | SELECT * FROM song WHERE id = ?
edit | Artist.find(id) | SELECT * FROM song WHERE id = ?
update | @artist.save / update | UPDATE song SET column = ? WHERE id = ?
destroy | @artist.destroy / delete | DELETE FROM song WHERE id = ?

`@artist` is an object that has an artist's data. With your console still open let's tackle the **new** RESTful route and make a new entry:

```ruby
@artist = Artist.new
@artist #=> <Artist id: nil, name: nil, origin: nil, genre: nil, created_at: nil, updated_at: nil>
```

Note we did not put the artist into the database yet, just created an object with an Artist's attributes hence why no SQL was fired off. Let's add some info to the attributes:

```ruby
@artist.name = "Queen"
@artist.origin = "London, England"
@artist.genre = "Rock"
@artist #=> <Artist id: nil, name: "Queen", origin: "London, England", genre: "Rock", created_at: nil, updated_at: nil>
```

We don't touch the id, created_at, or updated_at since they'll automatically be populated when we save the artist to our database, which is what we'll do now with our **create** RESTful route:

```sql
@artist.save
   (2.1ms)  BEGIN
  SQL (25.9ms)  INSERT INTO "artists" ("name", "origin", "genre", "created_at", "updated_at")
  VALUES ($1, $2, $3, $4, $5) RETURNING "id"  [["name", "Queen"], ["origin", "London, England"],
  ["genre", "Rock"], ["created_at", "2017-10-25 22:04:29.052588"], ["updated_at", "2017-10-25 22:04:29.052588"]]
   (4.4ms)  COMMIT
=> true
```

We can do the attribute population all at once:

```ruby
@artist = Artist.new(name: "Rush", origin: "Ontario, Canada", genre: "Rock")
#=> <Artist id: nil, name: "Rush", origin: "Ontario, Canada", genre: "Rock", created_at: nil, updated_at: nil>
@artist.save
(1.9ms)  BEGIN
  SQL (15.8ms)  INSERT INTO "artists" ("name", "origin", "genre", "created_at", "updated_at")
  VALUES ($1, $2, $3, $4, $5) RETURNING "id"  [["name", "Rush"], ["origin", "Ontario, Canada"],
  ["genre", "Rock"], ["created_at", "2017-10-25 22:06:01.996880"], ["updated_at", "2017-10-25 22:06:01.996880"]]
(2.3ms)  COMMIT
=> true
```

Since we're doing it directly we can skip the **new** process altogether and go right to the **create**:

```ruby
Artist.create(name: "Metallica", origin: "Los Angeles, California", genre: "Metal")
(1.6ms)  BEGIN
  SQL (12.5ms)  INSERT INTO "artists" ("name", "origin", "genre", "created_at", "updated_at") VALUES ($1, $2, $3, $4, $5) RETURNING "id"  [["name", "Metallica"], ["origin", "Los Angeles, California"], ["genre", "Metal"], ["created_at", "2017-10-25 22:11:51.499988"], ["updated_at", "2017-10-25 22:11:51.499988"]]
(3.6ms)  COMMIT
#=> <Artist id: 3, name: "Metallica", origin: "Los Angeles, California", genre: "Metal", created_at: "2017-10-25 22:07:51", updated_at: "2017-10-25 22:07:51">
```

Now that we some artists, let's create some songs that belong to those artists. Our current artists are:

ID 1 - Queen
ID 2 - Rush
ID 3 - Metallica

```ruby
Song.create(name: "Don't Stop Me Now", artist_id: 1, album: "Jazz", length: "3:29")
Song.create(name: "Somebody To Love", artist_id: 1, album: "A Day at the Races", length: "4:57")
Song.create(name: "Princes of the Universe", artist_id: 1, album: "A Kind of Magic", length: "3:32")

Song.create(name: "Subdivisions", artist_id: 2, album: "Signals", length: "5:34")
Song.create(name: "Red Barchetta", artist_id: 2, album: "Moving Pictures", length: "6:06")
Song.create(name: "Far Cry", artist_id: 2, album: "Snakes & Arrows", length: "5:21")

Song.create(name: "For Whom the Bell Tolls", artist_id: 3, album: "Ride the Lightning", length: "5:09")
Song.create(name: "Battery", artist_id: 3, album: "Master of Puppets", length: "5:12")
Song.create(name: "One", artist_id: 3, album: "...And Justice for All", length: "7:24")
```

Now we have 9 songs at our disposal and can type in our **index** RESTful route of `Artist.all` or `Song.all` to see them, and because of our models and their relationships we can see an artist's songs or a song's artist:

```ruby
Artist.first
# Artist Load (0.6ms)  SELECT  "artists".* FROM "artists" ORDER BY "artists"."id" ASC LIMIT $1  [["LIMIT", 1]]
# or
Artist.find(1)
Artist.find_by(id: 1)
# Artist Load (0.6ms)  SELECT  "artists".* FROM "artists" WHERE "artists"."id" = $1 LIMIT $2  [["id", 1], ["LIMIT", 1]]

# all return
#=> <Artist id: 1, name: "Queen", origin: "London, England", genre: "Rock" ... >

Artist.find_by(id: 1).songs
# Artist Load (0.6ms)  SELECT  "artists".* FROM "artists" WHERE "artists"."id" = $1 LIMIT $2  [["id", 1], ["LIMIT", 1]]
# Song Load (0.6ms)  SELECT  "songs".* FROM "songs" WHERE "songs"."artist_id" = $1 LIMIT $2  [["artist_id", 1], ["LIMIT", 11]]

#=> <ActiveRecord::Associations::CollectionProxy [
  #<Song id: 1, name: "Don't Stop Me Now", artist_id: 1, album: "Jazz", length: "3:29", ... >,
  #<Song id: 2, name: "Somebody To Love", artist_id: 1, album: "A Day at the Races", length: "4:57", ... >,
  #<Song id: 3, name: "Princes of the Universe", artist_id: 1, album: "A Kind of Magic", length: "3:32", ... ]>

Song.find_by(id: 1)
# Song Load (0.7ms)  SELECT  "songs".* FROM "songs" WHERE "songs"."id" = $1 LIMIT $2  [["id", 1], ["LIMIT", 1]]

#=> #<Song id: 1, name: "Don't Stop Me Now", artist_id: 1, album: "Jazz", length: "3:29", ... >

Song.find_by(id: 1).artist
# Song Load (0.8ms)  SELECT  "songs".* FROM "songs" WHERE "songs"."id" = $1 LIMIT $2  [["id", 1], ["LIMIT", 1]]
# Artist Load (0.4ms)  SELECT  "artists".* FROM "artists" WHERE "artists"."id" = $1 LIMIT $2  [["id", 1], ["LIMIT", 1]]

#=> #<Artist id: 1, name: "Queen", origin: "London, England", genre: "Rock", ... >
```

Everything works as normal!

# Seeding this data

This is great that we can use the Rails console for all this work but if we ever reset the database we'd have to do it all over again. This is where seeding our data comes into play. If you open up `db/migrate/seeds.rb` you can put EVERYTHING we just did in there:

```ruby
Artist.create(name: "Queen", origin: "London, England", genre: "Rock")
Artist.create(name: "Rush", origin: "Ontario, Canada", genre: "Rock")
Artist.create(name: "Metallica", origin: "Los Angeles, California", genre: "Metal")

Song.create(name: "Don't Stop Me Now", artist_id: 1, album: "Jazz", length: "3:29")
Song.create(name: "Somebody To Love", artist_id: 1, album: "A Day at the Races", length: "4:57")
Song.create(name: "Princes of the Universe", artist_id: 1, album: "A Kind of Magic", length: "3:32")

Song.create(name: "Subdivisions", artist_id: 2, album: "Signals", length: "5:34")
Song.create(name: "Red Barchetta", artist_id: 2, album: "Moving Pictures", length: "6:06")
Song.create(name: "Far Cry", artist_id: 2, album: "Snakes & Arrows", length: "5:21")

Song.create(name: "For Whom the Bell Tolls", artist_id: 3, album: "Ride the Lightning", length: "5:09")
Song.create(name: "Battery", artist_id: 3, album: "Master of Puppets", length: "5:12")
Song.create(name: "One", artist_id: 3, album: "...And Justice for All", length: "7:24")
```

Reload the database by typing in that Rakefile command we added: `rake db:reload`. Open up the rails console and you'll see nothing's there if you type in `Artist.all` or `Song.all`. Exit back out to the main terminal and type in `rake db:seed`. After a short period of time the next line will appear as if nothing happened, buf if you go back into your rails console and look for the artists and songs everything's there!

# Controller setup and the Rails server

So it's great we can manipulate these RESTful routes in the console or seed the data but right now we can't to do this via our app. Onto the `invoke  controller` and `create    app/controllers/artists_controller.rb` lines.

As I mentioned before the controller is the logic to our API. Let's look again at the Active Record commands:

route | explanation | AR
---|---|---
index | display a list of all artists | Artist.all
new | HTML form for creating a new artist | Artist.new(params)
create | create a new artist | @artist.save
show | display a specific artist | Artist.find(id)
edit | return an HTML form for editing a artist | Artist.find(id)
update | update a specific artist | @artist.save / update
destroy | delete a specific artist |  @artist.destroy / delete

In this specific app we're only going to using the **index** and **show** routes. Open up `app/controllers/artists_controller.rb` and you'll see:

```ruby
class ArtistsController < ApplicationController
end
```

It's here that we can add in commands similar to what we used in the rails console. Referencing the table above we know that **index** is `Artist.all` and **show** is `Artist.find(id)` or `Artist.find_by(id: id)`. Let's tackle our index method first. The first step is defining our index method:

```ruby
class ArtistsController < ApplicationController

  def index
  end

end
```

We'll then insert our command inside of it:

```ruby
class ArtistsController < ApplicationController

  def index
    Artist.all
  end

end
```

Save your work and let's start up our rails server by typing into your terminal `rails s`. Once your server is running you'll see a line `* Listening on tcp://0.0.0.0:3000` which means you can go to http://localhost:3000/ and see that your server is up and running with the default "Yay! You’re on Rails!" welcome screen.

We can access our artist model by visiting http://localhost:3000/artists - but nothing happens when you do. Go back to your mac terminal and you'll see the following message:

```bash
Started GET "/artists" for 127.0.0.1 at 2017-10-25 22:19:54 -0400
Processing by ArtistsController#index as HTML
Completed 204 No Content in 2ms (ActiveRecord: 0.0ms)
```

This is because we returned `Artist.all` but we're not rendering any content. We can render out our result as HTML by doing:

```ruby
class ArtistsController < ApplicationController

  def index
    render html: Artist.all
  end

end
```

And get back the enumerator `#<Artist::ActiveRecord_Relation:0x007fc9751ad100>` but that isn't helpful for looking at an API. Instead we can render as JSON:

```ruby
class ArtistsController < ApplicationController

  def index
    render json: Artist.all
  end

end
```

And voila we can see loads of data!

```ruby
[
  {
    id: 1,
    name: "Queen",
    origin: "London, England",
    genre: "Rock",
    created_at: "2017-10-26T02:39:48.053Z",
    updated_at: "2017-10-26T02:39:48.053Z"
  },
  {
    id: 2,
    name: "Rush",
    origin: "Ontario, Canada",
    genre: "Rock",
    created_at: "2017-10-26T02:39:48.064Z",
    updated_at: "2017-10-26T02:39:48.064Z"
  },
  {
    id: 3,
    name: "Metallica",
    origin: "Los Angeles, California",
    genre: "Metal",
    created_at: "2017-10-26T02:39:48.069Z",
    updated_at: "2017-10-26T02:39:48.069Z"
  }
]
```

And in our terminal we now see that the correct SQL fired off:

```bash
Started GET "/artists" for 127.0.0.1 at 2017-10-25 22:21:26 -0400
Processing by ArtistsController#index as HTML
  Artist Load (0.6ms)  SELECT "artists".* FROM "artists"
Completed 200 OK in 7ms (Views: 5.9ms | ActiveRecord: 0.6ms)
```

Now let's try adding the **show** route:

```ruby
class ArtistsController < ApplicationController

  def index
    render json: Artist.all
  end

  def show
    render json: Artist.find(id)
  end

end
```

And we can show a specific artist with the id of 1 by going to http://localhost:3000/artists/1 - but we get the following error:

`NameError in ArtistsController#show
undefined local variable or method 'id' for #<ArtistsController:0x007fc974cceb70>`

Our **show** method doesn't know what an 'id' is. Let's quickly debug this and learn something very important in the process. Put `byebug` at the beginning of our show method:

```ruby
class ArtistsController < ApplicationController

  def index
    render json: Artist.all
  end

  def show
    byebug
    render json: Artist.find(id)
  end

end
```

Reload http://localhost:3000/artists/1 and go to your terminal to see that your program stops at the byebug and allows you to type commands in as if you were inside your application. Typing in `id` get you the NameError Exception, so where is our id located? Introducing **parameters**, how Active Record handles table attributes. If you type in `params` you'll get back:

`<ActionController::Parameters {"controller"=>"artists", "action"=>"show", "id"=>"1"} permitted: false>`

You'll notice this is a hash that has the controller, action, and id, so we can type in `params[:id]` to access the id and get back "1". All we need to do is substitute `id` for `params[:id]` in our method and it should work:

```ruby
class ArtistsController < ApplicationController

  def index
    render json: Artist.all
  end

  def show
    render json: Artist.find(params[:id])
  end

end
```

In your terminal type in `exit` to exit the byebug instance, then reload http://localhost:3000/artists/1 and success!

```ruby
{
  id: 1,
  name: "Queen",
  origin: "London, England",
  genre: "Rock",
  created_at: "2017-10-26T02:39:48.053Z",
  updated_at: "2017-10-26T02:39:48.053Z"
}
```

Try doing the same thing for the songs controller on your own. Once you're done your two controllers should look like this:

```ruby
class ArtistsController < ApplicationController

  def index
    render json: Artist.all
  end

  def show
    render json: Artist.find(params[:id])
  end

end


class SongsController < ApplicationController

  def index
    render json: Song.all
  end

  def show
    render json: Song.find(params[:id])
  end

end
```

# Routes

There's one very important thing that Rails did for you automatically when you generated your resource and that's the resources themselves. If you go into `config/routes.rb` you'll notice the following:

```ruby
Rails.application.routes.draw do
  resources :songs
  resources :artists
end
```

This is the final piece of the generated invokes and file creation/editing: `invoke  resource_route` and `route    resources :songs`.



# CORS

`Gemfile`
`gem 'rack-cors'`

`/config/application.rb`
`/config/initializers/`



Better practices:

`/api/V1`

Code on.

Mike Merin
