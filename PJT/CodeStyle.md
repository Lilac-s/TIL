코드 스타일을 일치시키기 위해서 css로 짰던 코드를 styled.div로 바꿔 보았다.
처음엔 어떻게 하나 했는데, 예시를 보니까 바로 할 수 있었다.
역시 예시가 있는 건 정말 강력하다 bb 헤더 색깔 바뀌는 것도 예시를 보고 했으니..
이게 구글링의 힘일까?

```js
const DrinkUsHeader = styled.div`
  position: fixed;
  display: flex;
  padding: 40px 4rem;
  justify-content: center;
  background-color: ${(props) => props.color};
  margin: auto;
  width: calc(100% - 8rem);
  opacity: ${(props) => props.opacity};
`;

const user = useSelector((state) => state.user);
  return (
    <DrinkUsHeader color={HeaderStatus ? "white" : "black"} opacity={HeaderStatus ? "0.9" : "0.7"}>
      <HeaderMenu width={100} justify={"space-between"}>
        <li>
          <NavLink to="/" className={HeaderStatus ? "a" : "a light"}>DrinkUs</NavLink>
        </li>
        <li>
          <NavLink to={"/live"} className={HeaderStatus ? "a" : "a light"}>술Live</NavLink>
        </li>
        <li>
          <NavLink to={"/community"} className={HeaderStatus ? "a" : "a light"}>커뮤니티</NavLink>
        </li>
        {user.isLogin ? (
          <>
            <li>
              <NavLink to={"/users/{user_no}"} className={HeaderStatus ? "a" : "a light"}>{user.data.nickName}님</NavLink>
            </li>
            <li>
              {/* api 문서 나오면 주소 일치시켜야 해 */}
              <NavLink to={"/alarm"} className={HeaderStatus ? "a" : "a light"}><i class="far fa-heart"></i></NavLink>
            </li>
            <li>
              {/* api 문서 나오면 주소 일치시켜야 해 */}
              <NavLink to={"/friend"} className={HeaderStatus ? "a" : "a light"}><i class="fa-solid fa-user-group"></i></NavLink>
            </li>
            <li>
              <NavLink to={"/logout"} className={HeaderStatus ? "a" : "a light"}>로그아웃</NavLink>
            </li>
          </>
        ) : (
          <>
            <li>
              <NavLink to={"/login"} className={HeaderStatus ? "a" : "a light"}>로그인</NavLink>
            </li>
            <li>
              <NavLink to={"/join"} className={HeaderStatus ? "a" : "a light"}>회원가입</NavLink>
            </li>
          </>
        )}
      </HeaderMenu>
    </DrinkUsHeader>
  );
};

