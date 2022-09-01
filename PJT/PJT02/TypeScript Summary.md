# TypeScript Summary



## TypeScript란?

자바스크립트 문법을 그대로 이용가능한데, type 부분을 조금 업그레이드해서 쓸 수 있는 *업그레이드 자바스크립트* 같은 언어이다.

타입을 체크하기 때문에 에러메세지가 정확한 장점이 있다.

```json
// tsconfig.json

{   
  "compilerOptions" : {     
    "target": "es5",     
    "module": "commonjs",  
  } 
}
```

터미널 켜서 `tsc -w` 입력하고 실행시켜두면 `TS` >> `JS`로 자동변환된다.



## 문법 요약

### 간단한 변수 타입 지정

```tsx
let 이름 :string = 'kim';
// 앞으로 이름 변수에는 무조건 문자열만 들어갈 수 있음.
// 숫자를 할당하면 버그 발생
```

- string
- number
- boolean
- null
- undefined
- bigint
- []
- {}
- 등등...

```tsx
let 이름 :string[] = ['kim', 'park']
// 변수 타입 + array : 문자열 배열만 들어올 수 있음.
let 이름 :{ name? : string } = { name : 'kim'}
// {} object도 마찬가지.
// ?치면 옵션값으로 설정됨. (맞아도 안 맞아도 그만)
let 이름 :string | number = 'kim';
// Union type : 둘 다 가능
```



### 변수에 담아쓰기 : Type alias

```tsx
// 변수 만들기
type 내타입 = string | number;
// 타입명은 보통 영어 대문자로 작문함
```



### 함수에 타입지정 가능

```tsx
function 함수(x : number) :number {
    return x*2
}
// 들어오는 것도 문자, 나가는 것도 문자여야 하는 함수
```



### array에 쓸 수 있는 tuple 타입

```tsx
type Member = [number, boolean];
let joHn:Member = []
// 무조건 첫째는 number, 둘째는 boolean이 된다.
```



### object에 타입을 지정해야할 속성이 너무 많다면

```tsx
type Member = {
    [key :string] : string
    // 글자로 된 모든 object 속성의 타입은 :string
}
let john : Member
// 앞으로는 john에는 {name : string}만 들어갈 수 있다.
```



### class 타입 지정가능

```tsx
class User {
    name: string;
    constructor(name :string){
        this.name = name;
    }
}
```

