# boj_2477_meoln



```python
k = int(input())

max_length = []
small_length = []

a = [list(map(int, input().split())) for _ in range(6)]
a_idx = [i[0] for i in a]

for i in a_idx:
    if a_idx.count(i) == 1:
        max_length.append(a[a_idx.index(i)][1])
        if a_idx.index(i) == 5:
            small_length.append(abs(a[a_idx.index(i)-1][1] - a[a_idx.index(i)-5][1]))
        else:
            small_length.append(abs(a[a_idx.index(i)-1][1] - a[a_idx.index(i)+1][1]))

small_area = small_length[0] * small_length[1]
max_area = max_length[0] * max_length[1]

print(k * (max_area - small_area))
```

