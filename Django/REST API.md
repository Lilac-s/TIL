# REST API :seedling:



## HTTP



### 정의

- Hyper Text Transfer Protocol
- 웹 상에서 컨텐츠를 전송하기 위한 약속
- HTML 문서와 같은 리소스들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)
- 웹에서 이루어지는 모든 데이터 교환의 기초
- 요청(request)
  - 클라이언트에 의해 전송되는 메세지
- 응답(response)
  - 서버에서 응답으로 전송되는 메세지





### 특징

- 기본 특성
  - stateless : 상태가 없다(무상태)
  - connectionless : 비연결성
- 쿠키와 세션을 통해 서버 상태를 요청과 연결하도록 함





### HTTP 메세지

![image-20220421094607072](REST%20API.assets/image-20220421094607072.png)





### 요청 메서드(HTTP request methods)

- 자원에 대한 행위(수행하고자 하는 동작)을 정의
- 주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
- HTTP Method 예시
  - GET(조회), POST(작성), PUT(수정), DELETE(삭제)





### HTTP response status codes





### 웹에서의 리소스 식별

- HTTP 요청의 대상을 리소스(resource, 자원)라고 함
- 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음
- 각 리소스는 리소스 식별을 위해 HTTP 전체에서 사용되는 URI(Uniform Resource Identifier)로 식별됨





### URL, URN

- URL(Uniform Resource Locator)
  - 통합 자원 위치
  - 네트워크 상에 자원이 어디 있는지 알려주기 위한 약속
  - 과거에는 실제 자원의 위치를 나타냈지만 현재는 추상화된 의미론적인 구성
  - '웹 주소', '링크' 라고도 불림
- URN(Uniform Resource Name)
  - 통합 자원 이름
  - URL과 달리 자원의 위치에 영향을 받지않는 유일한 이름 역할을 함
  - 예시
    - ISBN(국제표준도서번호)





### URI

- Uniform Resource Identifier
  - 통합 자원 식별자
  - 인터넷의 자원을 식별하는 유일한 주소 (정보의 자원을 표현)
  - 인터넷에서 자원을 식별하거나 이름을 지정하는데 사용되는 간단한 문자열
  - 하위 개념
    - URL, URN
- URI는 크게 URL과 URN으로 나눌 수 있지만, URN을 사용하는 비중이 매우 적기 때문에 일반적으로 URL은 URI와 같은 의미처럼 사용하기도 함





### URI의 구조

