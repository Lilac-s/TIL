# 0511_homework



1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- Vue 프로젝트에서 상태 관리를 하기 위해서는 반드시 Vuex를 설치해야 한다.
  - F
- mutations는 반드시 state를 수정하기 위해서만 사용되어야 한다.
  - T
- mutations는 store.dispatch로, actions는 store.commit으로 호출할 수 있다.
  - F
- state는 data의 역할, getters는 computed와 유사한 역할을 담당한다.
  - T





2. Vuex에서 State, Getters, Mutations, Actions의 역할을 각각 서술하시오.

- Vuex State

  - state는 일종의 상태들을 모아놓은 저장소를 말한다. 실제로 각각의 컴포넌트에서 필요로 하는 공통된 데이터는 state에 표시하면 된다. 
  - state는 곧 data이며 해당 어플리케이션의 핵심이 되는 요소이다.
  - 중앙에서 관리하는 모든 상태 정보를 뜻한다.
    - Vuex는 single state tree를 사용
    - 즉, 이 단일 객체는 모든 애플리케이션 상태를 포함하는 원본 소스(single source of truth)의 역할을 함
    - 이는 각 애플리케이션마다 하나의 저장소만 갖게 된다는 것을 의미한다.
  - 여러 컴포넌트 내부에 있는 특정 state를 중앙에서 관리하게 된다.
    - 이전의 방식은 state를 찾기 위해 각 컴포넌트를 직접 관리해야 했다.
    - Vuex를 활용하는 방식은 Vuex Store에서 각 컴포넌트에서 사용하는 state를 한 눈에 파악 가능하다.
  - State가 변화하면 해당 state를 공유하는 여러 컴포넌트의 DOM은 알아서 렌더링된다.
  - 각 컴포넌트는 이제 Vuex Store에서 state정보를 가져와서 사용한다.

  

- Vuex getters

  - store 객체의 computed 속성과 비슷한 의미이다. 

  - compute를 사용하는 것처럼 getters는 저장소의 상태(state)를 기준으로 계산한다.

  - computed 속성과 마찬가지로 getters의 결과는 state 종속성에 다라 캐시(cached)되고, 종속성이 변경된 경우에만 다시 재계산 된다.

  - getters 자체가 state를 변경하지는 않는다.

    - state를 특정한 조건에 따라 계산만 하고, 계산된 값을 가져온다.

    

- Vuex Mutations

  - 실제로 state를 변경하는 유일한 방법이다.
  - mutation의 handler는 반드시 동기적이어야 한다.
    - 비동기적 로직은 state가 변화하는 시점이 의도한 것과 달라질 수 있으며, 콜백이 실제로 호출 될 시기를 알 수 있는 방법이 없다.(추적할 수 없다)
  - 첫 번째 인자로 항상 state를 받는다.
  - Actions에서 commit() 메서드에 의해 호출된다.

  

- Vuex Actions

  - Mutations와 유사하지만 다음과 같은 차이점이 있다.

    1. state를 변경하는 대신 mutations를 commit()메서드로 호출해서 실행한다.
    2. mutation과 달리 비동기 작업이 포함될 수 있다.

  - context 객체 인자를 받는다.

    - context객체를 통해 store/index.js 파일 내에 있는 모든 요소의 속성을 접근하고 메서드 호출이 가능하다.
    - 단, state를 직접 변경하지는 않는다.
    - 명확한 역할 분담을 통해 서비스 규모가 커져도 state를 올바르게 관리하기 위함이다.

  - 컴포넌트에서 dispatch() 메서드에 의해 호출된다.

    





3. 컴포넌트에 작성된 Todo App 관련 코드를 Vuex의 Store로 옮기고자 한다.  빈 칸 (a), (b), (c), (d)에 들어갈 코드를 작성하시오.

(a) : `state`

(b) : `getters`

(c) : `mutations`

(d) : `state`