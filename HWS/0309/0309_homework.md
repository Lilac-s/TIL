# 0309_homework



## Django Model



### 1)

```python
python manage.py makemigrations
```

```python
python manage.py migrate
```



### 2)

#3

id 값을 적어 주어야 한다.



### 3)

#2

음수 인덱싱은 불가능하다.



### 4)

```python
article = Article.objects.get(pk=1)
article.title = '안녕하세요'
article.save()
```

```python
article = Article.objects.get(pk=1)
article.content = '반갑습니다'
article.save()
```



### 5)

```python
posts = Post.objects.all()
```

