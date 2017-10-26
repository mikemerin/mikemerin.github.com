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
`rails g resource Song name artist_id album length`

Please note that all of these bits of info will default to a string, but if we wanted to we can make them into other data types like an integer for example by typing in `release_year:integer`, or a boolean `active:boolean`.

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

Now you can load up your Rails console by typing in `rails c` and see your database and models! Type in `Artist.all` or `Song.all` to see your tables (they're empty for now but they're there)

```ruby
# Artist.all
Artist Load (2.6ms)  SELECT  "artists".* FROM "artists" LIMIT $1  [["LIMIT", 11]]
=> #<ActiveRecord::Relation []>


# Song.all
Song Load (2.7ms)  SELECT  "songs".* FROM "songs" LIMIT $1  [["LIMIT", 11]]
=> #<ActiveRecord::Relation []>
```

It's a hassle to always type in these commands especially if you have to change tables, seed new data, etc., so here's a shortcut that allows you to type in one command. If you go into your `Rakefile` you can copy and paste this at the bottom:

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

# Controller setup, and RESTful routes

Onto the `invoke  controller` and `create    app/controllers/artists_controller.rb` lines. Even though in our rails console we can manage our database by viewing any row(s), creating new rows, editing existing rows, or deleting rows, we won't be able to do this via our app or an external app connecting to it. This is where the 7 RESTful rounds come in, which allow you to see all entries (the index), make new entries and create them in the database, show specific entries, edit and update those entries, or delete them. The 7 routes are:

route | explanation
---|---
index | display a list of all artists
new | HTML form for creating a new artist
create | create a new artist
show | display a specific artist
edit | return an HTML form for editing a artist
update | update a specific artist
destroy | delete a specific artist

You can visit [this site](http://restfulrouting.com/#introduction) for an intro to RESTful routes, and I also made a [cheat sheet](https://docs.google.com/spreadsheets/d/1YWPb6BsZjMorn4XGMA5o7qGKvgYNLJTgtrbhoceZvkw/edit?usp=sharing) with controller actions, usage, SQL, and more.

So how do we use these RESTful routes? As I mentioned before the controller is the logic to our API so we'll be running some specific and easy database commands


 In it we'll be tapping into these routes.


```ruby
class ArtistsController < ApplicationController

  def index
    @artists = Artist.all
    render json: @artists
  end

  def show
    @artist = Artist.find_by(id: params[:id])
    render json: @artist
  end

  private

  def artist_params
    params.permit(:name, :origin, :genre)
  end

end

class SongsController < ApplicationController

  def index
    @songs = Song.all
    render json: @songs
  end

  def show
    @song = Song.find_by(id: params[:id])
    render json: @song
  end

  private

  def song_params
    params.permit(:name, :artist_id, :album, :length)
  end

end
```







# Routes


     invoke  resource_route
      route    resources :songs



# CORS

`Gemfile`
`gem 'rack-cors'`

`/config/application.rb`
`/config/initializers/`



Better practices:

`/api/V1`

Code on.

Mike Merin
