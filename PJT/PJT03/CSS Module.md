# CSS Module

Sass에서 size props를 설정하기 위해서  `classnames`를 사용하여 프로필 이미지 컴포넌트를 작업하고 있었다.

하지만 classnames가 원하는 대로 작동하지 않았다.

[참고링크](https://agal.tistory.com/144)

css module을 사용하기 때문에 styles 또는 classes로 id를 가져오게 되는데,

이 때 className안에 bind를 제대로 해주지 못하는 문제였다.

CSS module에서 classnames를 어떻게 사용하는지 찾아보다가, 아래 링크를 보고 해결했다.

[벨로퍼트와 함께하는 모던 리액트 2장.래익트 컴포넌트 스타일링하기 2.CSS Module](https://react.vlpt.us/styling/02-css-module.html)

classnames의 `bind` 기능을 사용해서, 클래스 이름을 지정해 줄 수 있다.

이 때, classNames를 import 할 때 반드시 `classnames/bind`에서 import해와야 한다.

아래는 예시로 작성한 코드이다.

```js
import styles from "./ProfileImage.module.scss";
import classNames from "classnames/bind";


const ProfileImage = (props) => {
  const cx = classNames.bind(styles);

  return (
    <div className={cx('img_container', 'small')}>
      <img src={props.url}
      className={styles.profile_img}
      />
    </div>
  )
}

export default ProfileImage;
```

```scss
.img_container{
  width: 150px;
  height: 150px;
  border-radius: 70%;
  overflow: hidden;
  &.small {
    width: 100px;
    height: 100px;
  }
}

.profile_img{
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

위와 같은 코드로 프로필 이미지 컴포넌트를 만드는 데에 성공했다.