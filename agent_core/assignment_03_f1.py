# 5. 리스트 — 여러 값을 순서대로 담는다
# 리스트(list)는 값을 순서대로 줄 세워 담은 것이다. 계정이 서른 개면 변수를 서른 개 만들 수 없으니 한 이름에 담는다.

# 5.1 여러 값을 한 이름에 담고 싶을 때
# 대괄호로 감싸고 쉼표로 나눈다.

#이코드의목적-리스트를만들고번호로값을꺼낸다
#번호는0부터셉니다.
users =['Kim01', 'Lee02', 'Park03']
print(users[0]) # kim01
print(users[2]) # park03
print(len(users)) # 3

# IndexError: list index out of range, 마지막 번호는 2
# users = ["kim01", "lee02", "park03"]
# print (users [3])

# 5.2 값을 나중에 더하고 싶을 때
# 빈 리스트로 시작해 하나씩 붙인다.

# 이 코드의 목적 - 빈 리스트에 값을 하나씩 더한다.
# 점을 찍고 부르는 것을 메서드 라고합니다.
failed_users = [] # 빈 대괄호 = 빈 리스트
failed_users.append("kim01") # 뒤에 하나 붙인다
failed_users.append("lee02") 
print(failed_users) # ['kimø1', 'lee02']

# 2. 반복문 - 같은 일을 모든 값에 적용한다.
# 2.1 리스트를 처믕부터 끝까지 보고 싶을 때

users = ['kim01', 'lee02', 'park03'] # 확인한 계정 목록
for user in users: # 계정을 하나씩 꺼내 반복
    print(user)

# 2.4 정해진 횟수만큼 되풀이하고 싶을 때

for number in range(3):
    print(f'{number + 1}번째 점검')

# 예제 
users = ['choi04', 'han05']
for user in users:
    print(user)
