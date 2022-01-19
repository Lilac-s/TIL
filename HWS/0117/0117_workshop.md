# Python 01. 데이터 & 제어문

보안상의 이유로 인해 문제는 삭제합니다.



### 1. 세로로 출력하기



---

```python
nat = int(input())

for i in range(1, nat+1):
    print(i)
```





### 2. 거꾸로 세로로 출력하기



---

```python
nat = int(input())
list_nat = list(range(0,nat+1))

for i in range(1, nat+2):
    print(list_nat[-i])
```



### 3. N줄 덧셈



---

```python
nat = int(input())

if nat >= 10000:
    print('10000보다 작은 수를 입력하세요.')

elif nat % 2 == 0:
    print(int(nat/2)*(nat+1))

elif nat % 2 == 1:
    print(int((nat/2-0.5)*(nat+1)+(nat/2+0.5)))
```

