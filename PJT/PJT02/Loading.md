# Loading



```react
import { StyledDonateLoadingContainer, LoadingWrap, LoadingLiWrapper, LoadingWaveBox } from "./LoadingMadal.styled";

const LoadingModal = () => {
  return (
    <StyledDonateLoadingContainer>
      <LoadingWrap>
        <LoadingLiWrapper>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
          <LoadingWaveBox></LoadingWaveBox>
        </LoadingLiWrapper>
      </LoadingWrap>
    </StyledDonateLoadingContainer>
  );
};

export default LoadingModal;
```



```react
import { styled } from "@/styles/theme";

export const StyledDonateLoadingContainer = styled.div`
  display: flex;
  height: 100vh;
  justify-content: center;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.8);
`;

export const LoadingWrap = styled.div`
  width: auto;
  height: auto;
`;

export const LoadingLiWrapper = styled.ul`
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  animation: rot 8s linear infinite;
  @-webkit-keyframes rot {
    100% {
      transform: rotate(360deg);
    }
  }
  @keyframes rot {
    100% {
      transform: rotate(360deg);
    }
  }
`;

export const LoadingWaveBox = styled.li`
  width: 1rem;
  height: 1rem;
  background: #40b6ff;
  border-radius: 4px;
  box-shadow: 0 0 1px #fff, 0 0 5px #40b6ff, 0 0 10px #40b6ff, 0 0 15px #40b6ff, 0 0 25px #40b6ff, 0 0 55px #40b6ff;
  -webkit-animation: scale 0.8s linear alternate infinite;
  animation: scale 0.8s linear alternate infinite;
  @-webkit-keyframes scale {
    100% {
      transform: scale(0.1);
      opacity: 0;
    }
  }
  @keyframes scale {
    100% {
      transform: scale(0.1);
      opacity: 0;
    }
  }
  &:nth-child(1) {
    z-index: 24;
  }
  &:nth-child(2) {
    z-index: 23;
  }
  &:nth-child(3) {
    z-index: 22;
  }
  &:nth-child(4) {
    z-index: 21;
  }
  &:nth-child(5) {
    z-index: 20;
  }
  &:nth-child(6) {
    z-index: 19;
  }
  &:nth-child(7) {
    z-index: 18;
  }
  &:nth-child(8) {
    z-index: 17;
  }
  &:nth-child(9) {
    z-index: 16;
  }
  &:nth-child(10) {
    z-index: 15;
  }
  &:nth-child(11) {
    z-index: 14;
  }
  &:nth-child(12) {
    z-index: 13;
  }
  &:nth-child(13) {
    z-index: 12;
  }
  &:nth-child(14) {
    z-index: 11;
  }
  &:nth-child(15) {
    z-index: 10;
  }
  &:nth-child(16) {
    z-index: 9;
  }
  &:nth-child(17) {
    z-index: 8;
  }
  &:nth-child(18) {
    z-index: 7;
  }
  &:nth-child(19) {
    z-index: 6;
  }
  &:nth-child(20) {
    z-index: 5;
  }
  &:nth-child(21) {
    z-index: 4;
  }
  &:nth-child(22) {
    z-index: 3;
  }
  &:nth-child(23) {
    z-index: 2;
  }
  &:nth-child(24) {
    z-index: 1;
  }
  &:nth-child(25) {
    z-index: 0;
  }
  &:nth-child(1) {
    -webkit-animation-delay: 0.1s;
    animation-delay: 0.1s;
  }
  &:nth-child(7) {
    -webkit-animation-delay: 0.3s;
    animation-delay: 0.3s;
  }
  &:nth-child(13) {
    -webkit-animation-delay: 0.5s;
    animation-delay: 0.5s;
  }
  &:nth-child(19) {
    -webkit-animation-delay: 0.7s;
    animation-delay: 0.7s;
  }
  &:nth-child(24) {
    -webkit-animation-delay: 0.9s;
    animation-delay: 0.9s;
  }
  &:nth-child(2) {
    -webkit-animation-delay: 0.2s;
    animation-delay: 0.2s;
  }
  &:nth-child(8) {
    -webkit-animation-delay: 0.4s;
    animation-delay: 0.4s;
  }
  &:nth-child(14) {
    -webkit-animation-delay: 0.6s;
    animation-delay: 0.6s;
  }
  &:nth-child(20) {
    -webkit-animation-delay: 0.8s;
    animation-delay: 0.8s;
  }
  &:nth-child(3) {
    -webkit-animation-delay: 0.3s;
    animation-delay: 0.3s;
  }
  &:nth-child(9) {
    -webkit-animation-delay: 0.5s;
    animation-delay: 0.5s;
  }
  &:nth-child(15) {
    -webkit-animation-delay: 0.7s;
    animation-delay: 0.7s;
  }
  &:nth-child(4) {
    -webkit-animation-delay: 0.4s;
    animation-delay: 0.4s;
  }
  &:nth-child(10) {
    -webkit-animation-delay: 0.6s;
    animation-delay: 0.6s;
  }
  &:nth-child(5) {
    -webkit-animation-delay: 0.5s;
    animation-delay: 0.5s;
  }
  &:nth-child(1) {
    -webkit-animation-delay: 0.1s;
    animation-delay: 0.1s;
  }
  &:nth-child(6) {
    -webkit-animation-delay: 0.2s;
    animation-delay: 0.2s;
  }
  &:nth-child(11) {
    -webkit-animation-delay: 0.3s;
    animation-delay: 0.3s;
  }
  &:nth-child(16) {
    -webkit-animation-delay: 0.4s;
    animation-delay: 0.4s;
  }
  &:nth-child(21) {
    -webkit-animation-delay: 0.5s;
    animation-delay: 0.5s;
  }
  &:nth-child(7) {
    -webkit-animation-delay: 0.3s;
    animation-delay: 0.3s;
  }
  &:nth-child(12) {
    -webkit-animation-delay: 0.4s;
    animation-delay: 0.4s;
  }
  &:nth-child(17) {
    -webkit-animation-delay: 0.5s;
    animation-delay: 0.5s;
  }
  &:nth-child(22) {
    -webkit-animation-delay: 0.6s;
    animation-delay: 0.6s;
  }
  &:nth-child(13) {
    -webkit-animation-delay: 0.5s;
    animation-delay: 0.5s;
  }
  &:nth-child(18) {
    -webkit-animation-delay: 0.6s;
    animation-delay: 0.6s;
  }
  &:nth-child(23) {
    -webkit-animation-delay: 0.7s;
    animation-delay: 0.7s;
  }
  &:nth-child(19) {
    -webkit-animation-delay: 0.7s;
    animation-delay: 0.7s;
  }
  &:nth-child(24) {
    -webkit-animation-delay: 0.8s;
    animation-delay: 0.8s;
  }
  &:nth-child(25) {
    -webkit-animation-delay: 0.9s;
    animation-delay: 0.9s;
  }
`;
```

