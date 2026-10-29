# 필수 F2 : 잘못된 한 건을 건너뛰기

# 각 값을 숫자로 바꾸어 더합니다. 숫자가 아닌 값은 건너뜀과 원래 값을 출력하고 다음 값으로 진행합니다.

values = ["2", "bad", "3"]
total = 0

for value in values:
    try:
        total = total + int(value)
    except ValueError:
        print("건너뜀", value)

print("합계", total)

# 문제 R1 : 무엇이 보일까요?
#아래 코드를 실행하면 화면에 무엇이 보일지 적어 보세요. 파일을 실행한 뒤 결과와 이유를 확인합니다.
# 숫자가 아닙니다 프로그램은 계속 돌아갑니다
try:
    n = int("abc")
    print(n)
except ValueError:
    print("숫자가 아닙니다")

print("프로그램은 계속 돌아갑니다")

# 문제 R2: 없는 칸을 꺼낼 때
# 주어진 값에서 네 번째 칸을 출력하시오. 칸이 없으면 대신 칸이 모자랍니다를 출력합니다

line = "09:41,guest"
parts = line.split(",")

try:
    print(parts[3])
except IndexError:
    print("칸이 모자랍니다")

print("확인 끝")
