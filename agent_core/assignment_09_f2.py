# 필수 F2 · 판단을 함수로 묶기

# 이런 상황이 있습니다

# 담당자가 작은 학습용 기록을 확인하고 결과를 남기려 합니다. 이 문제는 그 처리의 핵심을 연습합니다.

# 할 일

# 실패 횟수를 받아 판단을 반환합니다. 2와 3을 각각 넣어 경계를 확인합니다.

def count_failed(count):
    if count >= 3:
        return '추가 확인'
    else:
        return '기록 유지'

print(count_failed(2))
print(count_failed(3))


