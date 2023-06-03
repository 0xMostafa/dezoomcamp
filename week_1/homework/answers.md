# Week 1 Homework (part 1) Answers

[Questios](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/cohorts/2023/week_1_docker_sql/homework.md)

## Question 1

- `--iidfile string`

```
docker build --help | grep -i "write the image id"
```

---


## Question 2

- 3

```
Package    Version
---------- -------
pip        22.0.4
setuptools 57.5.0
wheel      0.40.0
```
---

## Question 3

- 20530

```sql
select
	count(t."VendorID"),
	t."lpep_pickup_datetime"::date,
	t."lpep_dropoff_datetime"::date
from trips AS t
where t."lpep_pickup_datetime"::date = '2019-01-15'
and t."lpep_dropoff_datetime"::date = '2019-01-15'
group by 2, 3;
```

---

## Question 4

- 2019-01-15

```sql
select
	trips."lpep_pickup_datetime"::date,
	trips."trip_distance"
from trips
order by 2 desc;
```

---

## Question 5

- 2: 1282 ; 3: 254

```sql
select 
	trips."passenger_count",
	count(*) as trip_count
from trips
where trips."lpep_pickup_datetime"::date = '2019-01-01'
and passenger_count in (2,3)
group by passenger_count
```

---

## Question 6

- Long Island City/Queens Plaza

```sql
SELECT zdo."Zone", t."tip_amount"
FROM trips AS t
JOIN zones AS zpu
ON t."PULocationID" = zpu."LocationID"
AND zpu."Zone" = 'Astoria'
JOIN zones AS zdo
ON t."DOLocationID" = zdo."LocationID"
ORDER BY t."tip_amount" DESC
```

---