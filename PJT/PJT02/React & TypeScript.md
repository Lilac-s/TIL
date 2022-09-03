# React & TypeScript



## 환경설정

- CRA 사용하기

  - [create-react-app Adding TypeScript](https://create-react-app.dev/docs/adding-typescript/)

  - `푸르게` 프로젝트에서는 개발환경을 직접 설정한다. ~~bye~~

- 프로젝트를 만들 때 타입스크립트 기반 프로젝트로 만들기
  - `npx create-react-app --template typescript`



이렇게 프로젝트를 만들면 `src` 디렉토리 안에 `js` 파일 대신 `tsx` 파일들이 생성된다.



## Props 및 TypeScript 작업하기

```tsx
// src/components/Todos.tsx

import React from 'react';

const Todos: React.FC<{ items: string[] }> = (props) => {
    return (
    	<ul>
        	{props.items.map((item) => (
            	<li key={item}>{item}</li>
            ))}
        </ul>
    );
};

export default Todos;
```



```tsx
// src/App.tsx

import Todos from './components/Todos';

function App() {
    return (
    	<div>
        	<Todos items={['Learn React', 'Learn TypeScript']}/>
        </div>
    )
}
```



## 데이터 모델 추가하기

