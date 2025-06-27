--lists all records with a score from hbtn_0c_0 in MySQL server
SELECT score, name 
FROM second_table 
WHERE score >= 10 
ORDER BY score DESC;
