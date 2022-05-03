# 0503_homework



#### 1.  아래의 설명을 읽고 T/F 여부를 작성하시오.

- Event Loop는 Call Stack이 비워지면 Task Queue의 함수를 Call Stack으로 할당하는 역할을 한다.
  - T

- XMLHttpRequest(XHR)는 AJAX 요청 instance를 생성하는 Web API이다.  XHR객체를 활용하여 브라우저와 서버 간의 네트워크 요청을 전송할 수 있다.
  - T

- axios는 XHR(XMLHttpRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다
  - T






#### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

- `console.log('Hello SSAFY!')` 가 Call Stack 으로 들어간다.
- `setTimeout`을 Web API로 보내서 처리하도록 한 후 처리 Task queue에 줄세워놓는다.
- `console.log('Bye SSAFY!')` 가 Call Stack 으로 들어간다.
- Call Stack 이 빈 후 Event Loop가 Task queue에 있는 setTimeout을 Call Stack으로 보낸다.

