CREATE TABLE books(
ID integer primary key autoincrement not null unique,
name varchar(255) not null,
author_id integer NULL,
FOREIGN KEY (author_id) REFERENCES authors(ID)
);

CREATE TABLE authors(
ID integer primary key autoincrement not null unique,
name varchar(255) not null
);

CREATE TABLE customers(
ID integer primary key autoincrement not null unique,
name varchar(255) not null,
email varchar(255) not null unique
);

CREATE TABLE rents(
ID integer primary key autoincrement not null unique,
book_id integer not null,
customer_id integer not null,
state varchar(50) not null,
FOREIGN KEY (book_id) REFERENCES books(ID),
FOREIGN KEY (customer_id) REFERENCES customers(ID)
);
