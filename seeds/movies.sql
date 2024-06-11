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
    "genre_id" int not null
);

alter table "movies" add foreign key ("genre_id") references "genres" ("id");

INSERT INTO genres (name) VALUES ('Action');
INSERT INTO genres (name) VALUES ('Comedy');

INSERT INTO movies (title, release_year, genre_id) VALUES ('The Acolyte', 2024, 1);
INSERT INTO movies (title, release_year, genre_id) VALUES ('The Fall Guy', 2024, 2);

