with open('example.txt', 'w', encoding = 'utf-8') as f:
    f.write('예제 실행')
with open('example.txt', encoding = 'utf-8') as f:
    print(f.read())