# pjt 09 아침 수업



처음 세팅 다 한 후



```bash
$ python manage.py loaddata movies.json
```

모든 데이터를 `loaddata`로 만드는 건 하지 말자.

`loaddata`는 가지고 있는 데이터를 보내고, 받을 때 사용하는 거야.



영화를 어떤 식으로 추천해줄까?

ex) 본인이 보유하고 있는 주식 종목을 가지고 영화 추천받기 (대체 어떻게..??)

날씨 데이터로 추천해주기

완전한 랜덤 추천

등등등..



가장 많이 사용하는 추천 알고리즘

***collaborative filtering***

아예 기초 지식이 없는 사람은 이걸 공부하는 것부터 일일 것이다.



오늘의 핵심

1. AJAX로 만들기
2. 어떻게 추천할 건지 고민을 좀 해보자



프로젝트 소개 끝!

---



## Social Login



django allauth

'구글로 로그인하기'를 구현할거에요



1. django allauth 설치하기

2. 코드 적기

```python
# installed_apps 바로 위에

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
```

```python
# installed_apps에 코드 추가
'django.contrib.sites',

'allauth',
'allauth.account',
'allauth.socialaccount',
```

```python
# 다 적으면 이런 모양이다 (구글 기준)
INSTALLED_APPS = [
    # Local
    'accounts',
    'community',
    'movies',
    # 3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # Native
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]
```



3. `python manage.py migrate` 하기 : 앱을 추가했을 때 `migrate` 해줘야함

4. `python manage.py createsuperuser` 로 admin user 만들기



4. 코드 추가

```python
# installed_apps 밑에
SITE_ID = 1
```

반드시 site id 설정 필요! 그래야 runserver가 된다.



> 관련 내용을 검색할 때에는 OAuth로 검색해야 한다.
>
> [OAuth와 춤을](https://d2.naver.com/helloworld/24942)



5. 구글 로그인 구현

>[구글 클라우드 플랫폼](https://cloud.google.com/gcp/?utm_source=google&utm_medium=cpc&utm_campaign=japac-AU-all-en-dr-bkwsrmkt-all-all-trial-e-dr-1009882&utm_content=text-ad-none-none-DEV_c-CRE_540822941662-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20GCP%20~%20General_cloud%20-%20platform-KWID_43700061090678933-kwd-87853815&userloc_1009887-network_g&utm_term=KW_gcp&gclid=CjwKCAjw682TBhATEiwA9crl3_hx5kr_0bTeKCvhxqzPWCiPKT20uBnZTOl5sV4hMnbRL7AdpbFiOhoC-0sQAvD_BwE&gclsrc=aw.ds)
>
>1. 오른쪽 위 콘솔 들어가기
>
>프로젝트 선택 > 새 프로젝트 만들기
>
>프로젝트 화면으로 들어가기
>
>2. api 및 서비스 눌러서 들어가기
>
>oauth 동의 화면
>
>user type 외부 선택
>
>진짜 프로젝트 할때는 다 입력하는게 좋다.
>
>저장 후 계속
>
>범위 추가 또는 삭제 > 원하는 데이터 선택 > 업데이트
>
>저장 후 계속
>
>테스트 사용자 : add users해서 내 이메일 넣기
>
>끝. 대시보드로 돌아가기
>
>3. 사용자 인증 정보 들어가기
>
>사용자 인증 정보 만들기 > OAuth 클라이언트 ID 만들기\
>
>애플리케이션 유형 > 웹 애플리케이션
>
>이름 > 내가 식별할 수 있는 것으로 (나만 확인함)
>
>승인된 리디렉션 URI > django-allauth 문서의 Providers에서 확인가능
>
>`http://127.0.0.1:8000/accounts/google/login/callback/`
>
>그대로 붙여넣고 만들기 누르면 test를 위한 과정을 끝난다.
>
>[OAuth 2.0을 사용하여 Google API에 액세스](https://developers.google.com/identity/protocols/oauth2)
>
>![image-20220506095019894](%EC%95%84%EC%B9%A8%20%EC%88%98%EC%97%85.assets/image-20220506095019894.png)
>
>요런 모양이 나오면 된다.

우리의 admin 페이지로 돌아가서 소셜 어플리케이션에 추가한다.

제공자 google, 이름은 마음대로.

방금 전에 제공받은 클라이언트 아이디와 비밀 키를 넣고

site는 example로 일단 넣는다. > 저장

> 이제 우리가 뭘 하면 알아서 해줄 거야.



6. 코드 추가

```python
# urls.py (master)
path('accounts/', include('allauth.urls')),
```

accounts 이름 겹쳐도 상관없음.



7. 코드 추가

django allauth 사이트의 templates에 가면 social account tags라는 탭이 있다.

여기의 코드를 적당히 변경해서 넣으면 구글 로그인하러 가는 태그를 만들 수 있음.

```html
{% comment %} login.html {% endcomment %}

{% extends 'base.html' %}

{% load socialaccount %}

{% block content %}
<h1>로그인</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
<div>
  <a href="{% provider_login_url "google" next="/community/" %}">[google login]</a>
</div>
{% endblock  %}
```



8. 이상한 중간 화면을 안 보고 싶다면

django allauth 사이트의 configuration으로 들어간다.

**SOCIALACCOUNT_LOGIN_ON_GET (=False)**

을 변경해 주면 된다고 한다.

코드 추가

```python
# settings.py site_id 바로 밑에

# social login 바로 넘어가기
SOCIALACCOUNT_LOGIN_ON_GET = True
```



9. 이제 DB 가서 확인해 보면 이런저런거 받은 걸 볼 수 있는데, 안 받아지는건 구글 문서를 봐야 함..



auth signup 끝!

---



## Paginator



[django paginator](https://docs.djangoproject.com/en/4.0/topics/pagination/)

```python
# views.py

from django.core.paginator import Paginator

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movies' : page_obj,
    }
    return render(request, 'movies/index.html', context)
```



> ctrl + F 한 다음에 > 누르고 위에 바꾸고자 하는 단어, 아래에 새로운 단어 적고
>
> 오른쪽 버튼 누르면 한번에 다 바뀜



못생겼으니까 bootstrap form 쓸거래

[django bootstrap 5 pagination](https://django-bootstrap-v5.readthedocs.io/en/latest/templatetags.html#bootstrap-pagination)



1. 설치

```bash
$ pip install django-bootstrap-v5
```



2. 코드추가

```python
# settings.py

INSTALLED_APPS = [
    # Local
    'accounts',
    'community',
    'movies',
    # 3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'bootstrap5',
    # Native
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]
```

```html
// index.html

{% load bootstrap5 %}

...

  <div>
    {% bootstrap_pagination movies %}
  </div>
```



페이지네이션 끝! 하지만 이제 스크롤을 할 거래

---



## Infinite Scroll

![image-20220506104329332](%EC%95%84%EC%B9%A8%20%EC%88%98%EC%97%85.assets/image-20220506104329332.png)

이중에 우리가 안 배운건 없으니 할 수 있다..

할 수 있다..

할..



1. 코드 추가

```html
// base.html

  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  
  {% block script %}{% endblock script %}
```

스크립트 블록 만들고 axios cdn 불러오기

```python
# settings.py

INSTALLED_APPS = [
    # Local
    'accounts',
    'community',
    'movies',
    # 3rd party
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'bootstrap5',
    'rest_framework',
    # Native
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]
```

`'rest_framework'` 추가



[Element.scrollHeight](https://developer.mozilla.org/ko/docs/Web/API/Element/scrollHeight)

스크롤 관련한 mdn 문서



너무 빡세짐..

