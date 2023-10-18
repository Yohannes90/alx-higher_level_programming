-- creates the database hbtn_0d_2
-- creates the user user_0d_2
    -- with password user_0d_2_pwd
    -- and only SELECT privilege in the database hbtn_0d_2

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
