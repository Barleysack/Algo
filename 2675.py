t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)
               
               #텍스트를 담을 그릇이 필요하다...!
               #쌓아올리는 상황이라면...!