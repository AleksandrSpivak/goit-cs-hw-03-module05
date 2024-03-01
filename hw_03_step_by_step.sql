-- Отримати всі завдання певного користувача.
select title, description
from tasks 
where user_id = 2

-- Вибрати завдання за певним статусом.
select title, description
from tasks
where status_id in (
	select id 
	from status s 
	where s.name='new'
)	
	
-- Оновити статус конкретного завдання.
update tasks 
set status_id = 3
where id = 4

-- Отримати список користувачів, які не мають жодного завдання. 
select fullname 
from users u
where id not in (
	select t.user_id
	from tasks t 
)

--Додати нове завдання для конкретного користувача. 
insert into tasks (title, description, status_id, user_id)
values ('make this ASAP', 'create new table and populate it with the raw data', 1, 2)

--Отримати всі завдання, які ще не завершено. 
select title, description
from tasks t 
where status_id not in (
	select id 
	from status s
	where name='completed'
)

-- Видалити конкретне завдання. 
delete from tasks 
where id = 5

-- Знайти користувачів з певною електронною поштою.
select fullname, email
from users 
where email like 'a%'

-- Оновити ім'я користувача. 
update users 
set fullname = 'Aaa Bbbbbb'
where id = 3

-- Отримати кількість завдань для кожного статусу. Варіант 1
select count(title), status_id 
from tasks t 
group by status_id 

-- Отримати кількість завдань для кожного статусу. Варіант 2
select s.name as Status, count(title) 
from tasks as t 
join status as s on s.id = t.status_id 
group by s.name 

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
select u.fullname, t.title 
from tasks as t
join users as u on u.id = t.user_id 
where email like '%example.com'
order by u.fullname 

-- Отримати список завдань, що не мають опису. 
select title
from tasks t 
where description = '' 

-- Вибрати користувачів та їхні завдання, які є у статусі 'inProgress'
select u.fullname, t.title
from users as u 
inner join tasks as t on t.user_id = u.id 
where t.status_id in (
	select id 
	from status as s 
	where name = 'inProgress'
)
order by u.fullname 

-- Отримати користувачів та кількість їхніх завдань.
select u.fullname as user_name, count(t.title) as num_of_tasks
from users u 
left join tasks t on t.user_id = u.id 
group by u.fullname 
