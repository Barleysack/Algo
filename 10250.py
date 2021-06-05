T=int(input())

hosu = 0
book = []
answer=[]
for a in range(T):
    H,W,N= map(int,input().split())
    for i in range(1,W+1):

        for j in range(1,H+1):
            hosu = (j*100)+i
            book.append(hosu)

    answer.append(book[N-1])

print(answer)

#서석현님께 여쭤보자
