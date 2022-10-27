# OptionCard



```js
import styles from "./OptionCard.module.scss";
import classNames from "classnames/bind";
import Image from "next/image";

//* 커스텀 페이지에서 종류를 고를 때 사용하는 카드입니다.
//* props로 size(small, medium), img, title, content 값을 받습니다.
const OptionCard = (props) => {
  const cx = classNames.bind(styles);
  return (
    <div className={cx("custom_div", props.size)}>
      <Image src={props.img} className={styles.custom_img} width={180} height={180} />
      <p>{props.title}</p>
      <div className={styles.card_line}></div>
      <span>{props.content}</span>
    </div>
  );
};

export default OptionCard;
```

```scss
@mixin hoverButton {
  transition: all 0.5s linear;
  cursor: pointer;
  &:hover {
    transform: scale(1.01);
  }
  &:hover::after {
    top: 0;
    height: 100%;
  }
  &:active {
    top: 0.125px;
  }
  &:after {
    position: absolute;
    content: "";
    width: 100%;
    height: 0;
    bottom: 0;
    left: 0;
    z-index: -1;
    border-radius: 0.3rem;
    background-color: $gradient;
    background-image: $gradient;
    opacity: 0.3;
    box-shadow: -7px -7px 20px 0px #fff9, -4px -4px 5px 0px #fff9, 7px 7px 20px 0px #0002, 4px 4px 5px 0px #0001;
    transition: all 0.5s ease;
  }
}

.custom_div {
  @include flexDiv(column, center, center);
  box-shadow: $shadow700;
  border-radius: 0.25rem;
  background-color: $white;
  color: $mainParagraph;
  padding: 2rem 0.6rem 2rem 0.6rem;
  gap: 0.25rem;
  white-space: pre-line;
  text-align: center;
  &.small {
    @include hoverButton();
    width: 11.25rem;
    height: 20rem;
    & > p {
      @include font(1.5rem);
    }
    & > span {
      @include font;
      color: $gray;
      word-break: keep-all;
    }
  }
  &.medium {
    @include hoverButton();
    width: 15rem;
    height: 22rem;
    & > p {
      @include font(1.5rem);
    }
    & > span {
      @include font;
      word-break: keep-all;
    }
  }
}

.custom_img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.card_line {
  width: 60%;
  border: 0.05rem solid $primary300p;
  margin-bottom: 0.5rem;
}
```

