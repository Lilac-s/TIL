# 0512_homework



1.  다음은 Vuex로 구성된 하나의 숫자를 counting하는 store이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

(a) : `Vuex.Store`

(b) : `state.count += 1`

(c) : `context.commit("NUMBER_INCREAMENT")`



2. 아래 예시의 함수는 서버로부터 데이터를 가져 온 뒤,  응답 값을 state에 저장하기 위하여 mutations를 호출하는 로직을 수행한다. 이와 같이 비동기 API 및 mutations 호출에 적합한 store의 속성 (a)를 작성하시오.

(a) : `actions`



3. 왼쪽처럼 store에 state, getters, actions가 정의되어 있다. “Component Binding Helpers”를 통해 각 컴포넌트에서 사용하고자 한다. Vuex 공식문서를 참고하여 빈 칸 (a), (b), (c), (d), (e)에 들어갈 코드를 작성하시오.

(a) : `{mapstate, mapgetters, mapactions}`

(b) : `Vuex.Store`

(c) : `mapstate`

(d) : `mapgetters`

(e) : `...mapactions`



4. store에 정의한 state를 직접 변경하지 않고, mutations를 통해 변경해야 하는 이유를 Vuex 공식문서를 참고하여 작성하시오.

- 데이터의 흐름을 체크하기 위함이다.
- 상태를 검색할 때 저장소의 상태가 변경되면 반응적이고 효율적으로 업데이트 할 수 있도록 한다.
- 상태를 직접 변경할 수 없고, mutation을 통해 변경을 커밋한다. 이 방법을 사용하면 모든 상태 변경이 추적 가능한 기록을 남기므로 개발 과정을 더 잘 이해할 수 있게 된다.

> [참고링크](https://vuex.vuejs.org/guide/)