# 6.1 : 이름으로 값을 꺼내고 싶을 때

# 이 코드의 목적 - 딕셔너리를 만들고 키로 값을 꺼낸다.
# 키는 이름표, 값은 그 안에 든 내용입니다.

user = {'name': 'kim01', 'dept': 'finance', 'level': 'read'}
print(user['name']) # kim01
print(user['dept']) # finance

# 6.2 값을 바꾸거나 새로 넣고 싶을 때

# 이 코드의 목적 - 딕셔너리의 값을 바꾸고 새 키를 추가한다
# 이 모양이 10월 접근통제 과목의 승인 처리 코드가 됩니다.

user = {'name': 'kim01', 'level': 'read'}
user['level'] = 'admin'         # 있는 키 -> 값이 바뀐다
user['approver'] = 'hr_mgr'     # 없는 키 -> 새로 생긴다
print(user)

# 6.3 로그 한 줄을 딕셔너리 하나로 옮긴다
# 칸 이름이 키가 되고, 칸 내용이 값이 됩니다.

# 2026-09-22 14:03:11 kim01 10.0.3.21 LOGIN FAIL
log = {
    'time': '2026-09-22 14:03:11',
    'user': 'kim01',
    'ip': '10.0.3.21',
    'action': 'LOGIN',
    'result': 'FAIL'
}
print(log['user'], log['result'])

# 7. get() - 없는 키를 물어도 멈추지 않는다
log = {'user': 'kim01'}
print(log.get('ip'))

# 7.1 키가 있는지 먼저 확인하고 싶을 때

# 이 코드의 목적 - 딕셔너리에 그 키가 있는지 in으로 확인한다
# 있으면 True, 없으면 False가 나옵니다.

log = {'user': 'kim01', 'result': 'FAIL'} # ip가 없다
print('user' in log) # True
print('ip' in log) # False

# 7.2 멈추지 않게 하고 싶을 때

# 이 코드의 목적 - .get()이 없는 키를 물어도 멈추지 않는 것을 확인한다
# 맨 아래 검사 완료가 찍히는지 보세요. 아까와 다릅니다.

log = {'user': 'kim01', 'result': 'FAIL'}
print(log.get('ip'))            # None = 값이 없다는 뜻
print(log.get('ip', '알 수 없음')) # 두 번째 칸 = 없을 때 대신 쓸 값
print('검사 완료')                 # 이번엔 실행된다.

# 7.3 상황에 맞게 갈라 쓰고 싶을 때

# 이 코드의 목적 - 대괄호와 .get()을 상황에 맞게 갈라 쓴다.
# user는 없으면 문제다 -> 대괄호. ip는 없을 수 있다. -> .get()

log = {'user': 'kim01', 'result': 'FAIL'}
print(f'계정 {log['user']} * IP {log.get('ip', '-')} * 결과 {log['result']}')

# 5.1 리스트 안의 닥셔너리 

books = [ 
    {'title': '파이썬', 'price': 20000},
    {'title': '네트워크', 'price': 25000},
]

print(books[0])          # {'title': '파이썬', 'price': 20000}
print(books[0]['title']) # 파이썬
print(books[1]['price']) # 25000

# 5.2 딕셔너리 안의 딕셔너리

stores = {
    'seoul': {'count': 12, 'open': True},
    'busan': {'count': 5, 'open': False},
}

print(stores['seoul'])          # {'count': 12, 'open': True}
print(stores['seoul']['count']) # 12
stores['daegu'] = {'count': 3, 'open': True} # 새 칸을 만든다

# 6.1 dumps와 loads - 글자로 바꾼다

import json

menu = {'name': 'coffee', 'price': 4500}

text = json.dumps(menu) # 딕셔너리 -> 글자
print(text)             # {'name': 'coffee', 'price': 4500}

back = json.loads(text) # 글자 -> 딕셔너리
print(back['price'])    # 4500

# 6.2 dump와 load - 파일로 남긴다

import json

menu = {'name': 'coffee', 'price': 4500}

with open('menu.json', 'w', encoding='utf-8') as f:
    json.dump(menu, f, ensure_ascii=False, indent=2)

with open('menu.json', encoding='utf-8') as f:
    back = json.load(f)

print(back['name'])     # coffee

# 필수 F1 : 이름으로 값 찾기

log = {'user': 'kim01', 'count': 4}

print(log['user'], log['count'])