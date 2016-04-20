-- Adminer 4.2.2 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `roles_users`;
CREATE TABLE `roles_users` (
  `user_id` int(11) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  KEY `user_id` (`user_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `roles_users_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `roles_users_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 2016-04-06 19:38:46

DROP TABLE IF EXISTS `user`;

CREATE TABLE users (
	id INTEGER NOT NULL  AUTO_INCREMENT, 
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
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (1,'Admin',NULL,'admin','admin',1,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (2,'read','Brown','read','a',1,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (3,'create','Smith','create','$pbkdUXkss0JtM6ieMnpbh3o65vAzse.QsGSJtvzNe2UzZCnxSnosv7y0yigr5Ut5hwm7cGPDQQ',0,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (4,'user','Patel','user','$pb25000$XgvhXOud09rbG4NwLoXQWg$T6FdJkOrnrTH4oWfTuBO7Dnr202GrpnksQ5DF9YdyQQDwIH1Zd17EpiAe1vFBcFA',0,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (5,'suser','Jones','suser','$pba512$25000$9V7rHaPU2htjDKG09n5PiQvRpMkuu6a0wnk2RHcjhtHpmFLesO2PORPB1zBK8I.7w/CL4eIqAlQUQ3Ig',0,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (6,'delete','Williams','delete','$p2-sha512$20EM85euN2vHBm7637dzFMGp1BrScx13lWYcePPlJOuGCA',0,NULL);
INSERT INTO `users` (id,first_name,last_name,email,username,password,active,confirmed_at) VALUES (7,'Mia','Thomas','mia','$pblE1Hl2bSzEmC/zA',0,NULL);


INSERT INTO `roles_users` (user_id,role_id) VALUES (1,1);
INSERT INTO `roles_users` (user_id,role_id) VALUES (1,2);
INSERT INTO `roles_users` (user_id,role_id) VALUES (2,3);
INSERT INTO `roles_users` (user_id,role_id) VALUES (7,3);
INSERT INTO `roles_users` (user_id,role_id) VALUES (3,4);
INSERT INTO `roles_users` (user_id,role_id) VALUES (4,1);
INSERT INTO `roles_users` (user_id,role_id) VALUES (1,7);
INSERT INTO `roles_users` (user_id,role_id) VALUES (6,6);
INSERT INTO `roles_users` (user_id,role_id) VALUES (5,7);
INSERT INTO `roles_users` (user_id,role_id) VALUES (5,5);


DROP TABLE IF EXISTS `role`;

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

