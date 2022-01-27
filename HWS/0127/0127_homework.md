# 0127_homework

## 1. Circle 인스턴스 만들기

```python
o = Circle(3, 2, 4)
print(o.area())
print(o.circumference())
```

```python
28.259999999999998
18.84
```



## 2. Dog과 Bird는 Animal이다

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def walk(self):
        print(f'{self.name}! 딜린다!')
    
    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def walk(self):
        super().walk()
    
    def eat(self):
        super().walk()

    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
```

```python
멍멍이! 딜린다!
멍멍이! 짖는다!
구구! 걷는다!
구구! 걷는다!
구구! 푸드덕!
```





## 3. 오류의 종류

- ZeroDivisionError
  - 파이썬에서는 어떤 수를 0으로 나누게 되면 에러가 발생합니다.
- NameError
  - 지역 혹은 전역 이름 공간 내에서 유효하지 않은 이름은 사용할 수 없습니다.
  - 즉, 어느 곳에서도 정의되지 않은 변수를 호출하였을 경우 에러가 발생합니다.
- TypeError
  - 자료형이 올바르지 못한 경우
  - 함수 호출 과정에서 필수 매개변수가 누락된 경우
  - 함수 호출 과정에서 매개변수 개수가 초과해서 들어온 경우
- IndexError
  - 존재하지 않는 index로 조회할 경우
- KeyError
  - 존재하지 않는 Key로 접근한 경우
- ModuleNotFoundError
  - 존재하지 않는 Module을 `import`하는 경우
- ImportError
  - Module은 찾았으나 존재하지 않는 클래스/함수를 가져오는 경우