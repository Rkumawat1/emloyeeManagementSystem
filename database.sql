CREATE DATABASE employee_db;

USE employee_db;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary INT
);

select * from employees