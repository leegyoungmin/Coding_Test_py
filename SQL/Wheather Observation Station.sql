/* 1 */
select city, state from station;

/* 3 */
select distinct city from station where mod(id, 2) = 0;

/* 4 */
select count(city) - count(distinct city) from station;

/* 5 */
select city, length(city) from station
order by length(city) asc, city asc
    limit 1;

/* 6 */
select city, length(city) from station
order by length(city) desc, city desc
    limit 1;

/* 7 */
select distinct city from station
where city like '%a'
   or city like '%e'
   or city like '%i'
   or city like '%o'
   or city like '%u';