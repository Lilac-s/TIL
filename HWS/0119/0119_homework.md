# Python 03. 함수



## 1. Built-in 함수

Python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.

---

- abs : abs(value)는 인수로 숫자값 value를 받았을 때, 절대값을 반환한다. 입력이 복소수인 경우 abs(a+bj) = sqrt(a^2 + b^2) 값을 반환한다.

- divmod : divmod(a, b) - 두 개의 숫자를 입력 받아 a / b의 몫과 나머지를 튜플(tuple)의 형태로 변환한다. 출력 : (몫, 나머지).
- enumerate : 시퀀스 자료형(리스트, 튜플, 문자열)을 입력 받아, enumerate 객체를 반환한다. enumerate 객체는 첫번째로 그 순서값, 두번째로 그 순서값에 해당되는 시퀀스 자료형의 실제값을 갖는 객체이다. enumerate는 주로 for문과 함께 많이 사용된다.
- eval : eval(expression) - 입력값으로 실행가능한 문자열 (3+4+5, 'lo'+'ve' 등)을 받아 문자열을 실행한 결과값을 반환한다.
- filter : filter(function, list) - 함수와 시퀀스 자료형을 입력으로 받아서 시퀀스 자료형(리스트, 튜플, 문자열)의 값이 하나씩 함수에 인수로 전달될 때 참을 변환시키는 값만 따로 모아서 동일한 시퀀스 자료형으로 반환하는 함수.
- map : map(function, iterable) - iterable을 뽑아 와서 function에 넣고 이 결과값을 리스트로 형변환하여 만들어낸다.



## 2. 정중앙 문자

문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를 작성하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.

```python
get_middle_char('ssafy') #=> a
get_middle_char('coding') #=> di
```

---

```python
st = list(input())

def get_middle_char(x, y):
    if len(st)%2 == 0:
        x = st[int((len(st))/2 - 1)]
        y = st[int((len(st))/2)]
    elif len(st)%2 == 1:
        x = st[int((len(st))/2 - 0.5)]
        y = ''
    return x, y

a, b = get_middle_char(st, st)
print('{0}{1}'.format(a, b))
```



## 3. 위치 인자와 키워드 인자

다음과 같이 함수가 선언되어 있을 때, 보기 (1)~(4) 중에서 실행 시 오류가 발생하는 코드를 고르시오.

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

# (1)
ssafy('허준')

# (2)
ssafy(location='대전', name='철수')

# (3)
ssafy('영희', location='광주')

# (4)
ssafy(name='길동', '구미')
```

---

(4),  SyntaxError.



## 4. 나의 반환값은

다음과 같이 함수를 선언하고 호출하였을 때, 변수 result에 저장된 값을 작성하시오.

```python
def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7)
```

---

10

None



## 5. 가변 인자 리스트

가변 인자 리스트를 사용하여, 갯수가 정해지지 않은 여러 정수들을 전달 받아 해당 정수들의 평균 값을 반환하는 my_avg 함수를 작성하시오.

```python
my_avg(77, 83, 95, 80, 70) #=> 81.0
```

---

```python
def my_avg(*nums):
    sum_all = 0
    for i in nums:
        sum_all += i
        result = sum_all / len(nums)
    return result

print(my_avg(77, 83, 95, 80, 70))
```

