.mode csv
.output low_rated_paid_apps.csv
select * from apps where score < 3.5 and category NOT LIKE "GAME%" and isfree =="False" order by reviewers desc limit 500; 
.output low_rated_free_apps.csv
select * from apps where score < 3.5 and category NOT LIKE "GAME%" and isfree =="True" order by reviewers desc limit 500; 
.output stdout