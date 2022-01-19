# Python 02. 데이터 & 제어문

보안상의 이유로 인해 문제는 삭제합니다.



### 1. Mutable & Immutable



```python
String, List, Tuple, Range, Set, Dictionary
```

---

(1) mutable

`List`, `Set`, `Dictionary`, `range`

(2) immutable

`String`, `Tuple`





### 2. 홀수만 담기



---

```python
list(range(53))[1:52:2]
```





### 3. Dictionary 만들기



---

```python
dict_class = dict(jangho='1', dasom='2', yesuel='3', wuyeong='4', dongshin='5', dongwan='6', minyeong='7', minjung='8', wuwon='9', gunhwa='10', dabin='11', sugeun='12', youji='13', yonghyun='14', dyne='15', surang='16', junggun='17', jinhang='18', hyuntae='19', jinsae='20', ahyun='21', hangju='22', myeongweon='23', suyeon='24', junhyeok='25')
```



### 4. 반복문으로 네모 출력



```python
n = 5
m = 9
```

---

```python
n = 5
m = 9

for i in range(m):
    print('*'*n)
```



### 5. 조건 표현식



```python
temp = 36.5
if temp >= 37.5:
    print('입실 불가')
else:
    print('입실 가능')
```

---

```python
temp = 36.5
print('입실 불가')if temp>= 37.5 else print('입실 가능')
```





### 6. 평균 구하기



```python
scores = [80, 89, 99, 83]
```

---

```python
scores = [80, 89, 99, 83]
result = 0

for i in scores:
    result += i
print(result/len(scores))
```

