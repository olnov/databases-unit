## 1. Requirements

```
As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' titles.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' genres.

As a person who loves movies,
So I can list all my favourite movies
I want to see a list of movies' release years.

```

```
Nouns:

title, genre, release year, movie
```

## 2. Infer the Table Name and Columns


| Record                | Properties                    |
| --------------------- | ------------------------------|
| movie                 | title, release year, genre_id |


| Record                | Properties    |
| --------------------- | --------------|
| genre                 | name          |


Name of the table (always plural): `movies`

Column names: `id`,`title`, `release_year`,`genre_id`

Name of the table (plural): `genres`

Column names: `id`,`name`

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# Movies:

id: SERIAL PRIMARY KEY
title: text
release_year: int
genre_id: int FK genre.id

# Genres
id: SERIAL PRIMARY KEY
name: varchar (200)
```

## 4. Write the SQL

```sql
-- file: movies.sql

/* Dropping tables*/
drop table if exists movies;
drop table if exists genres;

CREATE TABLE "genres" (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(200) not null
);

CREATE TABLE "movies" (
  "id" SERIAL PRIMARY KEY,
  "title" text not null,
  "release_year" int not null,
  "genre_id" int not null,
);

alter table "movies" add foreign key ("genre_id") references "genres" ("id");
```

## 5. Create the table

```bash
psql -h 127.0.0.1 database_name < movies.sql
```