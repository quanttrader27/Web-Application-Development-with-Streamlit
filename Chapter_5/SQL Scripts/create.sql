create table paygrades (
	id SERIAL,
	base_salary varchar(255) not null,
	reimbursement varchar(255),
	bonuses varchar(255),
	primary key (id)
);

create table Persons (
	id SERIAL,
	name varchar(255) not null,
	date_of_birth varchar(255),
	paygrade_id int not null,
	primary key (id),
    FOREIGN KEY (paygrade_id) REFERENCES Paygrades(id)
);