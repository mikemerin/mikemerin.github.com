---
layout: post
title:  "Creating a Rails API and fixing CORS issues"
date:   2017-04-17 13:58:14 -0400
categories: ruby, rails, API, CORS, cross-origin
---

I recently tried to recreate an API for my random question generator, this time letting the front end handle the question creation. I ran into the infamous CORS issue `No 'Access-Control-Allow-Origin' header is present on the requested resource.` I ran into this issue before and it took a litle while to find the answer to it again, so I figure I'd go through the simple steps of how to create a rails API from scratch and fix the issue as I go.

If you're just interested in how to fix a CORS issue you can skip ahead to [here](https://mikemerin.github.io/Rails-API-cors#CORS).

# Tools

Ruby: There are a few ways to get Ruby installed on your computer but many roads lead [here](https://www.ruby-lang.org/en/documentation/installation/)

Rails: Connecting Ruby to the online world. You can find the guide to installing Rails [here](http://installrails.com/)

Database: Since you're creating an API you'll need to have a database program on your computer. You can use the clean and useful [DB Browser for SQLite](http://sqlitebrowser.org/), or my preferred [postgresql](https://www.postgresql.org/) which is much faster and advanced.


# Creating the application

Rails makes it incredibly easy to create a basic application from scratch. No needing to manually configure the little things like you need to with Sinatra, just type in the terminal commands and you're good to go. We're going to create a new API called `test_api`. The easiest way to do this is type in:

`rails new test_api --api`

or if like me you like Postgresql better you can instead type in:

`rails new test_api --api --database=postgresql -T`

Once the flurry of text finishes, you'll notice a new folder called `test_api`. If you `cd test_api` to go into the folder you'll see it contains files like a Gemfile, Rakefile, config, readme, etc. I won't go into detail about what each of them do right now, but technically you just made an API! Grats, now to get it working correctly.

# MVC

Rails uses the MVC framework which stands for "model, view, controller":

* Models: the data of your app, objects where you can store and retrieve information
* Views: as the name says, this is what a user will see and interact with
* Controllers: the logic that dictates how your app will behave

Since this is an API we won't be working with views. After all we're just after data and don't need to build a website for a user to interact with. That can either be later down the line, or more preferrably handled in a separate app on the front end.

### Models

We're going to make a little music API that has artists and songs. Rails once again makes this part easy for us. We can type in the terminal the following to create our two models:

`rails generate resource Artist _________`

We can generate many things this way: a migration, a model, a controller, etc., but we use `resource` in this case since it will create the model, controller, and the routes we need to connect to. We'll want our Artist to contain certain information like the artist's name, origin, its genre, and years it's been active. We'll also want the songs to have a name, artist_id, release date, album name, and length. Here's how we'll generate our models:


`rails generate resource Artist name origin genre start_year end_year`
`rails generate resource Song name artist_id release_date album_name length`

Please note that all of these bits of info will default to a string, but if we wanted to we can make them into other data types like an integer for example by typing in `date:integer`, or a boolean `active:boolean`.

Once you type these in you'll get another bit of text, including invoking the active_record controller and routes along with creating the necessary files. You now have your models!

### 


# CORS


Code on.

Mike Merin
