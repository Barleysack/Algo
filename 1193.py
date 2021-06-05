n = int(input())
know= 1
kwall = 1
kbefore = 1
bj = 1
bm = 1
smalllist=[]
while kwall<=n:
    
    know=know+1
    kwall=((know+1)*(know))/2
    

#x번째 집합까지 구해내는데 성공. 

if know%2 == 0:
    for i in range(1,know+1):
        bj=i
        bm=know+1-i
        wonso = bj/bm
        smalllist.append(wonso)
        
else:
    for i in range(1,know+1):
        bj=i
        bm=know+1-i
        bj=str(bj)
        bm=str(bm)
        wonso = bj+"/"+bm
        smalllist.append(wonso)
        
    smalllist.reverse()
#해당 집합을 만들어냈음.
#n 빼기 이전 know를 인덱스로 가지고 스몰리스트를 뽑으면 되겠지?
이전거 = ((know)*(know-1))/2
인덱스 = int(n-이전거)
print(smalllist[인덱스-1])

#ㅋㅋㅋㅋㅋ아니 세상에 그냥 줄과 위치로 나타내는거네 ㅋㅋㅋ
#틀렸지만 배운게 많은 문제. ..
#언제나 가장 쉬운 방법을 찾도록 해보자 ㅠㅠ 
#댕-청...
