# ThemeProvider



styled-component에서 ThemeProvider import 하기

```react
import {ThemeProvider} from "styled-components";
```



ThemeProvider 컴포넌트를 GlobalStyle보다 위에 상위 컴포넌트로 넣기



theme이라는 이름을 가진 비어있는 객체를 만든다.

```react
const theme = {}
```



생성한 객체를 ThemeProvider의 props로 넣어준다.

```react
<ThemeProvider theme={theme}/>
```

여기까지의 과정을 통해 styled-component가 모든 컴포넌트에 theme 변수를 inject 해주게 된다.



