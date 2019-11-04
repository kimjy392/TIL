해당 작업을 하는 함수를 인자로 받아서

나중에 저 함수를 부르자(callback)



Promise object를 리턴한다.

나중에(작업이 끝나면) then/catch를 실행 한다.

* promise object 상태
  * pending -> 작업 진행중
  * resolved -> resolve 함수 호출(작업 성공시)
  * rejected -> reject 함수 호출(작업 실패시)
* resolve -> then에서 처리, reject -> catch에서 처리