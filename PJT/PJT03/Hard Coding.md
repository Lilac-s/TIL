# Hard Coding

다시는 이렇게 긴 코드를 쓰는 하드코딩을 하고 싶지 않았는데
꽃을 예쁘게 배치하는 걸 어떻게 계산해서 코드를 써야 할지 아직은 떠오르지 않는다.

많은 내용을 코딩하면서 코드가 원치 않는 방향으로 복잡해질 때 마다
이게 나만의 코드가 아니라 팀원 모두의 코드라는 생각이 들면서 마음도 함께 복잡해진다.

앞으로 남은 기간 동안 어떻게 개선할 수 있을지 계속 생각하면서 개발해야겠다.



```scss
.circle_wrapper {
  position: relative;
  &.xs {
    height: 57%;
    &.ballon {
      height: 40%;
      & > div {
        width: 7rem;
        height: 7rem;
        transform: rotate(0deg);
      }
    }
    &.vase {
      height: 80%;
      left: -0.4rem;
      & > div {
        height: 6.5rem;
        width: 6.5rem;
        transform: rotate(6deg);
      }
    }
  }
  &.s {
    height: 75%;
    &.ballon {
      height: 65%;
      & > div {
        width: 6rem;
        height: 6rem;
      }
    }
    &.vase {
      height: 100%;
      & > div {
        height: 6.5rem;
        width: 6.5rem;
      }
    }
  }
  &.m {
    height: 36%;
    &.ballon {
      left: -0.5rem;
      height: 32%;
      & > div {
        width: 6rem;
        height: 6rem;
      }
    }
    &.vase {
      left: -0.7rem;
      height: 75%;
      & > div {
        width: 6rem;
        height: 6rem;
      }
    }
  }
  &.l {
    height: 36%;
  }
  &.xl {
    left: -0rem;
    height: 30%;
  }
}

.circle_1 {
  position: relative;
  background-color: $white 0.3;
  border-radius: 100rem;
  z-index: 10;
  left: 0.5rem;
  &.xs {
    left: 1rem;
    width: 8rem;
    height: 8rem;
    transform: rotate(8deg);
  }
  &.s {
    left: 0.5rem;
    top: 5rem;
    width: 8rem;
    height: 8rem;
  }
  &.m {
    left: 1rem;
    width: 7.5rem;
    height: 7.5rem;
  }
  &.l {
    left: 0.5rem;
    width: 7rem;
    height: 7rem;
  }
  &.xl {
    left: 1rem;
    width: 6rem;
    height: 6rem;
  }
}

.circle_2 {
  position: relative;
  background-color: $white 0.3;
  border-radius: 100rem;
  z-index: 9;
  &.s {
    top: -5rem;
    left: 3rem;
    width: 8rem;
    height: 8rem;
    transform: rotate(20deg);
    &.ballon {
      left: 2.5rem;
      top: -2rem;
      transform: rotate(35deg);
    }
    &.vase {
      top: -2rem;
      left: 2rem;
      transform: rotate(35deg);
    }
  }
  &.m {
    top: -9.5rem;
    left: 3.5rem;
    width: 7.3rem;
    height: 7.3rem;
    transform: rotate(30deg);
    &.ballon {
      left: 3rem;
      top: -6rem;
      transform: rotate(35deg);
    }
    &.vase {
      top: -6rem;
      left: 2.5rem;
      transform: rotate(35deg);
    }
  }
  &.l {
    top: -8.5rem;
    left: 3rem;
    width: 6.5rem;
    height: 6.5rem;
    transform: rotate(30deg);
  }
  &.xl {
    top: -8rem;
    left: 3.5rem;
    width: 6rem;
    height: 6rem;
    transform: rotate(30deg);
  }
}

.circle_3 {
  position: relative;
  background-color: $white 0.3;
  border-radius: 100rem;
  z-index: 8;
  &.s {
    top: -14rem;
    left: -1.5rem;
    width: 8rem;
    height: 8rem;
    transform: rotate(-20deg);
    &.ballon {
      left: -2rem;
      top: -9rem;
      transform: rotate(-20deg) scaleX(-1);
    }
    &.vase {
      left: -1.5rem;
      top: -9rem;
      transform: rotate(-30deg) scaleX(-1);
    }
  }
  &.m {
    top: -17rem;
    left: -1.5rem;
    width: 7.3rem;
    height: 7.3rem;
    transform: rotate(-20deg);
    &.ballon {
      top: -12rem;
      left: -2rem;
      transform: rotate(-35deg) scaleX(-1);
    }
    &.vase {
      top: -12rem;
      left: -1.5rem;
      transform: rotate(-30deg) scaleX(-1);
    }
  }
  &.l {
    top: -15rem;
    left: -1.5rem;
    width: 6.5rem;
    height: 6.5rem;
    transform: rotate(-20deg);
  }
  &.xl {
    top: -13rem;
    left: -2rem;
    width: 6rem;
    height: 6rem;
    transform: rotate(-30deg) scaleX(-1);
  }
}

.circle_4 {
  position: relative;
  background-color: $white 0.3;
  border-radius: 100rem;
  z-index: 7;
  &.m {
    top: -27.3rem;
    left: 3rem;
    width: 7rem;
    height: 7rem;
    transform: rotate(30deg);
    &.ballon {
      top: -20.5rem;
      left: -1rem;
      transform: rotate(-20deg) scaleX(-1);
    }
    &.vase {
      top: -20.5rem;
      left: -1rem;
      transform: rotate(-20deg) scaleX(-1);
    }
  }
  &.l {
    top: -23.5rem;
    left: 1rem;
    width: 6.3rem;
    height: 6.3rem;
    transform: rotate(10deg);
  }
  &.xl {
    top: -22rem;
    left: 5rem;
    width: 5.5rem;
    height: 5.5rem;
    transform: rotate(40deg);
  }
}

.circle_5 {
  position: relative;
  background-color: $white 0.3;
  border-radius: 100rem;
  z-index: 6;
  &.m {
    top: -34rem;
    left: -1rem;
    width: 7rem;
    height: 7rem;
    transform: rotate(-20deg);
    &.ballon {
      left: 2.5rem;
      top: -26.5rem;
      transform: rotate(35deg);
    }
    &.vase {
      left: 2.5rem;
      top: -26.5rem;
      transform: rotate(35deg);
    }
  }
  &.l {
    top: -30rem;
    left: 4.5rem;
    width: 6rem;
    height: 6rem;
    transform: rotate(20deg);
  }
  &.xl {
    top: -26.5rem;
    left: 1rem;
    width: 6rem;
    height: 6rem;
  }
}

.circle_6 {
  position: relative;
  background-color: $white 0.3;
  border-radius: 100rem;
  z-index: 5;
  &.l {
    top: -38.5rem;
    left: 1rem;
    width: 6rem;
    height: 6rem;
  }
  &.xl {
    top: -33rem;
    left: -3rem;
    width: 6rem;
    height: 6rem;
    transform: rotate(-30deg) scaleX(-1);
  }
}

.circle_7 {
  position: relative;
  background-color: $white 0.3;
  border-radius: 100rem;
  z-index: 4;
  &.l {
    top: -42.3rem;
    left: -2.3rem;
    width: 6rem;
    height: 6rem;
    transform: rotate(-20deg);
  }
  &.xl {
    top: -40.5rem;
    left: -1rem;
    width: 5.5rem;
    height: 5.5rem;
    transform: rotate(-10deg) scaleX(-1);
  }
}

.circle_8 {
  position: relative;
  background-color: $white 0.3;
  border-radius: 100rem;
  z-index: 3;
  &.xl {
    top: -46rem;
    left: 2.5rem;
    width: 5.5rem;
    height: 5.5rem;
    transform: rotate(20deg);
  }
}

.circle_9 {
  position: relative;
  background-color: $white 0.3;
  border-radius: 100rem;
  z-index: 2;
  &.xl {
    top: -53.5rem;
    left: 1rem;
    width: 5.5rem;
    height: 5.5rem;
  }
}
```

