# SCSS에 전역변수 설정하기

styled-component를 사용해오다가,
Next.js는 SCSS와 함께 쓰는 것이 성능 면에서 도움이 된다는 글을 읽게 되었다.

[CSS in JS](https://fe-developers.kakaoent.com/2022/220210-css-in-kakaowebtoon/)

오늘 처리해야 하는 지라 이슈로 theme설정이 있었는데,
SCSS에서는 어떻게 설정해야 하는지 공부하며 함께 적용해 보았다.
애쓴 시간에 비해서 굉장히 간단하다.

## 1. 파일 만들고 변수 설정하기

styles 폴더 안에 파일을 만들고 변수를 설정해준다.
이 때, 전역으로 사용하는 파일명은 아래와 같이 설정해주어야 한다.

`_variables.module.scss` : 변수가 들어가는 파일
`_mixins.module.scss` : mixin이 들어가는 파일

css module을 함께 사용하기 때문에 `.module`로 만들어 주었다.

```scss
// styles/_variables.module.scss
// color
// Main 컬러
$mainParagraph: #2a2a2a;
$mainPrimary: #96c62b;
$mainDanger: #ff5955;
$mainButton: #323232;
$mainModalBg: rgba(50, 50, 50, 0.3);
$mainWhite: #fcfcfc;

$transparent: transparent;

// gradient
$gradient: linear-gradient(350deg, #ff8fa4, #ffb4b0, #ffd9bb, #fffbc6);
$deepGradient: linear-gradient(350deg, #ffb800, #f4a39e, #f37f8b, #de6279);
$lightGradient: linear-gradient(350deg, #ffd8e0, #ffe8e7, #ffebdc, #fffffe);

// 너닮꽃 Primary
$primary300: #f7ffe5;
$primary400: #ecffc1;
$primary500: #ddff92;
$primary600: #beeb58;
$primary700: #96c62b;
$primary800: #6d921c;
$primary900: #445b0f;
$primary600p: #647838;
$primary500p: #93a669;
$primary400p: #c5dc90;
$primary300p: #d4dac6;

// 너닮꽃 White
$white: #ffffff;
$white100: #fcfcfc;
$white150: #f5f5f5;
$white200: #efefef;
$white250: #e8e8e8;
$white300: #dfdfdf;
$white350: #c8c8c8;
$white400: #b7b7b7;

// 너닮꽃 Gray
$gray: #949494;
$gray100: #777777;
$gray150: #616161;
$gray200: #555555;
$gray250: #3f3f3f;
$gray300: #323232;
$gray350: #2a2a2a;
$gray400: #1f1f1f;

// 너닮꽃 Black
$black100: #1a1a1a;
$black200: #111111;
$black: #000000;

// 너닮꽃 Red
$red300: #fee2e2;
$red400: #ffa7a5;
$red500: #ff908e;
$red600: #ff5955;
$red700: #d10500;
$red800: #9a0d0a;
$red900: #6c1e1d;
$red600p: #c93f3c;
$red500p: #de605d;
$red400p: #e79391;
$red300p: #eacdcc;

// 너닮꽃 ivory
$ivory300: #fffbeb;
$ivory400: #fdf5d6;
$ivory500: #f3dd8a;
$ivory600: #f6d55a;
$ivory700: #f5cc35;
$ivory800: #c99d00;
$ivory900: #907100;
$ivory600p: #71612a;
$ivory500p: #978c62;
$ivory400p: #cfc18d;
$ivory300p: #dbd6c5;

// shadow
$shadow700: 0px 100px 80px rgba(0, 0, 0, 0.07), 0px 41.78px 33.4px rgba(0, 0, 0, 0.0503),
  0px 22.34px 17.87px rgba(0, 0, 0, 0.0417), 0px 12.52px 10.02px rgba(0, 0, 0, 0.035),
  0px 6.65px 5.32px rgba(0, 0, 0, 0.0283), 0px 2.77px 2.21px rgba(0, 0, 0, 0.0197);
$shadow600: 0px 20px 80px rgba(0, 0, 0, 0.07), 0px 12.52px 10.02px rgba(0, 0, 0, 0.035),
  0px 2.77px 2.21px rgba(0, 0, 0, 0.0197);
$shadow500: 0px 0px 8px rgba(0, 0, 0, 0.1);
$shadow400: 0px 0px 4px rgba(0, 0, 0, 0.1);
```

```scss
// styles/_mixins.module.scss
// font
//* 인수를 넘기지 않으면 기본값으로 설정됩니다.
//TODO @include 이름(인수) 형식으로 사용
@mixin font($size: 1rem, $weight: 500, $color: #2a2a2a) {
  font-size: $size;
  font-weight: $weight;
  color: $color;
}

// flexdiv
//* 인수를 넘기지 않으면 기본값으로 설정됩니다.
//TODO 스타일을 추가해서 사용 가능
@mixin flexDiv($direction: row, $align: center, $justify: center) {
  display: flex;
  flex-direction: $direction;
  align-items: $align;
  justify-content: $justify;
  @content;
}

// grid
//* 인수를 넘기지 않으면 기본값으로 설정됩니다.
@mixin grid($columns: 25%, $rows: 25%) {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax($columns, auto));
  grid-template-rows: repeat(auto-fill, minmax($rows, auto));
  justify-items: center;
  justify-content: center;
  align-items: center;
  align-content: center;
}
```



## 2. config.js 수정

```js
// next.config.js
/** @type {import('next').NextConfig} */
const path = require("path");

module.exports = {
  reactStrictMode: true,
  swcMinify: true,
  sassOptions: {
    includePaths: [path.join(__dirname, "styles")],
    prependData: `@import "styles/_variables.module.scss"; @import "styles/_mixins.module.scss";`, // prependData 옵션 추가
  },
};
```

prependData: `@import "styles/_variables.module.scss"; @import "styles/_mixins.module.scss";`, // prependData 옵션 추가

위의 한 줄을 추가해 주었다.



## 3. 사용

```scss
// pages/custom/index.module.scss
.testbox {
  @include font(3rem, 700, $ivory500);
  @include flexDiv;
}
```

이제 위와 같은 형식으로 import 하지 않고도 변수와 mixins을 사용할 수 있다.