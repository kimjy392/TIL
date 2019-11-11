## App - SearchBar

* input 태그에 등록된 이벤트 (@input)
* trigger : input 값이 변경 되면, 
* 인자로 `event`
* `onInput` method 실행

---

* search-bar 컴포넌트에 등록된 이벤트(@input-change-event)

* trigger : `$emit` 메소드 실행되면, (자식컴포넌트)
* 인자로 `event.target.value`
* `onInputChange` method 실행

