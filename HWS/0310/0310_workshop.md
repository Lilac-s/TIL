# 0310_workshop



## url.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
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

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }

    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
    return redirect('articles:detail', article.pk)
```



## template



### create.html

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
    

    <input type="submit"><br>
    <a href="{% url 'articles:index' %}">BACK</a>
  </form>

{% endblock content %}
```



### detail.html

```html
{% extends 'base.html' %}


{% block content %}
  <h1>{{ article.pk }}번째 글</h1>
  <hr>
  <p>제목 : {{ article.title }}</p>
  <p>내용 : {{ article.content }}</p>
  <p>작성일 : {{ article.created_at }}</p>
  <p>수정일 : {{ article.updated_at }}</p>
  <hr>

  <a href="{% url 'articles:edit' article.pk %}">EDIT</a>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <button>DELETE</button>
  </form>
  <br>
  
  <a href="{% url 'articles:index' %}">BACK</a>

{% endblock content %}
```



### edit.html

```html
{% extends 'base.html' %}


{% block content %}
  <h1>Edit</h1>

  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}

    <label for="totle">TITLE :</label>
    <input type="text" name="title" id="title" value="{{ article.title }}"><br>
    <label for="content">CONTENT :</label>
    <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>
    

    <input type="submit">
    <a href="{% url 'articles:index' %}">BACK</a>
  </form>

{% endblock content %}
```



### index.html

```html
{% extends 'base.html' %}


{% block content %}
  <h1>INDEX</h1>
  <hr>
  <a href="{% url 'articles:new' %}">NEW</a>
  {% for article in articles %}
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %} ">DETAIL</a>
    
    <hr>
  {% endfor %}

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

![image-20220310235606017](C:/Users/SSAFY_youji/AppData/Roaming/Typora/typora-user-images/image-20220310235606017.png)

### 2) Create

![image-20220310235621187](C:/Users/SSAFY_youji/AppData/Roaming/Typora/typora-user-images/image-20220310235621187.png)

### 3) Detail

![image-20220310235638793](C:/Users/SSAFY_youji/AppData/Roaming/Typora/typora-user-images/image-20220310235638793.png)

### 4) Update

![image-20220310235656995](C:/Users/SSAFY_youji/AppData/Roaming/Typora/typora-user-images/image-20220310235656995.png)