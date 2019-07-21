# README

## 영화진흥위원회 오픈 API(주간/주말 박스오피스 데이터)

* 최근 50주간의 데이터 중에 주간 박스오피스 TOP10데이터를 수집한다.

  * `요청 URL`은 기본으로 `key`값과 `targetDt`를 필수적을 포함하고 있어야 한다.
  * `key`: token
  * `targetDt`: 조회하려는 날짜

  1. 주간까지 기간의 데이터를 조회한다.

     주간까지의 데이터를 조회하기 위해서 `요청 URL`에 `weekGb=0`를 추가하여 `api`를 요청한다.

  2. 조회 기간은 총 50주이며, 기준일은 2019년 7월 13일이다.

     기준일이 2019년 7월 13일이기 때문에 날짜관련 method로 `datetime`를 `import`하여 사용한다.

  3. 다양성 영화/상업 영화를 모두 포함하여야 한다.

  4. 한국/외국 영화를 모두 포함하여야 한다.

  5. 모든 상영지역을 포합하여야 한다.

     * 3, 4, 5번은 `요청 URL`에 추가하지않고 `defaul`값이기 때문에 따로 추가하지 않아도 된다.

* 결과

  ```python
  import requests#6685160
  from decouple import config
  import csv
  from datetime import datetime, timedelta
  
  boxoffice_result = {}
  key = config('KEY')
  
  for i in range(0, 50):
      targetDt = str(datetime(2018, 8, 4) + timedelta(weeks=i))
      targetDt = targetDt[:10].replace('-','')
      api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0'
      response = requests.get(api_url).json()
      for movie in response.get('boxOfficeResult').get('weeklyBoxOfficeList'):
          boxoffice_result[movie['movieCd']] = {
              '영화 대표코드': movie['movieCd'], 
              '영화명' : movie['movieNm'], 
              '누적관람객': movie['audiAcc']
          }
  
  
  with open('boxoffice.csv', 'w', encoding='utf-8') as f:
      fieldnames = ['영화 대표코드', '영화명', '누적관람객'] # 여기만 생성
      csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
      csv_writer.writeheader()
      for item in boxoffice_result.values(): # 딕셔너리 만든 것 반복
          csv_writer.writerow(item)
  
  ```

  

  1. 50주간의 데이터를 가지고 와야하기 때문에 `datetime`를 이용하여 기준일에서 50주 이전인 2018년 8월 4일부터 한주씩 날짜를 바꿔 API를 요청한다.

     ```python
     for i in range(0, 50):
         targetDt = str(datetime(2018, 8, 4) + timedelta(weeks=i))
         targetDt = targetDt[:10].replace('-','')
     ```

     

  2. API구조가 다음과 같이 똑같은 구조로 이루어져있기 때문에 반복문을 이용하여 각 영화의 대표코드, 영화명, 누적관람객을 `boxoffice_result`에 `key`가 영화대표코드인 이중으로된 dictionary형태로 저장한다.

     API 그림

     ```json
     {"boxOfficeResult":
      {"boxofficeType":"주간 박스오피스",
       "showRange":"20190708~20190714",
       "yearWeekTime":"201928",
       "weeklyBoxOfficeList":[{
           "rnum":"1",
           "rank":"1",
           "rankInten":"0",
           "rankOldAndNew":"OLD",
           "movieCd":"20196309",
           "movieNm":"스파이더맨: 파 프롬 홈",
         "openDt":"2019-07-02",
           "salesAmt":"18704459230",
           "salesShare":"50.6",
           "salesInten":"-20291831880",
           "salesChange":"-52.0",
           "salesAcc":"57709310340",
           "audiCnt":"2163519",
           "audiInten":"-2357242",
           "audiChange":"-52.1",
           "audiAcc":"6685136",
           "scrnCnt":"1900",
           "showCnt":"61772"}]
      	}
   }
     ```
  
     저장되는 결과
  
     ```python
      boxoffice_result = {
         key : {'영화대표코드' : '123123',
              '영화명' : '탁희쌤',
                '누적관람객': '999999999999999999999999999'
               }
     }
     ```
  
  3. 중복된 영화의 데이터는 `boxoffice_result`의 `key`에 의해 덮어쓰기가 된다.
  
  4. 반복문의 `movie`는 딕셔너리이기 때문에 `movie['movieCd']` 표현이 가능하다.
  
     ```python
       for movie in response.get('boxOfficeResult').get('weeklyBoxOfficeList'):
             boxoffice_result[movie['movieCd']] = {
               '영화 대표코드': movie['movieCd'], 
                 '영화명' : movie['movieNm'], 
                 '누적관람객': movie['audiAcc']
             }
     ```
  
     
  
  5. 50주간의 데이터가 저장된`boxoffice_result`를 이용하여 `boxoffie.csv`를 만든다.
  
     ```python
   with open('boxoffice.csv', 'w', encoding='utf-8') as f:
         fieldnames = ['영화 대표코드', '영화명', '누적관람객'] # 여기만 생성
         csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
         csv_writer.writeheader()
         for item in boxoffice_result.values(): # 딕셔너리 만든 것 반복
             csv_writer.writerow(item)
     ```
  
  6. `boxoffice.csv`
  
     50주간의 영화 대표코드, 영화명, 누적관람객이 저장된다.



## 영화진흥위원회 오픈 API(영화 상세정보)

* 위에서 수집한 영화 대표코드를 이용하여 상세 정보를 수집합니다.

  1.`boxoffice.csv` 를 이용하여 데이터를 찾는다.

	```python
	with open('boxoffice.csv', 'r', encoding = 'utf-8') as 		f:
    	reader = csv.DictReader(f)
    	for row in reader:
        	movieCd = row['영화 대표코드']
        	api_url = 	f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
	        response = requests.get(api_url).json()
	```
	
* 결과

  ```python
  import requests
  from decouple import config
  import pprint
  import csv
  
  key = config('KEY')
  movie_detail = {}
  
  with open('boxoffice.csv', 'r', encoding = 'utf-8') as f:
      reader = csv.DictReader(f)
      for row in reader:
          movieCd = row['영화 대표코드']
          api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={movieCd}'
          response = requests.get(api_url).json()
          movie_info = response['movieInfoResult']['movieInfo']
  
          movie_detail[movie_info['movieCd']] = {
          '영화 대표코드': movie_info['movieCd'], 
          '영화명': movie_info['movieNm'], 
          '영화명(원문)': movie_info['movieNmEn'],
          '관람등급': movie_info['audits'][0]['watchGradeNm'] if movie_info['audits'] else None,
          '개봉연도': movie_info['openDt'],
          '장르': movie_info['genres'][0]['genreNm'],
          '감독명': movie_info['directors'][0]['peopleNm'] if  movie_info['directors'] else None
      }
  
  with open('movie.csv', 'w', encoding='utf-8') as f:
      fieldnames = ['영화 대표코드', '영화명', '영화명(원문)', '관람등급', '개봉연도', '장르', '감독명'] # 여기만 생성
      csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
      csv_writer.writeheader()
      for item in movie_detail.values(): # 딕셔너리 만든 것 반복
          csv_writer.writerow(item)
  ```

  

  1. 영화별로 영화 대표코드, 영화명(국문), 영화명(영문), 관람등급, 개봉연도, 상영시간, 장르, 감독명을 저장합니다.

     ```python
             movie_info = response['movieInfoResult']['movieInfo']
     
             movie_detail[movie_info['movieCd']] = {
             '영화 대표코드': movie_info['movieCd'], 
             '영화명': movie_info['movieNm'], 
             '영화명(원문)': movie_info['movieNmEn'],
             '관람등급': movie_info['audits'][0]['watchGradeNm'] if movie_info['audits'] else None,
             '개봉연도': movie_info['openDt'],
             '장르': movie_info['genres'][0]['genreNm'],
             '감독명': movie_info['directors'][0]['peopleNm'] if  movie_info['directors'] else None
         }
     ```

     01.py와 다르게 API의 구조가 일정한 형식으로 구조되지 않았기 때문에 하나씩 저장한다.

     관람등급과 감독명에는 비어있는 영화도 있기 때문에 예외처리를 해준다.

  2. 해당 결과를 `movie.csv`에 저장한다.

     ```python
     with open('movie.csv', 'w', encoding='utf-8') as f:
         fieldnames = ['영화 대표코드', '영화명', '영화명(원문)', '관람등급', '개봉연도', '장르', '감독명'] # 여기만 생성
         csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
         csv_writer.writeheader()
         for item in movie_detail.values(): # 딕셔너리 만든 것 반복
             csv_writer.writerow(item)
     ```

     * `movie.csv`은 `boxoffice.csv`의 영화 목록을 이용하여 영화대표코드, 영화명,  영화명(원문), 관람등급, 개봉연도, 장르, 감독명이 저장되어있다.

##  영화진흥위원회 오픈API(영화인 정보)

* 위에서 수집한 영화 감독정보를 활용하여 상세 정보를 수집한다.

  1. 영화인명으로 조회한다.

     ```python
     import requests
     from decouple import config
     import pprint
     import csv
     
     key = config('KEY')
     people = {}
     
     with open('movie.csv', 'r', encoding = 'utf-8') as f:
         reader = csv.DictReader(f)
         for row in reader:
             peopleNm = (row['감독명'],row['영화명'])
             api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={peopleNm[0]}'
             response = requests.get(api_url).json()
     ```

     `movie.csv`의 감독명과 영화명을 이용하여 URL를 요청한다.

* 결과

  ```python
  import requests
  from decouple import config
  import pprint
  import csv
  
  key = config('KEY')
  people = {}
  
  with open('movie.csv', 'r', encoding = 'utf-8') as f:
      reader = csv.DictReader(f)
      for row in reader:
          peopleNm = (row['감독명'],row['영화명'])
          api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={peopleNm[0]}'
          response = requests.get(api_url).json()
          people_info = response['peopleListResult']['peopleList']
          for info in people_info:
              if info['peopleNm'] == peopleNm[0] and   peopleNm[1] in info['filmoNames']:
                  people[info['peopleCd']] = {
                      '영화인 코드': info['peopleCd'],
                      '영화인 명': info['peopleNm'],
                      '분야' : info['repRoleNm'],
                      '필모리스트': info['filmoNames']
                  }
              
  with open('director.csv', 'w', encoding='utf-8') as f:
      fieldnames = ['영화인 코드', '영화인 명', '분야', '필모리스트'] # 여기만 생성
      csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
      csv_writer.writeheader()
      for item in people.values(): # 딕셔너리 만든 것 반복
          csv_writer.writerow(item)
  ```

  1. `peopleNm`은 튜플 형식으로 저장된다.

     ```python
         for row in reader:
             peopleNm = (row['감독명'],row['영화명'])
     ```

  2. 감독명과 영화명이 요청한 API에서 이름과 필모리스트가 같으면 저장한다.

     ```python
             for info in people_info:
                 if info['peopleNm'] == peopleNm[0] and   peopleNm[1] in info['filmoNames']:
                     people[info['peopleCd']] = {
                         '영화인 코드': info['peopleCd'],
                         '영화인 명': info['peopleNm'],
                         '분야' : info['repRoleNm'],
                         '필모리스트': info['filmoNames']
                     }
     ```

     

  3. 영화인별로 영화인 코드, 영화인명, 분야, 필모리스트를 저장한다.

     `director.csv` 에 위와 같은 내용을 저장한다.

     ```python
     with open('director.csv', 'w', encoding='utf-8') as f:
         fieldnames = ['영화인 코드', '영화인 명', '분야', '필모리스트'] # 여기만 생성
         csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
         csv_writer.writeheader()
         for item in people.values(): # 딕셔너리 만든 것 반복
             csv_writer.writerow(item)
     ```

     