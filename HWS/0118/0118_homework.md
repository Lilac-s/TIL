# Python 02. 데이터 & 제어문



### 1. Mutable & Immutable

주어진 컨테이너들을 각각 변경 가능한 것(mutable)과 변경 불가능한 것(immutable)으로 분류하시오

```python
String, List, Tuple, Range, Set, Dictionary
```

---

(1) mutable

`List`, `Set`, `Dictionary`, `range`

(2) immutable

`String`, `Tuple`





### 2. 홀수만 담기

range와 slicing을 활용하여 1부터 50까지의 숫자 중, 홀수로만 이루어진 리스트를 만드시오.

---

```python
list(range(53))[1:52:2]
```





### 3. Dictionary 만들기

반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.

---

```python
dict_class = dict(jangho='1', dasom='2', yesuel='3', wuyeong='4', dongshin='5', dongwan='6', minyeong='7', minjung='8', wuwon='9', gunhwa='10', dabin='11', sugeun='12', youji='13', yonghyun='14', dyne='15', surang='16', junggun='17', jinhang='18', hyuntae='19', jinsae='20', ahyun='21', hangju='22', myeongweon='23', suyeon='24', junhyeok='25')
```



### 4. 반복문으로 네모 출력

두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를 별(*) 문자를 이용하여 출력하시오. 단, 반복문을 사용하여 작성하시오.

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

주어진 코드의 조건문을 조건 표현식으로 바꾸어 작성하시오.

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

주어진 list에 담긴 숫자들의 평균값을 출력하시오.

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

