-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS db;

-- Use the newly created database
USE db;

-- Create the 'users' table
CREATE TABLE IF NOT EXISTS users (
    user_id INT NOT NULL,
    Full_Name VARCHAR(30) NOT NULL,
    Email VARCHAR(30) NOT NULL,
    Credit INT NOT NULL DEFAULT 0,
    PRIMARY KEY (user_id)
);

-- Create the 'eventu' table
CREATE TABLE IF NOT EXISTS eventu (
    event_id INT NOT NULL,
    typu VARCHAR(30) NOT NULL,
    description VARCHAR(30) NOT NULL,
    address VARCHAR(30) NOT NULL,
    dangerous_level VARCHAR(30) NOT NULL,
    user_id INT NOT NULL,
    approves INT NOT NULL DEFAULT 0,
    PRIMARY KEY (event_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create the 'approves' table
CREATE TABLE IF NOT EXISTS approves (
    event_id INT NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (event_id, user_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (event_id) REFERENCES eventu(event_id)
);

-- Create the 'comments' table
CREATE TABLE IF NOT EXISTS comments (
    event_id INT NOT NULL,
    user_id INT NOT NULL,
    comments VARCHAR(50) NOT NULL,
    FOREIGN KEY (event_id) REFERENCES eventu(event_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert initial data into 'users' table
INSERT IGNORE INTO users (user_id, Full_Name, Email) VALUES
(1, "Julian Tech", "julian@gmail.com"),
(2, "Mahdi", "Mahdi@gmail.com"),
(3, "Malik", "Malik@gmail.com"),
(4, "Zahi", "Zahi@gmail.com");

-- Insert initial data into 'eventu' table
INSERT IGNORE INTO eventu (event_id, typu, description, address, dangerous_level, user_id) VALUES
(1, "environmental", "gas leaked", "haifa", "Hard", 1),
(2, "environmental", "Tornado", "Tel AViv", "Medium", 1),
(3, "health", "corona", "haifa", "low", 2),
(4, "health", "viruses", "Plaza Hotel", "Hard", 3);

-- Print message indicating successful database creation
-- Note: This would typically be part of your Python script rather than an SQL file.
