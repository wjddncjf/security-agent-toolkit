counts = [0, 4, 2, 5]
selected = 0
total = 0
for count in counts:
    if count >= 3:
        selected = selected + 1
        total = total + count
print(selected, total)

# 0->7로 변경
# 예상 출력 : 3 16
counts = [7, 4, 2, 5]
selected = 0
total = 0
for count in counts:
    if count >= 3:
        selected = selected + 1
        total = total + count
print(selected, total)

# 문제 R1. 계정 모두 출력하기

users = ['Kim01', 'Lee02', 'Park03']
for user in users:
    print(user)