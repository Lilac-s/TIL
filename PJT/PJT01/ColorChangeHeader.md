색이 변하는 헤더를 만들어 보았다.
opacity를 통해서 불투명도도 줬다.
헤더 배경색뿐만이 아니라 글자 색도 바꾸고 싶은데
태그를 어떻게 지정해야 할지 모르겠어서 아직 숙제로 남아있다.
대신 조금이나마 보기 좋게 만들기 위해서 글씨 색 자체는 조금 조정해 주었다.
바나나톡은 어떻게 한걸까...?

```js
const HeaderMenu = styled.ul`
  display: flex;
  width: calc(${(props) => props.width}% - 11rem);
  justify-content: ${(props) => props.justify};
`;

const Header = () => {
  const [ScrollY, setHeaderColor] = useState(0);
  const [HeaderStatus, setHeaderStatus] = useState(false);

  const handleColor = () => {
    setHeaderColor(window.pageYOffset);
    if(ScrollY > 640) {
      setHeaderStatus(true);
    } else {
      setHeaderStatus(false);
    }
  }

  useEffect(() => {
    const watch = () => {
      window.addEventListener('scroll', handleColor)
    }
    watch();
    return () => {
      window.removeEventListener('scroll', handleColor)
    }
  })

  const user = useSelector((state) => state.user);
  return (
    <div className={HeaderStatus ? "header active" : "header"}>
      <HeaderMenu width={100} justify={"space-between"}>
        <li>
          <NavLink to="/">DrinkUs</NavLink>
        </li>
        <li>
          <NavLink to={"/live"}>술Live</NavLink>
        </li>
        <li>
          <NavLink to={"/community"}>커뮤니티</NavLink>
        </li>
        {user.isLogin ? (
          <>
            <li>
              <NavLink to={"/users/{user_no}"}>{user.data.nickName}님</NavLink>
            </li>
            <li>
              {/* api 문서 나오면 주소 일치시켜야 해 */}
              <NavLink to={"/alarm"}><i class="far fa-heart"></i></NavLink>
            </li>
            <li>
              {/* api 문서 나오면 주소 일치시켜야 해 */}
              <NavLink to={"/friend"}><i class="fa-solid fa-user-group"></i></NavLink>
            </li>
            <li>
              <NavLink to={"/logout"}>로그아웃</NavLink>
            </li>
          </>
        ) : (
          <>
            <li>
              <NavLink to={"/login"}>로그인</NavLink>
            </li>
            <li>
              <NavLink to={"/join"}>회원가입</NavLink>
            </li>
          </>
        )}
      </HeaderMenu>
    </div>
  );
};

export default Header;

