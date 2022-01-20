# Python 04. 함수

보안상의 이유로 인해 문제는 삭제합니다.



## 1. 숫자의 의미



---

```python
def get_secret_word(nums):
    char = ''
    for i in range(len(nums)):
        char += chr(nums[i])
    return char

print(get_secret_word([83, 115, 65, 102, 89]))
```





## 2. 내 이름은 몇일까?



---

```python
def get_secret_number(string):
    num = 0
    for i in string:
        num += ord(i)
    return num

print(get_secret_number('tom'))
```





## 3. 강한 이름



---

```python
def get_strong_word(a, b):
    sum_a = 0
    for i in a:
        sum_a += ord(i)
    sum_b = 0
    for j in b:
        sum_b += ord(j)
    if sum_a >= sum_b:
        return a
    elif sum_a < sum_b:
        return b

print(get_strong_word('z', 'a'))
print(get_strong_word('tom', 'john'))
```

