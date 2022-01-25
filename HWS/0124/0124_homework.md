# python 05. 데이터 구조 및 활용



## 1. 모음은 몇 개나 있을까?

```python
def count_vowels(strs):
    strs_list = list(strs)
    num = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(vowels)):
        if vowels[i] in strs:
            num += strs_list.count(vowels[i])
    return num

print(count_vowels('banana'))
```



## 2. 문자열 조작

(4) 



## 3. 정사각형만 만들기

```python
def only_square_area(n, m):
    area_list = []
    for i in range(len(n)):
        if n[i] in m:
            area = n[i]**2
            area_list.append(area)
    return area_list

print(only_square_area([32, 55, 63], [13, 32, 40, 55]))
```

