# 0425_workshop



```javascript
let firstName
firstName = 'youji'
firstName = 'YoujiSung'
```



```javascript
const lastName = 'youji'
lastName = 'YoujiSung'

```

Uncaught TypeError: Assignment to constant variable.
    at <anonymous>:1:10



---



```javascript
let fullName = 'Brendan Eich'

if (true) {
  let fullName = 'Guido Van Rossum'
  console.log('블록 스코프:', fullName)
}

console.log('전역 스코프:', fullName)
```

블록 스코프: Guido Van Rossum
전역 스코프: Brendan Eich



```javascript
if (true) {
  const language = 'Python'
  console.log(language)
}

console.log(language)
```

VM2341:6 Uncaught ReferenceError: language is not defined
    at <anonymous>:6:13



---



```javascript
var framework
framework = 'Bootstrap'
framework = 'Django'
var framework = 'Vue'
```



```javascript
function f1() {
  var message = 'You are doing great!'
}
f1()
console.log(message)
```

Uncaught ReferenceError: message is not defined
    at <anonymous>:5:13



---



```javascript
const codeEditor = 'vscode'

if (codeEditor === 'vscode') {
  var theme = 'dark+'
}
console.log(theme)
```

dark+



---



```javascript
function f2() {
  const stack = 'Last In, First Out'
}
f2()
console.log(stack)

function f3() {
  let queue = 'First In, First Out'
}
f3()
console.log(queue)
```

Uncaught ReferenceError: stack is not defined
    at <anonymous>:5:13



---



```javascript
console.log(hoisted) // undefined
var hoisted = 'can you see me?'
```

can you see me?



```javascript
console.log(lunch) // ReferenceError
const lunch = '초밥'
```

VM2624:1 Uncaught ReferenceError: lunch is not defined
    at <anonymous>:1:13



```javascript
console.log(dinner) // ReferenceError
let dinner = '스테이크'
```

Uncaught ReferenceError: dinner is not defined
    at <anonymous>:1:13