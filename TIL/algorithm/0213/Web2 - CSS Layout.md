# Web2 - CSS Layout

- CSS layout techniques
  - Display
  - Position
  - Float (CSS1, 1996)
  - Flexbox (2012)
  - Grid (2017)
  - 기타
    - Responsive Web Design(2010), Media Queries(2012)



## Float:x:

- 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다는 CSS 원칙상에서 어떤 요소를 감싸는 형태 혹은 좌/우측 배치를 어떻게 할 것인가? : Float 이용



- Float 속성
  - none : 기본값
  - left : 요소를 왼쪽으로 띄움
  - right :  요소를 오른쪽으로 띄움



- Clearing Float

  - Float는 Normal Flow에서 벗어나 부동 상태(떠 있음)

  - 따라서, 이후 요소에 대하여 Float 속성이 적용되지 않도록 Clearing이 필수적임

    - `::after` : 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성

      ![image-20220213184756693](Web2%20-%20CSS%20Layout.assets/image-20220213184756693.png)

      - 보통 content 속성과 함께 짝지어, 요소에 장식용 콘텐츠를 추가할 때 사용

    - clear 속성 부여



- Float 정리
  - Float는 레이아웃을 구성하기 위해 필수적으로 활용 되었으며, 최근에는 Flexbox, Grid 등장과 함께 사용도가 낮아졌다.
  - Float 활용 전략 - Normal Flow에서 벗어난 레이아웃 구성
    - 원하는 요소들을 Float로 지정하여 배치
    - 부모 요소에는 반드시 Clearing Float를 하여 이후 요소부터 Normal Flow를 가지도록 지정



## Flexbox

- CSS Flexible Box Layout

  - 행과 열 상태로 아이템들을 배치하는 1차원 레이아웃 모델

  - 축

    - main axis(메인 축)
    - cross axis(교차 축)

  - 구성 요소

    - Flex Container(부모 요소)
    - Flex Item(자식 요소)

    ![image-20220213185141259](Web2%20-%20CSS%20Layout.assets/image-20220213185141259.png)

    

    ![image-20220213185242494](Web2%20-%20CSS%20Layout.assets/image-20220213185242494.png)





- Flexbox 구성 요소

  - Flex Container(부모 요소)

    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    - Flex Item들이 놓여있는 영역
    - display 속성을 flex 혹은 inline-flex로 지정

  - Flex Item(자식 요소)

    - 컨테이너에 속해 있는 컨텐츠(박스)

    - 부모 요소에 display: flex 혹은 inline-flex

      ![image-20220213185419756](Web2%20-%20CSS%20Layout.assets/image-20220213185419756.png)



- 왜 Flexbox를 사용해야 할까?
  - 이전까지 Normal Flow를 벗어나는 수단은 Float 혹은 Position이었다. 이 때, 수동 값 부여 없이 수직 정렬과 아이템의 너비와 높이 혹은 간격을 동일하게 배치하기가 어려웠다. flexbox는 부모 요소에 display함으로써 그것을 보다 편리하게 해 준다.



- Flex 속성:star:
  - 배치 설정
    - flex-direction
    - flex-wrap
  - 공간 나누기
    - justify-content (main axis)
    - align-content (cross axis)
  - 정렬
    - align-items (모든 아이템을 cross axis 기준으로)
    - align-self (개별 아이템)



- Flex 속성 : flex-direction

  - Main axis 기준 방향 설정

  - 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)

    ![image-20220213194713351](Web2%20-%20CSS%20Layout.assets/image-20220213194713351.png)



- Flex 속성 : flex-wrap

  - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정

  - 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함

    ![image-20220213194807435](Web2%20-%20CSS%20Layout.assets/image-20220213194807435.png)



- Flex 속성 : flex-direction & flex-wrap

  - flex-direction : Main axis의 방향을 설정

  - flex-wrap : 요소들이 강제로 한 줄에 배치되게 할 것인지 여부 설정

    - nowrap (기본 값) : 한 줄에 배치
    - wrap : 넘치면 그 다음 줄로 배치

  - flex-flow

    - flex-direction과 flex-wrap의 shorthand

    - flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성

      예시) flex-flow: row nowrap;



- Flex 속성 : justify-content

  - Main axis를 기준으로 공간 배분

    ![image-20220213195026182](Web2%20-%20CSS%20Layout.assets/image-20220213195026182.png)



- Flex 속성 : align-content

  - Cross axis를 기준으로 공간 배분 (아이템이 한 줄로 배치되는 경우 확인할 수 없음)

    ![image-20220213195109926](Web2%20-%20CSS%20Layout.assets/image-20220213195109926.png)



- Flex 속성 : justify-content & align-content
  - 공간 배분
    - flex-start (기본 값) : 아이템들을 axis 시작점으로
    - flex-end : 아이템들을 axis 끝 쪽으로
    - center : 아이템들을 axis 중앙으로
    - space-between : 아이템 사이의 간격을 균일하게 분배
    - space-around : 아이템을 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽에)
    - space-evenly : 전체 영역에서 아이템 간 간격을 균일하게 분배



- Flex 속성 : align-items

  -  모든 아이템을 Cross axis를 기준으로 정렬

    ![image-20220213195324092](Web2%20-%20CSS%20Layout.assets/image-20220213195324092.png)



- Flex 속성 : align-self:star:

  - 개별 아이템을 Cross axis 기준으로 정렬

    - 해당 속성은 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용

    ![image-20220213195410270](Web2%20-%20CSS%20Layout.assets/image-20220213195410270.png)



- Flex 속성 : align-items & **align-self**
  - Cross axis를 중심으로
    - stretch (기본 값) : 컨테이너를 가득 채움
    - flex-start : 위
    - flex-end : 아래
    - center : 가운데
    - baseline : 텍스트 baseline에 기준선을 맞춤 :star:



- Flex에 적용하는 속성
  - 기타 속성
    - flex-grow : 남은 영역을 아이템에 분배
    - order : 배치 순서



![image-20220213195613442](Web2%20-%20CSS%20Layout.assets/image-20220213195613442.png)



![image-20220213195627790](Web2%20-%20CSS%20Layout.assets/image-20220213195627790.png)





## Bootstrap



- CDN : Content Delivery(Distribution) Network
  - 컨텐츠(CSS, JS, Image, Text등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템.
  - 개발 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)
  - 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐



- spacing

  ![image-20220213205528389](Web2%20-%20CSS%20Layout.assets/image-20220213205528389.png)

  ![image-20220213205555358](Web2%20-%20CSS%20Layout.assets/image-20220213205555358.png)

  ![image-20220213205402675](Web2%20-%20CSS%20Layout.assets/image-20220213205402675.png)

  ![image-20220213205634585](Web2%20-%20CSS%20Layout.assets/image-20220213205634585.png)

  - mx-auto : 수평 중앙 정렬

    ![image-20220213205653949](Web2%20-%20CSS%20Layout.assets/image-20220213205653949.png)

    ![image-20220213205711960](Web2%20-%20CSS%20Layout.assets/image-20220213205711960.png)

  ![image-20220213205447654](Web2%20-%20CSS%20Layout.assets/image-20220213205447654.png)

  - 위의 모든 내용은 bootstrap.css에서 보다 확실하게 확인할 수 있음. +color



- Responsive Web Design

  - 다양한 화면 크기를 가진 디바이스들이 등장함에 따라 responsive web design 개념이 등장

  - 반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는 데 사용되는 용어

    예시) Media Queries, Flexbox, Bootstrap Grid System, The viewport meta tag



## Bootstrap Grid System

- Grid system (web design):star:

  - 요소들의 디자인과 배치에 도움을 주는 시스템

  - 기본 요소

    - Column : 실제 컨텐츠를 포함하는 부분
    - Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격)
    - Container : Column들을 담고 있는 공간

    

- Bootstrap Grid System:star:
  - Bootstrap Grid System은 flexbox로 제작됨
  - container, rows, column으로 컨텐츠를 배치하고 정렬
  - 반드시 기억해야 할 2가지!
    - 12개의 column
    - 6개의 grid breakpoints



- breakpoints:star:

  ![image-20220213210347679](Web2%20-%20CSS%20Layout.assets/image-20220213210347679.png)



- column

  예시)

  ```html
  <h2 class="text-center">Grid breakpoints</h2>
  <div class="row"><div class="box col-2 col-sm-8 col-md-4 col-lg-5">1</div>
    <div class="box col-8 col-sm-2 col-md-4 col-lg-2">1</div>
    <div class="box col-2 col-sm-2 col-md-4 col-lg-5">1</div> 
  </div>
  <hr>
  
  <h2 class="text-center">nesting</h2>
  <div class="row">
    <div class="box col-6">
      <div class="row">
        <div class="box col-3">1</div>
        <div class="box col-3">2</div>
        <div class="box col-3">3</div>
        <div class="box col-3">4</div>
      </div>
    </div>
    <div class="box col-6">1</div>
    <div class="box col-6">2</div>
    <div class="box col-6">3</div>
  </div>
  <hr>
  
  <h2 class="text-center">offset</h2>
  <div class="row">
    <div class="box col-md-4 offset-4">.col-md-4 .offset-4</div>
    <div class="box col-md-4 offset-md-4 offset-lg-2">.col-md-4 .offset-md-4 .offset-lg-2</div>
  </div>
  <hr>
  ```

  

> > 마무리로 하는 말:sunglasses:
> >
> > > 각각의 기술은 저마다 용도가 있고, 장단점이 있으며, 어떤 기술도 독립적인 용도를 갖추도록 설계되지는 않았다.
> > >
> > > 특정 상황에 어떤 기술이 가장 적합한 도구가 될 것인지 파악하는 데에는 많은 경험이 뒷받침되어야 한다.



## modal:star:

- 모달의 구조에 대한 이해

- 모달의 id와 #exampleModal이 일치해야 한다.

- data-bs-toggle이 있어야 한다.

  예시) 0211 실습

```html
  <!-- 01_nav_footer.html -->
  <nav class="navbar navbar-expand-md navbar-dark bg-dark sticky-top d-flex justify-content-between">
    <div class="container-fluid">
      <a href="02_home.html" class="navbar-brand">
        <img src="images/logo.png" alt="로고">
      </a>
      <div>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" 
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="02_home.html"><d>Home</d></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="03_community.html">Community</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#" data-bs-toggle="modal" data-bs-target="#exampleModal">Login</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <form>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label">Email address</label>
          <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
          <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label">Password</label>
          <input type="password" class="form-control" id="exampleInputPassword1">
        </div>
        <div class="mb-3 form-check">
          <input type="checkbox" class="form-check-input" id="exampleCheck1">
          <label class="form-check-label" for="exampleCheck1">Check me out</label>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
  </div>
</div>
```





- 모달 코드는 어디다 넣을까?
  - 모달은 position fixed, body에 쓴다.
  - body 바로 밑에 적어라. 잠재적인 다른 요소를 피하기 위해서.
  - 다른 요소랑 같이 있을 경우에는 nesting?될 수 있다.
  - Modal Body 태그 안에 넣어주세요.
  - 버튼이랑 연결 작업을 해주어야 하는데 그게 data-bs-toggle이다.
  - 만일 카드마다 눌렀을때 모달이 뜨게 하고 싶으면 카드의 버튼에 연결해줘야 한다.
  - 모달은 카드 내부에 넣는 게 아니라 바디 태그 안에 넣는다.
  - 아이디와 data-bs-target=#productModal 일치시킬것
  - data-bs-target = "modal" 추가하기

  - form을 넣는다거나 할 수 있다.
- 적절한 곳에 붙여넣는게 중요하다.



- bootstrap cheatsheet (https://getbootstrap.com/docs/5.1/examples/#framework)

- Modals example (https://getbootstrap.com/docs/5.1/examples/modals/)