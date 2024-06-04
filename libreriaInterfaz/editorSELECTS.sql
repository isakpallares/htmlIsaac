SELECT FIRST_NAME, LAST_NAME, SALARY
FROM EMPLOYEES;

SELECT DEPARTMENT_ID, LOCATION_ID
FROM DEPARTMENTS;

SELECT *
FROM REGIONS;

SELECT *
FROM EMPLOYEES;

SELECT *
FROM DEPARTMENTS;


SELECT LAST_NAME, SALARY, SALARY + 300
FROM EMPLOYEES;

SELECT LAST_NAME, SALARY,12 * SALARY + 100 , 12 *(SALARY + 100)
FROM EMPLOYEES;

SELECT LAST_NAME AS APELLIDO, COMMISSION_PCT+10 COMISION
FROM EMPLOYEES E;

SELECT LAST_NAME APELLIDO, COMMISSION_PCT+10 COMISION
FROM EMPLOYEES E;

SELECT LAST_NAME || " " || FIRST_NAME AS NOMBRECOMPLETO
FROM EMPLOYEES;

SELECT department_id 
FROM employees;

SELECT DISTINCT department_id 
FROM employees;

SELECT employee_id, last_name, job_id, department_id
FROM employees
WHERE department_id = 90;

SELECT employee_id, last_name, job_id, department_id
FROM employees
WHERE last_name = 'Whalen';

SELECT employee_id, last_name, job_id, department_id
FROM employees
WHERE hire_date = '1987-06-17';

--Apellido y salario de las personas que ganan entre 2500 y 3500 dolares

SELECT last_name, salary
FROM employees
WHERE salary >= 2500 AND salary <= 3500;

-- Función between

SELECT last_name, salary
FROM employees
WHERE salary BETWEEN 2500 and 3500
ORDER BY SALARY DESC;

--Operador In
--Mostrar el id, apellido, salario e id del manager de aquellos...
--cuyo manager tienen id 100,101,201.

SELECT employee_id, last_name, salary, manager_id
FROM employees
WHERE manager_id = 100 OR manager_id = 101 OR manager_id = 201;

SELECT employee_id, last_name, salary, manager_id
FROM employees
WHERE manager_id IN (100,101,201);

--Mostrar el id, apellido, salario e id del manager de aquellos
--empleados cuyo manager tienen id 124,145,205 y cuyo salario es mayor a 2500 dolares

SELECT employee_id, last_name, salary, manager_id
FROM employees
WHERE manager_id IN (124,145,205) and salary > 2500;

--Operador like

SELECT first_name
FROM employees
WHERE first_name LIKE '_i%';
--porcentaje al lado es que inicie en la letra, dos porcentaje y letra en medio es donde sea y '_i%' es con segunda letra

SELECT last_name, department_id, salary
FROM employees
ORDER BY department_id, salary DESC;

--Operador Join 

SELECT e.first_name, e.last_name, e.department_id, d.department_name 
FROM employees e
JOIN departments d
ON (e.department_id = d.department_id);

SELECT e.first_name, e.salary, j.job_title
FROM employees e
JOIN jobs j
ON (e.job_id = j.job_id)
ORDER BY salary DESC;

SELECT e.first_name, e.salary, d.department_name, l.city
FROM employees e
JOIN departments d
ON (e.department_id = d.department_id)
JOIN locations l
ON (d.location_id = l.location_id)
ORDER BY salary DESC;

--FUnciones Multifila

SELECT COUNT(*)
FROM employees
WHERE department_id = 50;

SELECT AVG(salary), MAX(salary), MIN(salary), SUM(salary)
FROM employees;

SELECT AVG(e.salary)
FROM employees e
JOIN departments j
ON (e.department_id = j.department_id)
WHERE j.department_name = 'marketing'


