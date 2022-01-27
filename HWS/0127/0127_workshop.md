# 0127_workshop

## 도형 만들기

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


        

class Rectangle:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_garo_sero(self):
        garo = self.p2.x - self.p1.x
        sero =  self.p1.y - self.p2.y
        return (garo, sero)

    def get_area(self):
        garo, sero = self.get_garo_sero()
        return garo * sero

    def get_perimeter(self):
        garo, sero = self.get_garo_sero()
        return 2*(garo + sero)

    def is_square(self):
        garo, sero = self.get_garo_sero()
        if garo == sero:
            return True
        else:
            return False
```

