"""

DISTINCT        >>  for showing Unique  
order by ASC    >>  ordering ascending order
order by desc   >>  ordering descending order
limit 3         >>  only shows 3 entries
offset 2        >>  cut 2 entries from top
IN              >>  check entries from a list
OR              >>  or condition
AND             >>  and condition
LIKE            >>  check string with similar characters ("%A" or "A%" or "__A" )




*********************************************************************************
************************************* JOINS *************************************
*********************************************************************************


Inner Join | Join               >>  commonn entries in both tables
Left Join                       >>  inner join + entries from left table
Right Join                      >>  inner join + entries from Right table
Full Outer Join | Full Join     >>  inner Join + left Join + right Join
Cross Join                      >>  returns cartesian product (product of both tables - numbers of entries)
Natural Join                    >>  sql decide on which column the join should happeny 
Self Join                       >>  join with itself



Examples:

1.  INNER JOIN | JOIN

    select e.emp_name, d.dept_name
    from employees e 
    inner join department d on e.dept_id = d.dept_id;


2.  LEFT JOIN

    select e.emp_name, d.dept_name
    from employees e 
    left join department d on e.dept_id = d.dept_id;


3.  RIGHT JOIN

    select e.emp_name, d.dept_name
    from employees e 
    right join department d on e.dept_id = d.dept_id;


4.  FULL JOIN | FULL OUTER JOIN

    select e.emp_name, d.dept_name
    from employees e 
    full join department d on e.dept_id = d.dept_id;


5.  CROSS JOIN (Don't need 'on')

    select e.emp_name, d.dept_name
    from employees e 
    cross join department d;


6.  NATURAL JOIN (Don't need 'on')

    select e.emp_name, d.dept_name
    from employees e 
    natural join department d;


7.  SELF JOIN 

    select child.name as child_name, child.age as child_age, parent.name as parent_name, parent.age as parent_age
    from family as child  
    join family as parent on child.parent_id = parent.member_id ;




*******************************************************************************************
************************************* WINDOWS FUNCTION ************************************
*******************************************************************************************


Table -->   select * from employees;


select e.*, max(salary) over() as Max_Salary
from employees e
group by dept_name;


select e.*, max(salary) over(partition by dept_name) as Max_Salary
from employees e;



1.  Row Number  >> Count the number of rows

    select e.*, 
    row_number() over(partition by dept_name order by emp_id) as rn
    from employees e ;


    >>  Fetch the first 2 employees from each department to join the company

        select * from ()
            select e,*,
            row_number() over(partition by dept_name order by emp_id) as rn
            from employees.e) as x
        where x.rn < 3 ;
        
    
    
2.  RANK    >>  skip a value for every duplicate value

    select e.*, 
    rank() over(partition by dept_name order by emp_id) as rn
    from employees e ;

    >>  Fetch top 3 employees whose has max salary from each department 
        
        select * from ()
            select e.*,
            rank() over(partition by dept_name order by salary desc) as rnk
            from employees.e) as x
        where x.rnk < 4 ;
    
       
3.  DENSE RANK  >>  Not skip a value for every duplicate value
    
    select e.*, 
    dense_rank() over(partition by dept_name order by emp_id) as dns_rnk
    from employees e ;
    
    >>  Fetch top 3 employees whose has max salary from each department [Using dense Rank]
        
        select * from ()
            select e,*,
            dense_rank() over(partition by dept_name order by salary desc) as dns_rnk
            from employees.e) as x
        where x.dns_rnk < 4 ;


4.  LEAD    >>  Next data

    select e.*,
    lead(salary) over(partition by dept_name order by emp_id) as prev_empl_salary
    from employees e;


5.  LAG     >>  previous data

    select e.*,
    lag(salary, 2, 0) over(partition by dept_name order by emp_id) as prev_empl_salary
    from employees e;
    
    here, 0 > default 
          2 > previous 2nd data 
    

    >>  Fetch a query to display if the salary of an employee is higher, lower or equal to the previous employee

        select e.*,
        lag(salary) over(partition by dept_name order by emp_id) as prev_empl_salary,
        
        case when e.salary > lag(salary) over(partition by dept_name order by emp_id) then "Higher then previous employee"
            when e.salary < lag(salary) over(partition by dept_name order by emp_id) then "Lower then previous employee"
            when e.salary = lag(salary) over(partition by dept_name order by emp_id) then "same as then previous employee"
            end salary_range
        from employees e;


6.  first_value >>  gives the first value

    select *,
    first_value(product_name) over(partition by product_category order by price desc) as most_expensive_product
    from product;


7.  last_value  >>  gives the last value

    select *,
    first_value(product_name) 
        over(partition by product_category order by price desc) 
        as most_expensive_product,
    last_value(product_name) 
        over(partition by product_category order by price desc
            range between unbounded preceding and unbounded following) 
        as least_expensive_product
    from product;


8.  Frames  >>  subpart of window
    By default  >> range between unbounded preceding and current row
    
    it can be like
        row between 2 precceding and 2 following
        row between unbouded preceding and 2 following
        row between unbounded preceding and unbounded following


9.  Nth Value  

    select *,
    first_value(product_name) over w as most_expensive_product,
    last_value(product_name) over w as least_expensive_product,
    nth_value(product_name, 2) over w as second_most_expensive_product
    from product
    window w as (partition by product_category order by price desc 
            range between unbounded preceding and unbounded following);


10. NTILE   >>  to group together and divide into buckets  

    select *,
    ntile(3) over (order by price desc) as buckets
    from products
    where product_category = 'Phones';

    >>  Write a query to segregate all the expensive, cheaper and mid range phones.
    
        select product_name,
            case when x.buckets = 1  then "Expensive Phones"
                when x.buckets = 2  then "Mid range Phones"
                when x.buckets = 3  then "cheaper Phones"
            end phone_category
        
        from            
            (select *, 
            ntile(3) over (order by price desc) as buckets
            from products
            where product_category = 'Phones') as x
        

11. CUME_DIST (Cumalative distribution)
    value   --> 1<= cume_dist > 0
    formula --> current row no (or row number with valuesame as current row)/ total no of rows


    select *,
    cume_dist() over(order by price desc) as cume_distribution
    round(cume_dist() over(order by price desc)::numeric *100, 2) as cume_distribution_percentage
    from products;


    >> Query to fetch all products which are constituting the first 30% 
    
        select product_name, (cume_distribution_percentage||'%') as cume_distribution_percentage
        from (
            select *,
            cume_dist() over(order by price desc) as cume_distribution
            round(cume_dist() over(order by price desc)::numeric *100, 2) as cume_distribution_percentage
            from products) x
            
        where x.cume_distribution_percentage <= 30;


12. PERCENT_RANK
    value   --> 1<= percent_rank > 0
    formula --> current row no -1 / total no of rows -1


    select *,
    percent_rank() over(order by price desc) as percent_rank
    round(percent_rank() over(order by price desc)::numeric *100, 2) as per_rank
    from products;


    >> Query to fetch all products which are constituting the first 30% 
    
        select product_name, per_rank
        from (
            select *,
            percent_rank() over(order by price desc) as percent_rank
            round(percent_rank() over(order by price desc)::numeric *100, 2) as per_rank
            from products) x
            
        where x.product_name = 'Galaxyy Z Fold 3';













ALTERNATE WAY TO WRITE SQL QUERY USING WINDOWS FUNCTION 



    select *,
    first_value(product_name) over w as most_expensive_product,
    last_value(product_name) over w as least_expensive_product
    from product
    window w as (partition by product_category order by price desc 
            range between unbounded preceding and unbounded following);
    
    
    
    

"""
