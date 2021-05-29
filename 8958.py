a = int(input())
for i in range(a):
    b = input() #한글자
    s = list(b)#for 안에서 이렇게 해도 되는건가..?
    sum = 0
    c = 1
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)#한 테스트 케이스 끝에 sum 출력