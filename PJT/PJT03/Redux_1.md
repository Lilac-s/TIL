# Redux_1

## Action

상태에 변화가 필요할 때 발생시키는 `액션`

```react
{
    type: "TOGGLE_VALUE"
}
```

액션 객체는 `type` 필드를 필수적으로 가지고 있어야 한다.

```react
{
    type: "ADD_TODO",
    data: {
        id: 0,
        text: "리덕스 배우기"
    }
}
```

그 외의 값들은 개발자가 자유롭게 넣어줄 수 있다.



## Action Creator

액션을 만드는 함수 `액션 생성함수`

```react
export const changeInput = text => ({
    type: "CHANGE_INPUT",
    text
});
```

파라미터를 받아와서 액션 객체 형태로 만들어 준다. 컴포넌트에서 보다 쉽게 액션을 발생시키기 위해 사용한다.



## Reducer

변화를 일으키는 함수 `리듀서`

```react
function reducer(state, action) {
  // 상태 업데이트 로직
  return alteredState;
}
```

`state`, `action` 의 두 가지 파라미터를 받아온다.

현재의 상태 `state `와 전달 받은 액션 `action` 을 참고하여 새로운 상태를 만들어서 반환한다.

`useReducer` 를 사용할 때 작성하는 리듀서와 똑같은 형태를 가지고 있다.

```react
// 카운터를 위한 리듀서 예제
function counter(state, action) {
  switch (action.type) {
    case 'INCREASE':
      return state + 1;
    case 'DECREASE':
      return state - 1;
    default:
      return state;
  }
}
```



## Store

한 애플리케이션당 하나의 `스토어` 를 가지고 있다.

스토어 안에는 현재의 앱 상태 `state` 와, 리듀서 `reducer`, 그리고 추가적인 몇 가지 내장 함수들이 있다.



## dispatch

스토어의 내장함수 중 하나인 `디스패치`

액션을 파라미터로 전달해서 액션을 발생시킨다.



## subscribe

스토어의 내장함수 중 하나인 `구독`

함수 형태의 값을 파라미터로 받아온다. subscribe 함수에 특정 함수를 전달해주면, 액션이 dispatch 되었을 때 마다 전달해준 함수가 호출된다.