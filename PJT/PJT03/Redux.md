# Redux

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



---



## Setting

```react
// store/index.js
import { configureStore } from "@reduxjs/toolkit";
import { createWrapper } from "next-redux-wrapper";
import rootReducer from "./reducers";
import { chatMiddleware } from "./middleware/chatMiddleware";

import {
  persistStore,
  persistReducer,
  FLUSH,
  REHYDRATE,
  PAUSE,
  PERSIST,
  PURGE,
  REGISTER,
} from "redux-persist";
import storageSession from "redux-persist/lib/storage/session";

// * session storage
const persistConfig = {
  key: "root",
  storage: storageSession,
  version: 1,
  whitelist: ["custom"],
};

const persistedReducer = persistReducer(persistConfig, rootReducer);

export const store = configureStore({
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false,
    }).concat(chatMiddleware),
  devTools: false,
});

const setUpStore = (context) => store;
const makeStore = (context) => setUpStore(context);

export const persistor = persistStore(store);

export const wrapper = createWrapper(makeStore);
```



```react
// store/reducers/custom.js
import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  package: null,
  size: null,
  wrapper_color: null,
  ribbon_color: null,
  flowers: null,
  current_flower: null,
  current_location: null,
};

const customSlice = createSlice({
  name: "custom",
  initialState,
  reducers: {
    selectPackage: (state, action) => {
      return { ...state, package: action.payload };
    },
    selectSize: (state, action) => {
      return { ...state, size: action.payload };
    },
    makeFlowerList: (state, action) => {
      return { ...state, flowers: action.payload };
    },
    makeCurrentFlower: (state, action) => {
      return { ...state, current_flower: action.payload };
    },
    makeCurrentLocation: (state, action) => {
      return { ...state, current_location: action.payload };
    },
    selectWrapperColor: (state, action) => {
      return { ...state, wrapper_color: action.payload };
    },
    selectRibbonColor: (state, action) => {
      return { ...state, ribbon_color: action.payload };
    },
  },
});

export default customSlice;
export const {
  selectPackage,
  selectSize,
  makeFlowerList,
  makeCurrentFlower,
  makeCurrentLocation,
  selectWrapperColor,
  selectRibbonColor,
} = customSlice.actions;

```

