CREATE TABLE Admins(
    id SERIAL,
    username VARCHAR(255) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    PRIMARY KEY(id)
);