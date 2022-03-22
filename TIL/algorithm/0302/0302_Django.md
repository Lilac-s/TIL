# 0302_Django

D는 묵음이야~



#### 장고 = 밀키트!

뼈대. 다른 것들을 추가해서 커스터마이즈 할 수 있다.

파이썬 웹 프레임워크.



지금까지 한 제주도 카드 만들기 같은게 정적 웹 페이지이다.

앞으로는 동적 웹 페이지(Dynamic web page)를 할거야!



인스타그램도 장고를 이용해서 만든 거래!



- MVC Design Pattern > 이젠 잊어줘

- 장고에서 사용하는 MVC : MTV Pattern
  - MTV Pattern : 당장 우리는 이것만 알면 돼.
    - Model
    - Template : 눈에 보이는 HTML 파일. 어떻게 보여주지? 를 정한다.
      - HTML 파일이다.
    - View : 뭘 보여주지? 어떤 데이터를 보여주지? 를 정한다.
      - 함수이다.
      - MVC의 View랑은 완전히 다른 애야.



브라우저에서 url을 통해서 우리에게 요청이 왔다. urls.py

이걸 어떤 View랑 맵핑하니? 를 알려주는게 view.py

그리고 그걸 우리에게 보여주는게 template의 .html 파일.



git bash 에서 취소할 땐 ctrl+c