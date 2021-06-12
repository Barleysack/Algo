T=int(input())



answer=[]
for a in range(T):
    H,W,N= map(int,input().split())
    book=[]
    
    hosu = 0
    for i in range(1,W+1):

        for j in range(1,H+1):
            hosu = (j*100)+i
            book.append(hosu)

    answer.append(book[N-1])

for k in range(T):
    print(answer[k])





#굳굳
