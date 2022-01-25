# python 05. 데이터 구조 활용



## 1. 평균 점수 구하기

```python
def get_dict_avg(dict):
    sum_all = 0
    for i in dict.keys():
        sum_all += dict[i]
    return sum_all / len(dict)

print(get_dict_avg({'python':80, 'algorithm':90, 'django':89, 'web':83}))
```



## 2. 혈액형 분류하기

```python
def count_blood(blood_list):
    blood_dict = {}
    blood_kind = ['A', 'B', 'O', 'AB']
    for i in range(len(blood_kind)):
        cnt = 0
        if blood_kind[i] in blood_list:
            cnt += blood_list.count(blood_kind[i])
            blood_dict[blood_kind[i]] = cnt
    return blood_dict


print(count_blood(['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']))
```

