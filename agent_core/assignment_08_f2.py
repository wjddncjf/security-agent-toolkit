# 필수 F2: JSON 저장과 복원

import json

logs = [
    {"user": "kim01", "count": 4},
    {"user": "lee02", "count": 1}
]
with open('logs.json', 'w', encoding='utf-8') as f:
    json.dump(logs, f, ensure_ascii=False, indent=2)

with open('logs.json', 'r', encoding='utf-8') as f:
    back = json.load(f)

print(back[0]['user'])