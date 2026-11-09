# 필수 F1 : CSV에서 실패 건수 집계
# 함께 받은 gichan_input.csv를 읽어 result가 FAIL인 기록의 개수를 출력합니다. 
# DictReader는 머리글을 키로 사용합니다.

import csv

fail_count = 0

with open('gichan_input.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row['result'] == 'FAIL':
            fail_count += 1

print(fail_count)

# 필수 F2 : JSON 결과 보고서
# JSON 입력을 읽어 전체·실패 건수를 summary.txt에 남깁니다. 
# 빈 목록으로 바꿨을 때도 확인합니다.

import json

with open('gichan_input.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

total_count = len(data)
fail_count = 0

for row in data:
    if row['result'] == 'FAIL':
        fail_count += 1

summary = f'전체 {total_count}건, 실패 {fail_count}건'

with open('summary.txt', 'w', encoding='utf-8') as file:
    file.write(summary)

print(summary)