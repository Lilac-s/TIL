# 0127_homework

## 1. Circle �ν��Ͻ� �����

```python
o = Circle(3, 2, 4)
print(o.area())
print(o.circumference())
```

```python
28.259999999999998
18.84
```



## 2. Dog�� Bird�� Animal�̴�

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! �ȴ´�!')

    def eat(self):
        print(f'{self.name}! �Դ´�!')

class Dog(Animal):
    def walk(self):
        print(f'{self.name}! ������!')
    
    def bark(self):
        print(f'{self.name}! ¢�´�!')

class Bird(Animal):
    def walk(self):
        super().walk()
    
    def eat(self):
        super().walk()

    def fly(self):
        print(f'{self.name}! Ǫ���!')

dog = Dog('�۸���')
dog.walk()
dog.bark()

bird = Bird('����')
bird.walk()
bird.eat()
bird.fly()
```

```python
�۸���! ������!
�۸���! ¢�´�!
����! �ȴ´�!
����! �ȴ´�!
����! Ǫ���!
```





## 3. ������ ����

- ZeroDivisionError
  - ���̽㿡���� � ���� 0���� ������ �Ǹ� ������ �߻��մϴ�.
- NameError
  - ���� Ȥ�� ���� �̸� ���� ������ ��ȿ���� ���� �̸��� ����� �� �����ϴ�.
  - ��, ��� �������� ���ǵ��� ���� ������ ȣ���Ͽ��� ��� ������ �߻��մϴ�.
- TypeError
  - �ڷ����� �ùٸ��� ���� ���
  - �Լ� ȣ�� �������� �ʼ� �Ű������� ������ ���
  - �Լ� ȣ�� �������� �Ű����� ������ �ʰ��ؼ� ���� ���
- IndexError
  - �������� �ʴ� index�� ��ȸ�� ���
- KeyError
  - �������� �ʴ� Key�� ������ ���
- ModuleNotFoundError
  - �������� �ʴ� Module�� `import`�ϴ� ���
- ImportError
  - Module�� ã������ �������� �ʴ� Ŭ����/�Լ��� �������� ���