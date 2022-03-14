# 0314_workshop



## SQL Query

### 1

```sql
CREATE TABLE countries (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 room_num TEXT NOT NULL,
 check_in TEXT NOT NULL,
 check_out TEXT NOT NULL,
 grade TEXT NOT NULL,
 price INT NOT NULL
);
```



### 2

```sql
INSERT INTO countries VALUES (1, 'B203', '2019-12-31', '2020-01-03', 'suite', 900);
INSERT INTO countries VALUES (2, '1102', '2020-01-04', '2020-01-08', 'suite', 850);
INSERT INTO countries VALUES (3, '303', '2020-01-01', '2020-01-03', 'deluxe', 500);
INSERT INTO countries VALUES (4, '807', '2020-01-04', '2020-01-07', 'superior', 300);
```



### 3

```sql
ALTER TABLE countries RENAME TO hotels;
```



### 4

```sql
SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;
```



### 5

```sql
SELECT grade, count(grade) FROM hotels GROUP BY grade ORDER BY count(grade) DESC;
```



### 6

```sql
SELECT * FROM hotels WHERE grade='deluxe' OR room_num LIKE 'B%';
```



### 7

```sql
SELECT * FROM hotels WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04' ORDER BY price ASC;
```

