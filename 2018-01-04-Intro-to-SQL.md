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

Note: certain programs may prevent you from deleting data and therefore some of the DROP / TRUNCATE commands here may not may not work, and in some cases it may prevent you from adding multiple columns at once to a table. I will list similar alternate methods in those cases if they're available.

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

--- Create a table along with its columns
CREATE TABLE table_name (
  column_name DATA_TYPE -- (TEXT, INTEGER, etc)
  column_name2 DATA_TYPE2
  etc
)
--- Delete a table
DROP TABLE table_name;

--- Rename a table
ALTER TABLE table_name
RENAME TO table_name2;

--- Remove all data in a table
TRUNCATE TABLE table_name;

-- Columns

--- Add a column to a table
ALTER TABLE table_name
ADD column_name DATA_TYPE;

--- Remove a column from a table (note, doesn't work with certain programs)
ALTER TABLE table_name
DROP column_name;

--- If your program can't perform column drops,
--- here's an alternate solution of copying to another table

CREATE TABLE table_name2
INSERT INTO table_name2 (column_name, column_name2, ...)
SELECT (column_name, column_name2, ...)
FROM table_name;

--- Rename a column
ALTER TABLE table_name
RENAME column_name TO column_name2;

-- Modifying data

--- Add rows of data into your table
INSERT INTO table_name (column_name, column_name2, ...)
VALUES (value, value2, ...);


```
---

Code on.

Mike Merin

<!--


CREATE TABLE animals (
  name TEXT,
  age INTEGER
  animal_type TEXT
);

.tables
.schema

DROP TABLE animals;

CREATE TABLE animals (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    animal_type TEXT
);

.schema

ALTER TABLE animals
ADD COLUMN breed TEXT;

.schema





INSERT INTO animals
(name, age, animal_type, breed)
VALUES ("Lira", 15, "Cat", "Chartreux");

INSERT INTO animals
(name, age, animal_type, breed)
VALUES ("Lily", 9, "Dog", "Pit Mix");

SELECT * FROM testing; -->


-- Welcome to the SQL code-along!
-- I have included the first command from my post below.
-- Use the "Execute" button above to run the commands.

CREATE TABLE animals;


.tables
.schema
