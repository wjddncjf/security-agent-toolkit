# 기존 처리를 함수로 나누기

# 5.4 : 값을 안 넘기면 정해 둔 값을 쓰고 싶을 때
# 매개변수에 =값을 붙이면 기본값이 됩니다. 넘기지 않으면 기본값을, 넘기면 넘긴 값을 씁니다.

def needs_review(count, threshold=2): # threshold를 안넘기면 2
    return count >= threshold

print(needs_review(3))      # 기본값 2와 비교 -> True
print(needs_review(3,5))    # 넘긴 값 5와 비교 -> False

# 5.5 : 코드를 통째로 함수에 넣을 때

from collections import Counter # 항목별 횟수를 세는 도구

def find_suspects(failed_users, threshold=2):
    counts = Counter(failed_users)
    suspects = []
    for user, count in counts.items():
        if count >= threshold:
            suspects.append(user)

    return suspects

print(find_suspects(['kim01', 'kim01', 'lee02', 'kim01']))
print(find_suspects(['kim01', 'kim01', 'lee02', 'kim01'], 5)) # 기준을 바꿔 다시 확인

# F1 : 모으는 함수
# 3 이상인 값의 새 목록을 반환합니다. 빈 목록을 받으면 빈 목록을 반환하는지도 확인합니다.

def filter_three_or_more(values):
    result = []
    for value in values:
        if value >= 3:
            result.append(value)
    return result


print(filter_three_or_more([1, 2, 4, 5]))   # [4, 5]
print(filter_three_or_more([]))             # []