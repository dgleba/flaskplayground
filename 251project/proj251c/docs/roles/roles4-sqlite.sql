BEGIN TRANSACTION;
CREATE TABLE users (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	first_name VARCHAR(255), 
	last_name VARCHAR(255), 
	email VARCHAR(255), 
	username VARCHAR(255), 
	password VARCHAR(255), 
	active BOOLEAN, 
	confirmed_at DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	UNIQUE (username), 
	CHECK (active IN (0, 1))
);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (1,'Admin',NULL,'admin','admin','admin',1,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (2,'read','Brown',NULL,'read','a',1,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (3,'create','Smith',NULL,'create','a',1,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (4,'user','Patel',NULL,'user','a',1,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (5,'suser','Jones',NULL,'suser','a',1,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (6,'delete','Williams',NULL,'delete','a',1,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (7,'Mia','Thomas',NULL,'mia','a',1,NULL);

CREATE TABLE roles_users (
	user_id INTEGER, 
	role_id INTEGER, 
	FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);
INSERT INTO `roles_users` (user_id,role_id) VALUES (1,1);
INSERT INTO `roles_users` (user_id,role_id) VALUES (1,2);
INSERT INTO `roles_users` (user_id,role_id) VALUES (2,7);
INSERT INTO `roles_users` (user_id,role_id) VALUES (3,7);
INSERT INTO `roles_users` (user_id,role_id) VALUES (4,7);
INSERT INTO `roles_users` (user_id,role_id) VALUES (5,7);
INSERT INTO `roles_users` (user_id,role_id) VALUES (6,7);
INSERT INTO `roles_users` (user_id,role_id) VALUES (7,7);
CREATE TABLE role (
	id INTEGER NOT NULL AUTO_INCREMENT, 
	name VARCHAR(80), 
	description VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
INSERT INTO `role` (id,name,description) VALUES (1,'user',NULL);
INSERT INTO `role` (id,name,description) VALUES (2,'adminrole',NULL);
INSERT INTO `role` (id,name,description) VALUES (3,'create',NULL);
INSERT INTO `role` (id,name,description) VALUES (4,'supervisor',NULL);
INSERT INTO `role` (id,name,description) VALUES (5,'delete',NULL);
INSERT INTO `role` (id,name,description) VALUES (6,'export',NULL);
INSERT INTO `role` (id,name,description) VALUES (7,'read',NULL);
COMMIT;
