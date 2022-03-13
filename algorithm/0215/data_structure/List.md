# List

2022.02.14

참고자료

- [생활코딩-리스트(List)](https://opentutorials.org/module/1335/8636)
- [나무위키-리스트(자료구조)](https://namu.wiki/w/%EB%A6%AC%EC%8A%A4%ED%8A%B8(%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0))
- [파이썬으로 구현하는 링크드 리스트](https://velog.io/@woga1999/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EB%A7%81%ED%81%AC%EB%93%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8)



## 1단계 : 자료구조의 목적과 이론 이해



### List란 무엇인가?

추상적 자료형, 자료구조의 하나. 순열(Sequence)이라고도 불리며, 순서를 가지고 일렬로 나열한 원소들의 모임으로 정의한다. 순서가 있다는 점에서 집합과는 구별되며, 갈림길 없이 일렬로 나열되어 처음과 끝이 하나씩만 있다는 점에서 그래프와도 구별된다.

- 리스트와 배열의 차이점

  리스트 이전에, 다수의 데이터를 그룹핑해서 효율적으로 관리할 수 있는 데이터 스트럭쳐인 배열이 있었다. 배열의 가장 큰 특징은 인덱스를 이용하여 데이터를 가져올 수 있다는 것이다. 하지만 배열에서 인덱스를 이용하여 어떤 데이터를 가져오고 삭제했을 때, 그 데이터가 삭제된 공간을 빈 공간으로 남겨둬야 한다는 단점이 발생하였다. 빈 공간은 메로리의 낭비를 초래하며, 배열에 데이터가 있는지 없는지를 체크하는 로직을 필요로 하게 된다.

  이것을 보완하기 위하여 리스트가 등장하였다. 리스트는 배열이 가지고 있는 인덱스라는 장점을 버리고, 대신 빈틈없는 데이터의 적재라는 장점을 취한 데이터 스트럭쳐라고 할 수 있다.

리스트에서는 인덱스가 중요하지 않다. 리스트 데이터 스트럭쳐의 핵심은 엘리먼트들 간의 순서이다. 그래서 리스트를 다른 말로는 시퀀스(sequence)라고도 부른다. 즉, 리스트는 순서가 있는 데이터의 모임이다.

> Textbook-List1-Array1, Textbook-List2-Array2에 추가적인 자료를 정리해 두었다.



## 2단계 : 자료구조의 구현 로직 따라가기

- 파이썬으로 구현하는 링크드 리스트
  - 링크드 리스트란?
    - 각 노드가 데이터와 포인터를 가지고 한 줄로 연결되어 있는 방식으로 데이터를 저장하는 자료 구조.
    - 데이터를 담고 있는 노드들이 연결되어 있으며, 노드의 포인터가 다음이나 이전의 노드와의 연결을 담당하게 된다.



- 노드 구현

  ```python
  class Node:
      def __init__(self, data):
          self.data = data
          self.next = None
  ```



- 링크드 리스트 구현

  ```python
  class LinkedList:
      def __init__(self, data):
          self.head = Node(data)
      
      #헤더부터 탐색해 뒤에 새로운 노드 추가하기
      def append(self, data):
          cur = self.head
          while cur.next is not None:
              cur = cur.next
          cur.next = Node(data)
  	
      #모든 노드 값 출력
      def print_all(self):
          cur = self.head
          while cur is not None:
              print(cur.data)
              cur = cur.next
  ```



- 노드 인덱스 알아내기

  ```python
      def get_node(self, index):
          cnt = 0
          node = self.head
          while cnt < index:
              cnt += 1
              node = node.next
          return node
  ```

  

- 삽입

  ```python
      def add_node(self, index, value):
          new_node = Node(value)
          if index == 0:
              new_node.next = self.head
              self.head = new_node
              return
          node = self.get_node(index-1)
          next_node = node.next
          node.next = new_node
          new_node.next = next_node
  ```



- 삭제

  ```python
      def delete_node(self, index):
          if index == 0:
              self.head = self.head.next
              return
          node = self.get_node(index-1)
          node.next = node.next.next
  ```

  





## 3단계 : 자료구조의 형태와 오퍼레이션 직접 구현하기

