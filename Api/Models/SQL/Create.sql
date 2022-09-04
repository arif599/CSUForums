-- creating csuforums database
CREATE DATABASE csuforums;

-- creating the users table
CREATE TABLE users(
	userID BIGSERIAL PRIMARY KEY,
	username VARCHAR(25) NOT NULL UNIQUE,
	password VARCHAR(225) NOT NULL,
	verified BOOLEAN DEFAULT FALSE
);

ALTER TABLE users ALTER COLUMN password TYPE VARCHAR(65);
-- creating the posts table
CREATE TABLE posts(
	postID BIGSERIAL PRIMARY KEY,
	userID BIGINT REFERENCES users(userID) NOT NULL,
	voteCount INT DEFAULT 1,
	title VARCHAR(225) NOT NULL,
	body TEXT NOT NULL,
	publishedDate DATE
);

-- creating the comments table
CREATE TABLE comments(
	commentID BIGSERIAL PRIMARY KEY,
	userID BIGINT REFERENCES users(userID) NOT NULL,
	postID BIGINT REFERENCES posts(postID) NOT NULL,
	voteCount INT DEFAULT 1,
	body TEXT NOT NULL,
	publishedDate DATE
);



-- testing  queries
INSERT INTO users(username, password) VALUES ('lilreef599', 'password123');
SELECT userID FROM users WHERE username='lilreef599';

INSERT INTO posts(userID, title, body, publishedDate) VALUES(
	1, 'test title', 'test body', '2021-8-9' 
);

-- deleting tables
DROP TABLE users;