# 0125_workshop

## 1. 무엇이 중복일까

```python
def duplicated_letters(strs):
    letter_list = []
    for i in range(len(strs)):
        if strs.count(strs[i]) > 1:
            letter_list.append(strs[i])
    return list(set(letter_list))

print(duplicated_letters('apple'))
```

## 2. 소대소대

```python
def low_and_up(strs):
    strs_list = list(strs)
    for i in range(len(strs)):
        if i % 2 == 0:
            strs_list[i] = strs_list[i].lower()
        elif i % 2 == 1:
            strs_list[i] = strs_list[i].upper()
    return ''.join(strs_list)
        
print(low_and_up('apple'))
print(low_and_up('banana'))
print(low_and_up('BANANA'))
```

## 3. 솔로 천국 만들기

```python
def lonely(strs) :
    result = [strs[0]] 
    for i in range(len(strs)) : 
        if result[-1] == strs[i]: 
            continue			
        else :
            result.append(strs[i])  
    return result
```