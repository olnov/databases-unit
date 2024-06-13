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