# Python 02. 데이터 & 제어문

보안상의 이유로 인해 문제는 삭제합니다.



### 1. 간단한 N의 약수



---

```python
nat = int(input())

for i in range(1,1001,1):
    if nat % i == 0:
        print(i, end=' ')
```





### 2. 중간값 찾기



```python
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
```

---

```python
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
numbers.sort()
print(numbers[int(len(numbers)/2 - 0.5)])
```



### 3. 계단 만들기



---

```python
nat = int(input())

for i in range(1,nat+1):
    for k in range(1,i+1):
        print(k, end=' ')
    print()
```

