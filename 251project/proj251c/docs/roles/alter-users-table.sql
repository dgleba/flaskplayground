
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Title:  .
-----------------------2016-04-13[Apr-Wed]12-34PM

ALTER TABLE  `users` ADD column 	active BOOLEAN after email;

ALTER TABLE  `users` ADD column 	confirmed_at DATETIME after email;

ALTER TABLE  `users` ADD column 	first_name VARCHAR(255)  after email;
ALTER TABLE  `users` ADD column 	last_name VARCHAR(255)  after first_name;

ALTER TABLE `users` DROP INDEX `PRIMARY`;
ALTER TABLE  `users` ADD Unique  (username);
ALTER TABLE  `users` ADD Unique  (email);

ALTER TABLE users ADD id INT PRIMARY KEY AUTO_INCREMENT;


=

    

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

