---
layout: post
title:  "Intro to SQL"
subtitle: "SQL 101"
date:   2017-12-30 22:22:22 -0400
categories: SQL, tutorial
---
If you want to store information that's clean and structured then you need to use a database. If you want to access that information then you need to use SQL. There are plenty of SQL cheat sheets out there (my favorite reference is [this one](https://zeroturnaround.com/wp-content/uploads/2016/06/RebelLabs-SQL-cheat-sheet.png)), however I find when you're learning SQL it's better to see it in action and code along.

As you go through this post, use my setup in this [coding playground](http://tpcg.io/zkrK2w) to code along!

# Tables / Schema
---

Fortunately in the coding playground our database was already created for us. However if you ever needed to create a database on your own it's as easy as typing in the following command:

```sql
CREATE DATABASE database_name;
```

Let's actually store some data. If you've seen my [educational](https://mikemerin.github.io/education/) posts, including the [Python through Ruby](https://mikemerin.github.io/Python-through-Ruby/#19-sorting-a-collection) one you'll know I like to reference some of either my pets or other family ones. Let's continue that trend here!

In order to store our data we need to make a `table` that has different `columns`, which put together is known as a `schema`.

I want to make a table with the title of Animals.


```sql
CREATE TABLE animals (
  name TEXT,
  breed TEXT
);
```

```sql
-- General

--- See current tables (M)
.tables
--- See current tables with their schemas
.schema

-- Databases

--- Create a database
CREATE DATABASE database_name;
--- Delete a database
DROP DATABASE database_name;

-- Tables

-- Create a table along with its columns
CREATE TABLE table_name (
  column_name DATA_TYPE -- (TEXT, INTEGER, etc)
  column_name2 DATA_TYPE2
  etc
)
-- Delete a table
DROP TABLE table_name;
-- Add columns to a table




```
---

Code on.

Mike Merin
