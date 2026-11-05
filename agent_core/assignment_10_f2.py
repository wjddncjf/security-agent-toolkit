# F2 : 함수 결과를 파일에
# 합계를 문장으로 반환하는 summarize를 만들고 반환값을 report.txt에 저장합니다.

def summarize(numbers):
    total = sum(numbers)
    return f'합계 {total}'

result = summarize([2,3])
print(result)

with open('report.txt', 'w') as f:
    f.write(result)