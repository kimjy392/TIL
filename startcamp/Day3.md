# Startcamp Day3

## 연습 문제 정리

1. 문제 1

   - 문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

   ```python
   str = list(input('문자를 입력하세요: '))
   
   print(str[0])
   print(str[-1]) # => -1 인덱스 접근은 가장 마지막이다.
   ```

   `str[0] = 'a'` 이고 `str[-1] = e` 이다. -1을 인덱스는 마지막 배열을 가리킨다.

   ​	

2. 문제 2

   - 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

   ```python
   numbers = int(input('숫자를 입력하세요: '))
   
   for number in range(numbers):
       print('{}'.format(number+1))
   ```

   ```python
   # 탁희쌤 풀이
   numbers = int(input('숫자를 입력하세요: '))
   for number in range(numbers):
       print(number+1) 
   ```

   ​	

3. 문제 3

   - 숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.

   ```python
   number = int(input('숫자를 입력하세요: '))
   
   if number % 2:
       print('홀수입니다.')
   else:
       print('짝수입니다.')
   ```

   `number % 2 ==0`과 같이 표현해도 되지만 0과 1을 가지고 있기 때문에 위와 같이 표현해도 된다.

   `if x:`  조건 x에서 0은 False, 0을 제외한 다른 수는 True

   ​	

4. 문제 4

   - 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.

     국어는 90점 이상,

     영어는 80점 초과,

     수학은 85점 초과, 

     과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)

     다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 

   ```python
   a = int(input('국어: '))
   b = int(input('영어: '))
   c = int(input('수학: '))
   d = int(input('과학: '))
   
   if a >= 90 and b > 80 and c > 85 and d >= 80:
       print('True')
   else:
       print('False')
   ```

   `and`를 이용하여 논리 연산을 한다.

   ​	

5. 문제 5

   - 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.

     입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.

     입력 예시: 300000;20000;10000

     ​	

     1. 반복문

        ```python
        prices = prices.split(';')
        int_price = []
        for price in prices:
            int_price.append(int(price))
        print(int_price)
        ```

        `변수.append( x )`를 이용하여 리스트에 수를 추가할 수 있다.

        `.split(';')`: 리스트로 반환한다. 원본이 바뀌지는 않는다. 하나의 인자를 받고 싶다면 `.split(';')[0]`을 사용한다.

        

     2. list comprehension

     ```python
       int_price2 = [int(price) for price in prices]
       print(int_price2)
     ```

        `list comprehension`은 많이 사용하고 실행 시간이 1번 반복문을 이용한 것보다 짧다.

   

   3. map

      ```python
      int_price3 = list(map(int,prices))
      print(int_price3)
      int_price3 = sorted(int_price3, reverse = True)
      # int_price3.sort()     sorted()를 대신해서
      
      # int_price3.reverse() reverse를 대신해서 
      
      for price in int_price3:
      print(price)
      ```

   `map(func, x ):`첫번째 인자의 함수를 두번째 인자를 반복하며 적용, 반복 가능한 객체에 함수를 각각 적용

   `.reverse():` 숫자를 반대로 뒤집어 준다. 설명을 보면 flag가 있는데 보통 True/ False값을 인자로 가진다.

   `.sort():` return이 None. 원본 리스트 자체를 변경

   `sorted(list):`return이 정렬된 리스트. 원본 자체는 변경하지 않음



## HTML/CSS

### HTML

`HTML` 은 HyperText Markup Language의 약자로 웹 문서를 구조화 하는데 사용되는 언어이다.

1. HTML 기본 구조

   ```html
   <!DOCTYPE html>
   <html lang="ko">
   <head>
       <meta charset="UTF-8">
       <title>Document</title>
   </head>
   <body>
       <h1>용흠아 안녕!</h1>
   </body>
   </html>
   ```

   - `<head> </head>` 는 문서의 정보를 담고 있다.
   - `<body> </body>` 는 문서의 본문을 담고 있다.

2. 태그의 종류

   1. 기본적으로 태그는 `여는태그`와 `닫는태그` 로 구성된다.

      ```html
      <h1>제목1</h1>
      ```

   2. `닫는태그` 가 없는 경우도 있다. (self-closing tag)

      ```html
      <img src="__"/>
      ```

3. 태그의 구성

   ```html
   <img src="____" width="300" height="300" class="img-blue"/>
   <a href="https://google.com" class="blue">구글</a>
   ```

   - 태그별로 공통적으로 가질 수 있는 속성 : `id` , `class` , `style`
   - 각 태그별로 가질 수 있는 속성이 추가적으로 있다.
     - img - `src`, `width` , `height`
     - a - `href` 



### CSS

CSS는 Cascading Style Sheets의 약자로, HTML을 꾸며주는 역할을 한다.

HTML을 꾸며주기 위하여, `선택자(selector)`를 통해 특정한 element를 지정하여야 한다.

1. 선택자

   - 태그 선택자

     ```css
     p {
         color: red;
     }
     ```

   - class 선택자

     ```css
     .blue {
         color: blue;
     }
     ```

   - id 선택자

     ```css
     #pink {
     	color: pink;
     }
     ```

   선택자 우선순위는 id선택자 > class선택자 > 태그선택자 순서로 적용된다.



## Flask

`Flask` 는 파이썬 기반의 micro framework이다.

### 기본 활용법

1. 설치

   ```bash
   $ pip install flask
   ```

2. 기본 코드

   ```python
   # app.py
   from flask import Flask
   
   app = Flask(__name__)
   
   @app.route('/')
   def hello():
       return 'Hello!'
   
   if __name__ == '__main__':
       app.run(debug=True)
   
   ```

3. 서버 실행

   ```bash
   $ flask run
   
   ```

   - 기본적으로 `flask run` 명령어는 `app.py` 파일을 실행시킨다. 
     만약 다른 파일명으로 만들었다면, 옵션을 추가해야 한다.
   - 마지막 두 줄을 작성해놓았다면, 아래와 같이 실행도 가능하다.

   ```bash
   $ python app.py
   
   ```

## Variable routing

요청 오는 url을 변수화 하여 값을 사용할 수 있다.

```python
@app.route('/hi/<string:name>')
def hi(name):
    return f'{name}아 안녕?'

```

## Rendering Template

`HTML` 파일을 만들어 활용할 수 있다. 기본적으로 `templates` 폴더에 파일을 만들어야 한다.

```
app.py
templates/
	hi.html
	lunch.html
	index.html

```

```python
from flask import Flask, render_template
# ...
@app.route('/hi')
def hi():
    return render_template('hi.html')

```

`HTML` 파일에서 변수의 값을 출력하고자 한다면, 키워드 인자로 그 값을 넘겨줘야한다.

```python
return render_template('hi.html', name=name)

```

그리고 출력을 위해서는 `{{ }}` 사용한다.

```jinja2
<h1>{{name}} 안녕?</h1>
```

## Flask Template Engine - jinja2

Flask는 기본적으로 Template을 만들 때 `jinja2` 언어를 사용한다. 기본 문법은 다음과 같다.

1. 값 출력

   ```jinja2
   <h1> {{ name }}, 안녕? <h1>
   ```

2. 조건문

   ```jinja2
   {% if name == '용흠' %}
   	<h1>반장님 안녕하세요.</h1>
   {% else %}
   	<h1>학생들 ㅎㅇ</h1>
   {% endif %}
   ```

3. 반복문

   ```jinja2
   {% for menu in menu_list %}
   	<li>{{ menu }}</li>
   {% endif %}
   ```













