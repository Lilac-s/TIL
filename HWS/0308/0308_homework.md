# 0308_homework



## 1. Model 반영하기

migration



## 2. Model 변경사항 저장하기

### 1)

```python
python manage.py migrate
```

### 2)

```python
python manage.py sqlmigrate app_name 0001
```



## 3. Python Shell

```python
python manage.py shell_plus
```



## 4. Django Model Field

- Field.null
- Field.blank
- Field.choices
- Field.db_column
- Field.db_index