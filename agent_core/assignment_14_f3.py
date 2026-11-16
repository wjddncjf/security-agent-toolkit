import re
import json

# 1. 브루트포스(Brute Force)
# 비밀번호 등 가능한 값을 반복적으로 입력해 인증을 시도하는 공격 방식이다.
# 로그인 로그에서 특정 계정의 인증 실패가 반복되면 의심할 수 있다.
# 단, 로그인 실패가 여러 번 발생했다고 반드시 공격인 것은 아니다.

# 2. 임계값(Threshold)
# 특정 행동을 비정상적이거나 의심스럽다고 판단하기 위해 정하는 기준값이다.
# 탐지 룰을 설계하는 사람이 로그 특성과 정상적인 사용 패턴을 고려해 설정한다.
# 예를 들어 임계값이 3이면 로그인 실패가 3회 이상인 계정에 경보를 발생시킨다.
# 임계값이 낮으면 탐지가 많아지지만 정상적인 행동도 경보로 처리될 수 있다.

PATTERN = r"(?P<time>[\d:]+) (?P<level>\w+) \w+ login for (?P<user>[\w.]+) from (?P<ip>[\d.]+)"

# 문제 4-1: 정규표현식에 맞지 않는 로그를 파일로 저장하기

unmatched = []

with open("raw_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        m = re.search(PATTERN, line)

        if not m:
            unmatched.append(line.strip())

with open("unmatched_logs.txt", "w", encoding="utf-8") as f:
    for line in unmatched:
        f.write(line + "\n")

print("안 맞음", len(unmatched), "건을 남겼습니다")

# 문제 4-3: 계정별 등장 횟수 세기

users = ["admin", "kim01", "admin"]

count = {}

for name in users:
    if name in count:
        count[name] = count[name] + 1
    else:
        count[name] = 1

print(count)

# 문제 4-4: 계정별 로그인 실패 횟수 세기

with open("normalized_logs.json", "r", encoding="utf-8") as f:
    rows = json.load(f)

count = {}

for row in rows:
    if row["level"] == "WARN":
        user = row["user"]

        if user in count:
            count[user] = count[user] + 1
        else:
            count[user] = 1

print(count)

# 문제 4-5: 로그인 실패가 3회 이상인 계정 탐지하기

THRESHOLD = 3

for user in count:
    if count[user] >= THRESHOLD:
        print("[룰 1] 확인 필요:", user, "— 실패", count[user], "회")