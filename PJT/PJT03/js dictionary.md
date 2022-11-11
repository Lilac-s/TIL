# js dictionary

```react
//* 꽃 이름 : 꽃 송이수 출력을 위한 로직
  let flowerInfo = {};
  if (customOption.flowers) {
    const copyOfFlowers = [...customOption.flowers];
    copyOfFlowers.map((flowerNumber, index) => {
      if (!flowerInfo[flowerNumber]) {
        flowerInfo[flowerNumber] = 1;
      } else if (flowerInfo[flowerNumber]) {
        flowerInfo[flowerNumber]++;
      }
    });
  }
```



`Object.entries` 로 출력



```html
<div className={styles.description_wrapper}>
              {Object.entries(flowerInfo).map(([key, value]) => (
                <>
                  <span className={styles.description}>
                    {flower[Number(key)].title}&nbsp;&nbsp;
                    {value}송이
                  </span>
                </>
              ))}
            </div>
```

