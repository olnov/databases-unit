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