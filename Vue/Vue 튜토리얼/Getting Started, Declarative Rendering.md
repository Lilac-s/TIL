# Vue 튜토리얼 해보기



## Getting Started

- 전제 조건
  - HTML, CSS, JavaScript에 대한 기본적인 지식
- 사용 방법
  - 각 단계에서 코드를 완성한다.
  - 막히면 "Show me!"가 표시된다.
  - 끝내고 나서 가이드도 읽기!



## Declarative Rendering (선언적 렌더링)

- using a template syntax that extends HTML, we can describe how the HTML should look like based on JavaScript state. When the state changes, the HTML updates automatically.

- State that can trigger updates when changed are considered **reactive**. In Vue, reactive state is held in components.

  > 컴포넌트 : 하나의 화면을 적절하게 분리하여 블록화 하고, 여기서 하나하나의 블록이 컴포넌트이다. 공식 문서에서는 "코드의 캡슐화"라고 부른다. 프로그래밍을 할 때, 비동기적으로 따로따로 움직여야 하는 부분들을 컴포넌트로 나누곤 했다.

- We can declare reactive state using the `data` component option, which should be a function that returns an objcet

- The `message` property will be made available in the template. This is how we can render dynamic text based on the value of `message`, use mustaches syntax

  > `export default {}`안에 컴포넌트 옵션이 들어간다.
  >
  > 필요하다면 message에 `split`등을 쓸 수 있다.
  >
  > 예시) `<h1>{{ message.split('').reverse().join('') }}</h1>`

  ```vue
  <script>
  export default {
    data() {
      return {
        message: 'Hello World!',
        counter: {
          count: 0
        }
      }
    }
  }
  </script>
  
  <template>
    <h1>{{ message }}</h1>
    <p>Count is: {{ counter.count }}</p>
  </template>
  ```

  