# HoverButton



```scss
.main_bouquet {
  height: 18rem;
  width: 18rem;
  opacity: 0.8;
  transition: all 0.5s linear;
  &:hover {
    transform: scale(1.02);
    opacity: 1;
  }
  & > button {
    transition: all 0.5s linear;
  }
}

.arrow_box {
  visibility: hidden;
  position: absolute;
  top: 7rem;
  left: 4rem;
  width: 10rem;
  padding: 1rem;
  border-radius: 5rem;
  background-color: rgba(255, 255, 255, 0.6);
  box-shadow: $shadow400;
  @include font(1rem, 600, $primary900);
  text-align: center;
  opacity: 0;
  &:hover {
    visibility: visible;
    opacity: 1;
    cursor: pointer;
  }
}

div:hover + button.arrow_box {
  visibility: visible;
  opacity: 1;
}

```

