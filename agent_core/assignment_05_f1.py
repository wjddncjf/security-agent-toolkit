raw = 'abc'

try:
    number = int(raw)
    print(number)
except ValueError:
    print('숫자가 아닙니다')

print('확인 끝')