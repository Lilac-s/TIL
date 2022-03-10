# 0309_workshop



## url.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
```



## view.py

```python
from django.shortcuts import redirect, render
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()[::-1]

    context = {
        'articles' : articles
    }

    return render(request, 'articles/index.html', context)


def new(request):

    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    # return render(request, 'articles/index.html')
    return redirect('articles:detail', article.pk)
```



## template\articles



### index.html

```html
{% extends 'base.html' %}


{% block content %}
  <h1>INDEX</h1>
  <hr>
  <a href="{% url 'articles:new' %}"></a>
  {% for article in articles %}
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %} ">DETAIL</a>
    
    <hr>
  {% endfor %}

{% endblock content %}
```



### new.html

```html
{% extends 'base.html' %}


{% block content %}
  <h1>New</h1>

  <form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    <label for="totle">TITLE :</label>
    <input type="text" name="title" id="title"><br>
    <label for="content">CONTENT :</label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea><br>
    

    <input type="submit">
    <a href="{% url 'articles:index' %}">BACK</a>
  </form>

{% endblock content %}
```



## model.py

```python
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```



## 이미지



### 1) Read

![image-20220310234656773](0309_workshop.assets/image-20220310234656773.png)



### 2) Create

![image-20220310234758466](0309_workshop.assets/image-20220310234758466.png)
