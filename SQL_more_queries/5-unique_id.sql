--unique id
DROP DATABASE IF EXISTS hbtn_test_db_5;
CREATE DATABASE IF NOT EXISTS hbtn_test_db_5;
INSERT INTO unique_id (name) VALUES ("Holberton School");
INSERT INTO unique_id (id, name) VALUES (2, "Holberton");
INSERT INTO unique_id (id, name) VALUES (3, "School");
INSERT INTO unique_id (id, name) VALUES (4, "C is fun");
INSERT INTO unique_id (id, name) VALUES (5, "Python is cool");
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
