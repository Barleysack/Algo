N = int(input())
count = 0
a = map(int,input().split())

    #자신보다 작은 것으로 나누어 1 이외에 아무것도 나뉘지 않는다면 집계.
for k in a:
    if k == 2:
        count = count +1
        continue
    
    for i in range(2,k):
       
        if k%i ==0:
            break;
        #자신을 나누는 놈이 나타나면 이번 a는 틀려먹었으니 패스...
        if i == k-1:
            count= count+1
            #끝까지 잘 갔다면 +1
print(count)