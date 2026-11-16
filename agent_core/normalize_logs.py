import re
import json

# 로그에서 시간, 등급, 계정, IP를 추출하는 정규표현식
PATTERN = r"(?P<time>[\d:]+) (?P<level>\w+) \w+ login for (?P<user>[\w.]+) from (?P<ip>[\d.]+)"


# 문제 4-2: 로그 한 줄을 딕셔너리로 변환하는 함수
def parse_raw_logs(line):
    m = re.search(PATTERN, line)

    if m:
        return m.groupdict()

    return None


# 정규화된 로그와 일치하지 않는 로그를 저장할 리스트
rows = []
unmatched = []

# 원본 로그 파일 읽기
with open("raw_logs.txt", "r", encoding="utf-8") as f:
    for line in f:
        row = parse_raw_logs(line)

        if row:
            rows.append(row)
        else:
            unmatched.append(line.strip())


# 정규화된 로그를 JSON 파일로 저장
with open("normalized_logs.json", "w", encoding="utf-8") as f:
    json.dump(rows, f, ensure_ascii=False, indent=2)


# 정규화되지 않은 로그를 텍스트 파일로 저장
with open("unmatched_logs.txt", "w", encoding="utf-8") as f:
    for line in unmatched:
        f.write(line + "\n")


print("정규화", len(rows), "건")
print("안 맞음", len(unmatched), "건")