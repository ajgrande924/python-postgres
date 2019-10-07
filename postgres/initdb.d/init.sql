create database lmd;
\c lmd

CREATE TABLE midi_instrument(
	code VARCHAR (5) UNIQUE NOT NULL,
	name VARCHAR (80) NOT NULL,
	family VARCHAR (55) NOT NULL
);

CREATE TABLE filename_instrument(
  filename VARCHAR (80) NOT NULL,
  instrument VARCHAR (80) NOT NULL
);

CREATE TABLE debugger(
  col_str_one VARCHAR (50) UNIQUE NOT NULL,
  col_str_two VARCHAR (50) NOT NULL
);