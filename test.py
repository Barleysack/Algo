N = int(input())
f0 = [0 for x in range(1,10001)] #계수를 위한 배열을 생성한다.

f1 =[]
for _ in range(N):
    a=int(input())
    f1.append(a)

   
for i in f1:
    f0[i-1]=f0[i-1]+1

#계수 행렬 완성.

for k in range(len(f0)-1):
    f0[k+1]=f0[k]+f0[k+1]
#직전요소 더하기 완료
f0=f0[:max(f1)]


f2=[0 for x in range(len(f1))] 
#출력행렬 만들고

for p in range(1,len(f2)):
    f2[f0[f1[-p]]]=f0[f1[-p]]
    
    #f1의 마지막 부터 값을 계수행렬에서 f1의 
    #마지막 부터 값이 위치한 자리의 값을 리턴해 그를 출력행렬의 자리로 삼아 넣습니다.


print(f2)




