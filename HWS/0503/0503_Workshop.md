# 0503_Workshop



## 팔로우 구현



#### profile.html

```html
// accounts > templates\accounts > profile.html

{% with followers=person.followers.all followings=person.followings.all %}
  <div id="follow-cnt">
    팔로워 : {{ followers|length }} / 팔로우 : {{ followings|length }}
  </div>

  <div>
    {% if user != person %}
      <form data-person-pk="{{ person.pk }}" id='follow-form'>
        {% if user in followers %}
          <button>언팔로우</button>
        {% else %}
          <button>팔로우</button>
        {% endif %}
      </form>
    {% endif %}
  </div>
{% endwith %}
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const form = document.querySelector('#follow-form')

    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const personPk = form.dataset.personPk

    form.addEventListener('submit', function(event){
      event.preventDefault()
      axios({
        method: 'post',
        url: `/accounts/${personPk}/follow/`,
        headers: {
          'X-CSRFToken' : csrftoken
        }
      })
        .then(res=> {
          // 버튼 선택해서 값 바꿔주기
          // 팔로워 수 선택해서 값 바꿔주기
          const liked = res.data.liked
          const button = document.querySelector('button')
          if (liked === true) {
            button.innerText = '언팔로우'
          } else {
            button.innerText = '팔로우'
          }
          const followCnt = document.querySelector('#follow-cnt')

          const followerCnt = res.data.follower_cnt
          const followingCnt = res.data.following_cnt
          
          followCnt.innerText = `팔로워 : ${followerCnt} / 팔로우 : ${followingCnt}`
        })

    })
  </script>
```



#### views.py

```python
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        you = get_object_or_404(get_user_model(), pk=user_pk)
        me = request.user

        if me != you:
            if you.followers.filter(pk=me.pk).exists():
            # if me in you.followers.all():
                # 언팔로우
                you.followers.remove(me)
                liked = False
            else:
                # 팔로우
                you.followers.add(me)
                liked = True
            context = {
                'liked' : liked,
                'follower_cnt' : you.followers.count(),
                'following_cnt' : you.followings.count(),
            }
        return JsonResponse(context)
    return redirect('accounts:login')
```



- `csrf token` 넣는 코드

```javascript
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
```

- js에서 `id`를 사용한다. 그래서 `'#follow-form'`과 같이 사용할 수 있다.
- js에서 `post` 사용하는 방법 + `CSRFToken`

```javascript
axios({
        method: 'post',
        url: `/accounts/${personPk}/follow/`,
        headers: {
          'X-CSRFToken' : csrftoken
        }
      })
```

- view함수에서 `liked`, `follwer_cnt`, `following_cnt`를 설정해서 html 파일의 `axios`에서 사용한다.
  - 이와 같은 방법을 통해 페이지를 연속적으로 만들 수 있다.
- js에서 `pk` 사용하기
  - 아래와 같은 과정을 거쳐 `pk`값을 받고 사용할 수 있다.

```html
<form data-person-pk="{{ person.pk }}" id='follow-form'>
```

```javascript
const personPk = form.dataset.personPk
```





## 좋아요 구현



#### index.html

```html
// articles > templates\articles > index.html

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">CREATE</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인 하세요]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>작성자: <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></p>
    <p>글 번호: {{ article.pk }}</p>  
    <p>글 제목: {{ article.title }}</p>
    <p>글 내용: {{ article.content }}</p>
    
    <div>
      <form data-article-pk="{{ article.pk }}" class='like-form'>
        {% if user in article.like_users.all %}
        <input type="submit" value="좋아요 취소" id="input-{{article.pk}}">
        <i class="fa-solid fa-heart" style='color:red'></i>                  
        {% else %}
        <input type="submit" value="좋아요" id="input-{{article.pk}}">
        <i class="fa-solid fa-heart"></i>
        {% endif %}
      </form>
      <p id="cnt-{{article.pk}}">좋아요 수 :{{ article.like_users.count }}</p>

      
    </div>
    <a href="{% url 'articles:detail' article.pk %}">DETAIL</a>
    <hr>
  {% endfor %}

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    const likeForms = document.querySelectorAll('.like-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    likeForms.forEach( form => {
      form.addEventListener('submit', function(event){
        event.preventDefault()
        const articlePk = event.target.dataset.articlePk
        axios({
          method:'post',
          url: `/articles/${articlePk}/likes/`,
          headers: {
            'X-CSRFToken' : csrftoken,
          }
        })
        .then(res => {
          const liked = res.data.liked
          const likedCnt = res.data.like_cnt
          const p = document.querySelector(`#cnt-${ articlePk }`)
          p.innerText = `좋아요 수 : ${likedCnt}`
          const input = document.querySelector(`#input-${aritclePk}`)
          if (liked === true){
            input.value = '좋아요 취소'
            
          } else{
            input.value = '좋아요'
          }
        })
      })
    })


  </script>

{% endblock content %}
```





#### views.py

```python
@require_POST
def likes(request,article_pk):
    if request.user.is_authenticated :
        article = get_object_or_404(Article, pk=article_pk)
        
        #이미 좋아요를 눌렀다면
        if article.like_users.filter(pk=request.user.pk).exists() :
        # if request.user in article.like_users.all() : 
            article.like_users.remove(request.user) #좋아요 취소
            liked=False
        else : #아직 안눌렀다면
            article.like_users.add(request.user) #좋아요\
            liked=True
        context = {
            'liked' : liked,
            'like_cnt': article.like_users.count(),
        }
        return JsonResponse(context)

        return redirect('articles:index')
    return redirect('accounts:login')
```

