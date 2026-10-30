# 6. 파일 : 코드 밖의 글자를 읽고 쓴다.

# 6.1 : 파일에 글자를 쓰고 싶을 때

with open('memo.txt', 'w', encoding = 'utf-8') as f: # 쓰기 모드로 열고 f라고 부른다
    f.write('첫 번째 줄\n') # \n은 줄바꿈 문자
    f.write('두 번째 줄\n')

print('memo.txt 를 만들었습니다')

# encoding="utf-8"은 한글이 깨지지 않게 하는 설정입니다. 파일을 열 때마다 붙입니다.
# write()는 줄을 알아서 바꾸지 않습니다. 줄 끝마다 \n을 붙여야 다음 줄로 넘어갑니다.

# 6.2 : 파일 전체를 읽고 싶을 때

with open('memo.txt', encoding = 'utf-8') as f: # 모드를 안 쓰면 읽기
    print(f.read())

# 6.3 한 줄씩 읽고 싶을 때

# 오늘 사용할 로그 파일을 만듭니다.
lines = [
    "09:01, kim01, 10.0.3.21, LOGIN, FAIL",
    "09:03, lee02, 10.0.7.5, LOGIN, OK",
    "09:05, kim01, 10.0.3.21, LOGIN, FAIL",
    "09:08, park03, 10.0.9.8, FILE_OPEN, OK",
    "09:11, kim01, 10.0.3.21, LOGIN, FAIL",
    "09:14, park03, 10.0.9.8, LOGIN, FAIL",
]

with open('sample_logs.csv', 'w', encoding = 'utf-8') as f:
    for line in lines:
        f.write(f'{line}\n')

print('sample_logs.csv를 만들었습니다')

# for line in f는 파일에서 한 줄씩 꺼냅니다.
# strip()은 글자 양쪽의 빈칸과 줄바꿈을 지웁니다.
with open('sample_logs.csv', encoding = 'utf-8') as f:
    for line in f: # 한 줄씩 꺼내 line에 담는다
        print(line.strip())

# 6.4 특정 글자가 든 줄만 고르고 싶을 때

print('FAIL' in '09:01,kim01,10.0.0.21.LOGIN,FAIL') # True
print('FAIL' in '09:03,lee02,10.0.7.5,LOGIN,OK') # False

with open('sample_logs.csv', encoding = 'utf-8') as f:
    for line in f:
        if 'park03' in line: # park03이 들어 있는 줄만
            print(line.strip())

# 6.5 기존 파일 뒤에 이어서 쓰고 싶을 때
# 'a'는 덧붙이기(append) 모드입니다. 원래 내용을 두고 맨 뒤에 씁니다.

with open('memo.txt', 'a', encoding = 'utf-8') as f:
    f.write('세 번째 줄\n')

with open('memo.txt', encoding = 'utf-8') as f:
    print(f.read())

# 필수 F1 : 결과 파일 쓰고 다시 읽기

with open('check.txt', 'w', encoding = 'utf-8') as f:
    f.write('점검시작\n')
    f.write('점검 끝\n')

with open('check.txt', encoding = 'utf-8') as f:
    print(f.read())