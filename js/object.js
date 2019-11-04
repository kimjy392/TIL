const me ={
    name: 'tak',
    phone: '010-9429-xxxx',
    greeting: function() {
        return 'hi' + this.name
    }
}

const Person = function(name, phone) {
    this.name = name
    this.phone = phone
    this.greeting = function() {
        return 'hi, ' + this.name
    }
}

// 새로운 오브젝트 생성
const lee = new Person('lee', '010-1234-1234')


// 생성자 함수에서는 arrow function 사용 금지
// 상위함수가 this가 되기 떄문에 this가 window가 된다.
// 생성자 함수는 arrow function를 사용하면 에러를 
const Animal = name => {
    this.name = name
}

const dog = new Animal('dog') // Error

const name = '겨레'
const phone = '010-1234-1234'
const greeting = function() {
    return 'hi, ' + this.name
}
const you = {
    name,
    phone,
    greeting
}