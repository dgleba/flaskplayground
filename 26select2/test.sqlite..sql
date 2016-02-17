BEGIN TRANSACTION;
CREATE TABLE users (id INTEGER NOT NULL, name VARCHAR (50), email VARCHAR (120), comment VARCHAR (245), c3 VARCHAR (99), PRIMARY KEY (id), UNIQUE (name), UNIQUE (email));
INSERT INTO `users` VALUES ('1','admin','admin@localhost','244','99');
INSERT INTO `users` VALUES ('2','dave','dgleba@gmail.com','244','99');
CREATE TABLE tyres (
	car_id INTEGER NOT NULL, 
	tyre_id INTEGER NOT NULL, 
	"desc" VARCHAR(50), 
	PRIMARY KEY (car_id, tyre_id), 
	FOREIGN KEY(car_id) REFERENCES cars (id)
);
CREATE TABLE cars (
	id INTEGER NOT NULL, 
	"desc" VARCHAR(50), 
	PRIMARY KEY (id)
);
CREATE TABLE "Persons" (
	`P_Id`	integer NOT NULL,
	`Name_fnln`	varchar(255) NOT NULL,
	`donotuse_FirstName`	varchar(255),
	`Address`	varchar(255),
	`City`	varchar(255),
	PRIMARY KEY(Name_fnln)
);
INSERT INTO `Persons` VALUES ('1','Andy Smith','a',NULL,NULL);
INSERT INTO `Persons` VALUES ('2','Ted Ford','t',NULL,NULL);
INSERT INTO `Persons` VALUES ('3','Cy Kiby','c',NULL,NULL);
CREATE TABLE "Orders" (
	`O_Id`	integer NOT NULL UNIQUE,
	`OrderNo`	int NOT NULL UNIQUE,
	`P_Id`	int,
	`Name_fnln`	TEXT NOT NULL,
	PRIMARY KEY(O_Id)
);
INSERT INTO `Orders` VALUES ('1','22','1','1');
INSERT INTO `Orders` VALUES ('2','23','2','2');
INSERT INTO `Orders` VALUES ('3','24','1','3');
;
;
;
;
;
;
CREATE VIEW vw_user1 AS select id, name, comment from users;
COMMIT;
