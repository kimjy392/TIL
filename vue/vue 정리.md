```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
</head>
<body>
    <div id="app">
        <h1>{{ message }}</h1>
        <!-- 반복문을 돌려서 li 태그로 이름 출력하기
            for
                if (같은 라인에서는 for가 우선순위가 높음)
        -->
        <li v-for='member in members' v-if="member.gender === 'M'">{{ member.name }} ?</li>
        <li v-else>{{ member.name }}</li>
        <!-- v-model 
            data 내에 초기화가 반드시 필요!
        -->
        <input type="text" v-model="userText">
       <p> 사용자 입력중....! {{ userText }}</p>
    </div>
    <script>
    const app = new Vue({
        el: '#app',
        data: {
            message: 'Hello',
            members: [
                {name: '경호', gender: 'M'},
                {name: '은비', gender: 'F'},
                {name: '태우', gender: 'M'}
            ],
            userText: ''
        },
    })
    </script>
</body>
</html>
```

### console에서 접근방법

* app.$data.message : 오브젝트로 접근

* app.message : 단축어로 접근

### flow

* 같은 라인이면 우선순위가 for가 더 먼저 실행된다.
* if 가 더 먼저 실행되야 된다면 for보다 위에 쓴다. 

### v-model

* 항상 정의가 되어있어야하고 초기화가 필요하다.

### Error

```
2vue.js:634 [Vue warn]: Property or method "userText" is not defined on the instance but referenced during render. Make sure that this property is reactive, either in the data option, or for class-based components, by initializing the property. See: https://vuejs.org/v2/guide/reactivity.html#Declaring-Reactive-Properties.

(found in <Root>)
```

* 이런 오류 메세지는 `userText`가 Vue에 정의되지 않았기 때문에 뜬다.

```
src="{{ url }}": Interpolation inside attributes has been removed. Use v-bind or the colon shorthand instead. For example, instead of <div id="{{ val }}">, use <div :id="val">.
```

* v-bind를 사용하지 않고 이용하였을 경우.