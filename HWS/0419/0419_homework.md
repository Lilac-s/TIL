# 0419_homework



## 1. MTV

MTV는 장고의 디자인 패턴으로, Model-Template-View의 약자이며 MVC패턴과 같이 한 요소가 다른 요소들에게 영향을 주지 않도록 설계하는 방식이다.

- Model
  - DB에 저장되는 데이터를 의미한다. 모델은 클래스로 정의되며 하나의 클래스가 하나의 DB Table이다. 
  - 장고는 ORM(Object Relational Mapping)기능을 지원하기 때문에 파이썬 코드로 DB를 조작할 수 있다.
- Template
  - 유저에게 보여지는 화면을 의미한다. 장고는 뷰에서 로직을 처리한 후 html 파일을 context와 함께 렌더링하는데 이 때의 html 파일을 템플릿이라 칭한다. 
  - 장고는 자체적인 Django Template 문법을 지원하며 이 문법 덕분에 html 파일 내에서 context로 받은 데이터를 활용할 수 있다.
- View
  - 요청에 따라 적절한 로직을 수행하여 결과를 템플릿으로 렌더링하며 응답한다. 다만 항상 템플릿을 렌더링하는 것이 아니라, 백엔드에서 데이터만 주고받을 때가 있다.





## 2. 404 Page not found

(a) : `articles`

(b) : `views`

(c) : `views.index, name:'index'`





## 3. templates and static

(a) : settings.py

(b) : [BASE_DIR / 'templates']

(c) : STATICFILES_DIRS



## 4. migration

1. `python manage.py makemigrations`
2. `python manage.py showmigrations`
3. `python manage.py sqlmigrate 앱 이름 0001`
4. `python manage.py migrate`





## 5. ModelForm True or False

F

T

F

T





## 6. media 파일 경로

`MEDIA_ROOT = BASE_DIR/CRUD`

`MEDIA_URL`





## 7. DB True or False

T

F

T

T

F





## 8. on_delete

`Protect`





## 9. Like in models

(a) : `ManyToManyField`

(b) : `related_name`





## 10. Follow in models

accounts_User_follwings

User_id : bigint

followings_id : bigint