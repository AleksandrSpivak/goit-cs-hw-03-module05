create table if not exists users (
	id serial primary key,
	fullname varchar(100),
	email varchar(100) unique
);

create table if not exists status (
	id serial primary key,
	name varchar(50) unique
);

create table if not exists tasks (
	id serial primary key,
	title VARCHAR(100),
	description TEXT,
	status_id INTEGER,
	user_id INTEGER,
	foreign key (status_id) references status (id),
	foreign key (user_id) references users (id)
		on delete cascade
		on update cascade	
);
