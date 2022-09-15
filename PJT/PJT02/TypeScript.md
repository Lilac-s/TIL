# TypeScript



## TypeScript

타입스크립트는 자바스크립트의 "슈퍼셋(superset)" 언어이다.

자바스크립트를 기반으로 하되, 더 확장된 언어이다.

자바스크립트의 기본 문법, 코드 작성법, 객체 사용법 등을 그대로 사용한다.



타입스크립트는 **정적 타입(static Typed)**의 특징을 갖는다.

자바스크립트는 반대로 동적 타입 언어이다.



## 설치하기

[typescript](https://www.typescriptlang.org/)

`npm install typescript`

`npm install -g typescript`



브라우저에서 ts를 읽지 못하므로 js로 컴파일해야 한다.

구성 파일을 지정한 후

`npx tsc`

컴파일 단계에 오류가 있더라도 컴파일 자체는 가능하다.

에러 메세지는 보여준다.



## 기본 자료형(Type)

- Primitives : number, string, boolean
- More complex types : arrays, objects
- Function types, parameters

**타입은 소문자로 적어야 한다**

```tsx
let age: number;
age = 12;

let userName: string;
userName = 'Max';

let isInstructor: boolean;
isInstructor = true;
```



## 배열과 객체

```tsx
let hobbies: string[];
hobbies = ['Sports', 'Cooking', '12']

let person: {
    name: string;
    age: number;
};
person = {
    name: 'Max',
    age: 32
};

let peolpe: {
    name: string;
    age: number;
}[];
```

- 아무것도 명시해주지 않으면 기본 타입은 `any`로 지정된다.
  - 예비적으로 사용하는 것이므로 사용하지 않는 것이 좋다.
  - 자바스크립트를 쓰는 것과 다를 바 없다.



## 타입 추론(type inference)

```tsx
let course = 'React'
course = 12341;
// 이렇게 하면 타입 추론이 일어나서 12341; 부분에서 에러가 발생한다.
// 타입스크립트가 처음에 받은 타입을 추론해서 지정한 것이다.
```

매번 :type을 지정해 주는 것보다, 타입 추론을 통해서 지정되게 하는 것이 권장되는 방법이다.

매번 지정해 주는 것은 불필요한 작업이므로 지양하는 것이 좋다.



## 유니온(union) 유형

- 유니온 타입
  - 타입을 정의할 때 한 개 이상의 타입을 사용할 수 있도록 하는 기능

```tsx
let course: string | number | boolean = 'React'
course = 12341;

let userName: string | string[];
userName = 'Max';
```

결과 타입을 유연하게 적용할 수 있도록 해준다.



## 타입 별칭(Type Aliases)

직접 기본(Base) 타입을 만들어서 거기에 복잡한 타입을 정의해 두고 재사용하는 방식

반복해서 타입을 정의하지 않을 수 있다.

Type Aliases는 TS의 고유 기능이기 때문에 JS로 컴파일하면 코드에서 사라지게 된다.

```tsx
type Person = {
    name: string;
    age: number;
};

let person: Person;
let people: Person[];
```

- `type` 키워드
  - `type` 뒤에 원하는 이름을 붙이면 그게 새로운 타입의 이름이 된다.



## Functions & types

```tsx
function add(a: number, b: number) {
    return a + b;
}
// 타입스크립트는 함수가 반환하는 값을 통해 타입 추론을 할 수 있다.
// 따라서 위의 코드는 아래와 같은 의미를 가진다.
function add(a: number, b: number): number {
    return a + b;
}
// 결과값도 숫자형일것이라고 지정한 것이다.

function printOutput(value: any) {
    console.log(value)
}
// 위의 함수는 아무것도 리턴하지 않는다.
// 이 경우에는 'void'타입을 반환한다.
// 이 함수의 반환값을 사용하고자 한다면 undefined로 지정해줘야 한다.
```

- `void`
  - 아무것도 리턴하지 않을 경우에 반환되는 타입
  - 반드시 함수와 결합해서 사용한다.



## 제네릭(Generics)

[공식문서 - Generics](https://www.typescriptlang.org/ko/docs/handbook/2/generics.html)

> 공식문서에 나오는 `interface` 와 `type`의 차이
>
> [타입스크립트 type과 interface의 공통점과 차이점](https://yceffort.kr/2021/03/typescript-interface-vs-type)
>
> 둘의 확장에 대해서도 기술되어있다.
>
> 프로젝트를 진행할 때 둘 중 하나로의 협의가 필요하다.

