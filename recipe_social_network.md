# Unit three, section two. Social network exercise.

## 1. Extract nouns from the user stories or specification

```
As a social network user,
So I can have my information registered,
I'd like to have a user account with my email address.

As a social network user,
So I can have my information registered,
I'd like to have a user account with my username.

As a social network user,
So I can write on my timeline,
I'd like to create posts associated with my user account.

As a social network user,
So I can write on my timeline,
I'd like each of my posts to have a title and a content.

As a social network user,
So I can know who reads my posts,
I'd like each of my posts to have a number of views.

```

```
Nouns:

posts, users, title, content, email address, username, number of views
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties                      |
| --------------------- | --------------------------------|
| post                  | title, content, number of views |
| users                 | username, email                 |

1. Name of the first table (always plural): `posts` 

    Column names: `title`, `content`,`views`

2. Name of the second table (always plural): `users` 

    Column names: `username`,`email`

## 3. Decide the column types

```
Table: posts
id: SERIAL PRIMARY KEY
title: varchar(200)
content: text
views: int
user_id: int FK refferences users.id

Table: users
id: SERIAL PRIMARY KEY
username: varchar(50)
email: varchar(100)
```

## 4. Decide on The Tables Relationship

To decide on which one, answer these two questions:

1. Can one post have many users ? No
2. Can one user have many posts? Yes

Replace the relevant bits in this example with your own:

```
1. Can one post have many users ? No
2. Can one user have many posts? Yes

-> Therefore,
-> A user HAS MANY posts
-> A post BELONGS TO a user

-> Therefore, the foreign key is on the posts table.
```


## 5. Write the SQL

```sql

drop table if exists posts;
drop table if exists users;

CREATE TABLE "users" (
    "id" SERIAL PRIMARY KEY,
    "username" VARCHAR(50) not null,
    "email" VARCHAR(100) not null
);

CREATE TABLE "posts" (
    "id" SERIAL PRIMARY KEY,
    "title" VARCHAR(200) not null,
    "content" TEXT not null,
    "views" int,
    "user_id" int not null
);



alter table "posts" add foreign key ("user_id") references "users" ("id");

INSERT INTO users (username, email) VALUES ('joshglasson','glasson@gmail.com');
INSERT INTO users (username, email) VALUES ('johnlennon','lennon@gmail.com');

INSERT INTO posts (title, content, views, user_id) VALUES ('Day 1 at Makers Academy','Day 1 was an introduction to Makers Academy and the 6 other people I would be completing the course with',55,1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Day 2 at Makers Academy','Day 2 was the day we actually started coding!',38, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Let it be','When I find myself in times of trouble...',6000000, 2);


```

## 6. Create the tables

```bash
psql -h 127.0.0.1 database_name < blog.sql
```