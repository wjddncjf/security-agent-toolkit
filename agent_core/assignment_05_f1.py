# F1 : 숫자가 아닌 입력
# int로 바꿔 출력하되 ValueError가 나면 숫자가 아닙니다 출력합니다. 마지막 확인 끝은 항상 출력합니다

raw = 'abc'

try:
    number = int(raw)
    print(number)
except ValueError:
    print('숫자가 아닙니다')

print('확인 끝')