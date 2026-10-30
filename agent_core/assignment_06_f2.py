# 필수 F2: 없는 파일 처리

try:
    with open('not-provided.txt', encoding='utf-8') as f:
        print(f.read())

except FileNotFoundError:
    print('파일 위치를 확인하세요')