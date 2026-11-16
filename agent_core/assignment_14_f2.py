import re

# 1. 비정형 로그
# 정형 데이터(CSV)는 쉼표 등으로 값이 구분되고 각 열의 의미가 일정하다.
# 반면 비정형 로그는 기록마다 문장 구조와 값의 위치가 달라질 수 있다.
# 따라서 split()으로 나눈 뒤 고정된 인덱스로 값을 추출하면
# 로그 형식에 따라 잘못된 값을 가져올 수 있다.

# 2. 정규표현식
# 문자열에서 특정 위치가 아닌 글자의 형태와 규칙을 기준으로 값을 찾는 방법이다.
# 예를 들어 IP 주소가 몇 번째 칸에 있는지 지정하는 대신,
# 'from' 뒤에 숫자와 점이 이어지는 형태를 검색해 IP를 추출할 수 있다.
# 따라서 값의 위치가 달라져도 패턴에 일치하면 원하는 값을 찾을 수 있다.

# 3. 그룹(Group)
# 정규표현식에서 추출하고 싶은 부분을 괄호 ()로 묶는 기능이다.
# 전체 검색 결과 중 괄호로 묶은 부분만 따로 가져올 수 있다.
# group(1), group(2)처럼 괄호의 순서에 따라 값을 추출한다.

# 4. 네임드 그룹(Named Group)
# 정규표현식의 그룹에 이름을 붙여 원하는 값을 추출하는 기능이다.
# (?P<user>...)처럼 이름을 지정하고 group("user")로 값을 가져온다.
# groupdict()를 사용하면 그룹 이름과 값을 딕셔너리로 변환할 수 있다.
# 번호 대신 이름으로 구분하므로 여러 값을 추출할 때 이해하기 쉽다.

# 문제 3-1: 정규표현식으로 로그에서 IP 주소 찾기
line = "2026-09-29 09:12:00 WARN failed login for kim01 from 203.0.113.5"

m = re.search(r"from [\d.]+", line)
print(m.group())


# 문제 3-2: 정규표현식으로 로그에서 계정 이름 찾기
line = "2026-09-29 09:12:00 WARN failed login for kim.cs from 203.0.113.5"

m = re.search(r"for [\w.]+", line)
print(m.group())

# 문제 3-3: raw_logs.txt 파일 전체에서 IP 주소 찾기

with open("raw_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        ips = re.findall(r"from [\d.]+", line)
        print(ips)

# 문제 3-4: 이름 붙인 그룹에서 IP 주소 추출하기

line = "2026-09-29 09:12:00 WARN failed login for kim01 from 203.0.113.5"

PATTERN = r"(?P<time>[\d:]+) (?P<level>\w+) \w+ login for (?P<user>[\w.]+) from (?P<ip>[\d.]+)"
m = re.search(PATTERN, line)
print(m.group("ip"))

# 문제 3-5: 로그에서 시간, 등급, 계정, IP를 딕셔너리로 추출하기

line = "2026-09-29 09:12:00 WARN failed login for kim01 from 203.0.113.5"

PATTERN = r"(?P<time>[\d:]+) (?P<level>\w+) \w+ login for (?P<user>[\w.]+) from (?P<ip>[\d.]+)"
m = re.search(PATTERN, line)
print(m.groupdict())

# 문제 3-6: raw_logs.txt에서 정규표현식에 맞는 로그를 딕셔너리 리스트로 만들기

rows = []

with open("raw_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        m = re.search(PATTERN, line)

        if m:
            rows.append(m.groupdict())

print("정규화", len(rows), "건")

# 문제 3-7: 정규화된 로그에서 계정별 등장 횟수 세기

count = {}

for row in rows:
    user = row["user"]

    if user in count:
        count[user] = count[user] + 1
    else:
        count[user] = 1

print(count)
print("전체 로그:", sum(count.values()), "건")