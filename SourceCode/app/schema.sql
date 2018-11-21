DROP TABLE if EXISTS users ;

CREATE TABLE users
(
    ID int IDENTITY(1,1) PRIMARY KEY,
    LoginName NVARCHAR(40) NOT NULL,
    Password BINARY(64) NOT NULL,
    FirstName NVARCHAR(40) NULL,
    LastName NVARCHAR(40) NULL,
    Type NVARCHAR(40) NULL
);

INSERT INTO users VALUES (NULL,'Admin','Admin','Enrique','Belenguer','Administrator');
