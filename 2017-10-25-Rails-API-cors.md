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

Once the flurry of text finishes, you'll notice a new folder called `test_api` containing files like a Gemfile, Rakefile, config, readme, etc. Technically, you just made an API! Now to get it working correctly.

# MVC

Rails uses the MVC framework which stands for "model, view, controller":

* Models: the data of your API. These are objects


# CORS


Code on.

Mike Merin
