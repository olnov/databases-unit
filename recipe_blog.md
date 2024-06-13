# Unit three. Blog database.

## 1. Extract nouns from the user stories or specification

```
As a blogger
So I can write interesting stuff
I want to write posts having a title.

As a blogger
So I can write interesting stuff
I want to write posts having a content.

As a blogger
So I can let people comment on interesting stuff
I want to allow comments on my posts.

As a blogger
So I can let people comment on interesting stuff
I want the comments to have a content.

As a blogger
So I can let people comment on interesting stuff
I want the author to include their name in comments.

```

```
Nouns:

posts, title, content, comments, author name
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                  |
| --------------------- | --------------------------  |
| post                  | title, content, author name |
| comment               | content, author name        |

1. Name of the first table (always plural): `posts` 

    Column names: `title`, `content`,`author`

2. Name of the second table (always plural): `comments` 

    Column names: `content`,`author`

## 3. Decide the column types

```
Table: posts
id: SERIAL PRIMARY KEY
title: varchar(200)
content: text
author: varchar(50)

Table: comments
id: SERIAL PRIMARY KEY
content: text
author: varchar(50)
post_id: int FK references posts.id
```

## 4. Decide on The Tables Relationship

To decide on which one, answer these two questions:

1. Can one post have many comments ? Yes
2. Can one comment have many posts? No

Replace the relevant bits in this example with your own:

```

1. Can one post have many comments ? Yes
2. Can one comment have many posts? No

-> Therefore,
-> A post HAS MANY comments
-> A comment BELONGS TO a post

-> Therefore, the foreign key is on the comments table.
```


## 5. Write the SQL

```sql

drop table if exists comments;
drop table if exists posts;

CREATE TABLE "posts" (
    "id" SERIAL PRIMARY KEY,
    "title" VARCHAR(200) not null,
    "content" TEXT not null,
    "author" VARCHAR(50) not null
);

CREATE TABLE "comments" (
    "id" SERIAL PRIMARY KEY,
    "content" TEXT not null,
    "author" VARCHAR(50) not null,
    "post_id" int not null
);

alter table "comments" add foreign key ("post_id") references "posts" ("id");

INSERT INTO posts (title, content, author) VALUES ('Day 1 at Makers Academy','Day 1 was an introduction to Makers Academy and the 6 other people I would be completing the course with','Josh Glasson');
INSERT INTO posts (title, content, author) VALUES ('Day 2 at Makers Academy','Day 2 was the day we actually started coding!','Josh Glasson');

INSERT INTO comments (content, author, post_id) VALUES ('What a news! Good luck!', 'John Lennon', 1);
INSERT INTO comments (content, author, post_id) VALUES ('Did they order coffee pods?', 'Paul Mccartney', 1);
INSERT INTO comments (content, author, post_id) VALUES ('Already!?', 'John Doe', 2);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 database_name < blog.sql
```