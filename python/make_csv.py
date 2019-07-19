students = {
    'asdf1': {
        '순번': '01',
        '이름': '김성훈'
    },

    'asdf2':{
        '순번': '02',
        '이름': '김은정'
    } 
}

students2 = [
    {
        '순번': '03',
        '이름': '김준영'
    },

    {
        '순번': '04',
        '이름': '양혜진'
    } 
]

# with open('a.txt','w', encoding = 'utf-8') as f:
#     f.write('number, name\n')
#     for number, name in student.items():
#         f.write(f'{number}, {name}\n')

import csv

with open('b.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['순번', '이름'] # 여기만 생성
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in students2: # 딕셔너리 만든 것 반복
        csv_writer.writerow(item)
