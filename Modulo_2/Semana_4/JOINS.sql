--JOINS

--1. Obtenga todos los libros y sus autores

Select b.name, a.name as author_name
from books b
join authors a on b.author_id = a.ID;

--2. Obtenga todos los libros que no tienen autor

Select b.name, a.name as author_name
from books b
left join authors a on b.author_id = a.ID
where a.ID is null;

--3. Obtenga todos los autores que no tienen libros

Select a.name as author_name
from authors a
left join books b on b.author_id = a.ID
where b.ID is null;

--4. Obtenga todos los libros que han sido rentados en algún momento

Select distinct b.name
from books b
join rents r on b.ID = r.book_id;

--5. Obtenga todos los libros que nunca han sido rentados

Select distinct b.name
from books b
left join rents r on b.ID = r.book_id
where r.ID is null;

--6. Obtenga todos los clientes que nunca han rentado un libro

Select distinct c.name
from customers c
left join rents r on c.ID = r.customer_id
where r.ID is null;

--7. Obtenga todos los libros que han sido rentados y están en estado “Overdue”

Select distinct b.name
from books b
join rents r on b.ID = r.book_id
where r.state = 'Overdue';

















