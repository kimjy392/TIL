console.log('Happy!')

// var
console.log(a) // undefined
var a = '변수'
// 변수 hoisting(호이스팅)
// : 해당 스코프 범위 내에서 최상단에 변수의 선언을 함.
// var a
// console.log(a)
// a = '변수'

// let(ES6+)
// console.log(b)  Error : Reference error
// let b = '변수'
let b = '변수'
b = '다른 변수' // 재할당 가능
let b = '다른 변수' // 재선언 불가능


// const(ES6+)
// 재선언 및 재할당이 불가능하다.
const c = '상수'
c = '다른 값'   // 재할당
const c = '다른상수'    // 재선언
const tak // 불가능

// let, const vs var
// 재선언이 불가능하다. vs 가능하다.
// 블록 스코프 vs 함수 스코프
var outerVar = '밖'
if (true){
    var outerVar = '안'
    console.log(outerVar) // 안
}
console.log(outerVar) // 안

let outerLet = '밖'
if (true) {
    let outerLet = '안'
    console.log(outerLet) // 안
}
console.log(outerLet) // 밖