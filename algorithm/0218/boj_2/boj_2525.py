A, B = map(int, input().split())
C = int(input())

cook_H = C//60
cook_m = C - cook_H*60

end_H = A + cook_H
end_m = B + cook_m

if end_m >= 60:
    end_H = end_H + 1
    end_m = end_m - 60

if end_H >= 24:
    end_H = end_H - 24
print(f'{end_H} {end_m}')
