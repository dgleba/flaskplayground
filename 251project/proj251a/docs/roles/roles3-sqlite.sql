BEGIN TRANSACTION;
CREATE TABLE user (
	id INTEGER NOT NULL, 
	first_name VARCHAR(255), 
	last_name VARCHAR(255), 
	email VARCHAR(255), 
	password VARCHAR(255), 
	active BOOLEAN, 
	confirmed_at DATETIME, 
	PRIMARY KEY (id), 
	UNIQUE (email), 
	CHECK (active IN (0, 1))
);
INSERT INTO `user` (id,first_name,last_name,email,password,active,confirmed_at) VALUES (1,'Admin',NULL,'admin','$pbkdf2-sha512$25000$JmTsvbcWgjBGyJmT8n4PQQ$ipjPNW9XmSefwU5iYONDEZwjpHQYx845zPZc.tUnS7AsDOK0Ulng8GGEb0W14THdLuSECfwxWgQpJ9jUi1lttA',1,NULL);
INSERT INTO `user` (id,first_name,last_name,email,password,active,confirmed_at) VALUES (2,'read','Brown','read','$pbkdf2-sha512$25000$rbXW2tsbI4Rw7r03pjTGWA$j4fDcNmAd.o47eajV/p6o06cNIKHqo3qF7NQM8/s/boqD5ZFWNJgQ0zy30JjPYsxijxkrUBgS1A052rBSqo25Q',1,NULL);
INSERT INTO `user` (id,first_name,last_name,email,password,active,confirmed_at) VALUES (3,'create','Smith','create','$pbkdf2-sha512$25000$7L03Ruh9713L.R.DUEqptQ$mngDJeI/7faLgU2nUXkss0JtM6ieMnpbh3o65vAzse.QsGSJtvzNe2UzZCnxSnosv7y0yigr5Ut5hwm7cGPDQQ',1,NULL);
INSERT INTO `user` (id,first_name,last_name,email,password,active,confirmed_at) VALUES (4,'user','Patel','user','$pbkdf2-sha512$25000$XgvhXOud09rbG4NwLoXQWg$T6FdJkOrJQpRXw.079DTXbHrzY4H5UnrTH4oWfTuBO7Dnr202GrpnksQ5DF9YdyQQDwIH1Zd17EpiAe1vFBcFA',1,NULL);
INSERT INTO `user` (id,first_name,last_name,email,password,active,confirmed_at) VALUES (5,'suser','Jones','suser','$pbkdf2-sha512$25000$9V7rHaPU2htjDKG09n5PiQ$PuY5D9bJBiItjSE06B7RTACl6jJLvRpMkuu6a0wnk2RHcjhtHpmFLesO2PORPB1zBK8I.7w/CL4eIqAlQUQ3Ig',1,NULL);
INSERT INTO `user` (id,first_name,last_name,email,password,active,confirmed_at) VALUES (6,'delete','Williams','delete','$pbkdf2-sha512$25000$M8ZYS8n5PydEaC3FGKNUCg$zunro0XKYioUKsWNG9Tmnq2x32nK.9Ntz9vrFUT7c0EM85euN2vHBm7637dzFMGp1BrScx13lWYcePPlJOuGCA',1,NULL);
INSERT INTO `user` (id,first_name,last_name,email,password,active,confirmed_at) VALUES (7,'Charlie','Johnson','charlie','$pbkdf2-sha512$25000$MOYcY2zNmdM6xxjDWAuBEA$ndun54mLDdRoh580sSrSCTZNtlcDXkQv76gonXJS1qrO6OAjxoVgD7onjHenz34KIBOtBW.sFWrH8wU56U8qsg',1,NULL);
INSERT INTO `user` (id,first_name,last_name,email,password,active,confirmed_at) VALUES (8,'Sophie','Taylor','sophie','$pbkdf2-sha512$25000$PEdIyRnDOOf83xsj5FyrlQ$U93DB14ZIMihHH3gEGHWTymm3glm5HN6ln4RkyifbDcw/VNasRJGcew6hQil0ZEDCgiHIFyKIvTsAgGRwjDYlw',1,NULL);
INSERT INTO `user` (id,first_name,last_name,email,password,active,confirmed_at) VALUES (9,'Mia','Thomas','mia','$pbkdf2-sha512$25000$55yzNuZ8T0kJoVSqVYqxNg$46JpadioINT70z/amPu3UIzWGBf1uwQa6hqbFiVFg2DnNBKk6Dd4n9QuVSJYWtoqBl9aNq/lE1Hl2bSzEmC/zA',1,NULL);
CREATE TABLE roles_users (
	user_id INTEGER, 
	role_id INTEGER, 
	FOREIGN KEY(user_id) REFERENCES user (id), 
	FOREIGN KEY(role_id) REFERENCES role (id)
);
INSERT INTO `roles_users` (user_id,role_id) VALUES (1,1);
INSERT INTO `roles_users` (user_id,role_id) VALUES (1,2);
INSERT INTO `roles_users` (user_id,role_id) VALUES (2,3);
INSERT INTO `roles_users` (user_id,role_id) VALUES (7,3);
INSERT INTO `roles_users` (user_id,role_id) VALUES (8,3);
INSERT INTO `roles_users` (user_id,role_id) VALUES (9,3);
INSERT INTO `roles_users` (user_id,role_id) VALUES (3,4);
INSERT INTO `roles_users` (user_id,role_id) VALUES (4,1);
INSERT INTO `roles_users` (user_id,role_id) VALUES (1,7);
INSERT INTO `roles_users` (user_id,role_id) VALUES (6,6);
INSERT INTO `roles_users` (user_id,role_id) VALUES (5,7);
INSERT INTO `roles_users` (user_id,role_id) VALUES (5,5);
CREATE TABLE role (
	id INTEGER NOT NULL, 
	name VARCHAR(80), 
	description VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
INSERT INTO `role` (id,name,description) VALUES (1,'user',NULL);
INSERT INTO `role` (id,name,description) VALUES (2,'adminrole',NULL);
INSERT INTO `role` (id,name,description) VALUES (3,'read',NULL);
INSERT INTO `role` (id,name,description) VALUES (4,'create',NULL);
INSERT INTO `role` (id,name,description) VALUES (5,'supervisor',NULL);
INSERT INTO `role` (id,name,description) VALUES (6,'delete',NULL);
INSERT INTO `role` (id,name,description) VALUES (7,'export',NULL);
COMMIT;
