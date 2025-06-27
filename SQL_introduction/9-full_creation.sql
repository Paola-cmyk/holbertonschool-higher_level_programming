-- Create the table with PRIMARY KEY on id
CREATE TABLE IF NOT EXISTS second_table (
    id INT PRIMARY KEY,
    name VARCHAR(256),
    score INT
);

-- Insert new rows, or update existing ones if id already exists
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), (4, 'George', 8)
ON DUPLICATE KEY UPDATE
    name = VALUES(name),
    score = VALUES(score);

