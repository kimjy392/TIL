import requests
key = '2961dcb2e4336ffa43975ece6fdaec32'
targetDt = '20190713' # yyyymmdd
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'
print(api_url)
response = requests.get(api_url).json()
print(response)


# 1. 영화 정보를 불러온다. 
# 영화 정보를 어떻게 저장할것인가
# set에 딕셔너리 형태로 저장해야한다.
# 계속 추가할 수 있도록 해야한다.
# 추가하다가 새로운 영화가 나온다면 누적관객수를 저장하고 그 이후에는 보지 않는다.
# 

c = {}
c.update({'사과' : 1})
print(c)
