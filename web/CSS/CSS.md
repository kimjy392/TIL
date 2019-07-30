# 190730 CSS

## CSS

* CSS(*Cascading Style Sheets*)

* HTML은 정보와 구조화, CSS는  styling의 정의, 각자 문법이 다른 별개의 언어.

  ```css
  h1 {
      color: blue; /* color - property, blue - value*/
      font-size:15px
  }
  ```

## CSS 활용하기

1. Inline 인라인

   * HTML 요소의 style에 CSS를 넣기

   ```html
     <!-- 태그 안에 style넣으면(인라인) 고생해서 사용해줘-->
     <p id="green" style="color: purple;">인라인 CSS 활용</p> 
   ```

2. Embedding 내부참조

   * HTML내부에 CSS를 포함시키기(선택자 사용하는거 봐)

   ```html
    <style>
       /* 태그 선택자 */
       h1 {
         color: red;
       }
       /* 클래스 선택자 : .클래스명 */
       .blue {
         color: blue;
       }
       /* 아이디 선택자 : #아이디명 */
       #green {
         color: green ;
       }
     </style>
   <body>
       <h1>Hello, CSS!</h1> <!-- 위의 정의된 스타일로 h1태그의 글자가 빨간색으로 변한다. -->
   </body>
   ```

3. Link file 외부참조

   * 외부에 있는 CSS파일을 로드하기

   ```html
   <head>
       <link rel="stylesheet" href="01_style.css">
   </head>
   ```



### 선택자

* 선택자는 우선순위가 있다.  !important > 인라인 > class > id > tag 순서

  ```css
      .brown {
        color: brown !important; /* CSS파일이나 html에서 선택자를 정의할 때 이런식으로 사용*/
      }
  	h1 {
    		text-align: center; /* 텍스트를 가운데 정렬*/
  		}
  ```

1. 그룹 선택자

   ```css
   h1, h2, h3, h4, h5, h6, .goldenrod {
     color: goldenrod;
   }
   ```

2. 인접 선택자

   ```css
   /* 인접 선택자 */
   .blue + .red + div {
     background-color: purple;
   }
   ```

3. 자식 선택자

   ```css
   /* 자식 선택자 */
   .parent > li {
     color: red;
   }
   ```

   자식 선택자는 `.parent`가 있는 태그에서 바로 밑 하위에 있는`ls`태그만 색상을 변화시킨다.

4. 후손 선택자

   ```css
   /* 후손 선택자 */
   .ancestor li {
     color: blue;
   }
   ```

   후손 선택자는 `.ancestor`가 있는 태그가 포함하는 모든 `li`태그의 색상을 변화시킨다.



* id는 문서에서 반드시 한번만 등장한다.
* class는 문서에서 여러번 등장한다.



