a = int(input())
b= int(input())
mr = b-1
count = 0
Fanswer=[]

    #1978을 재활용하자. 


for p in range(a,b):
    if p== 2:
        count= count +1
        continue

   
    for i in range(2,p):
       
        if p%i ==0:
            break;
        #자신을 나누는 놈이 나타나면 이번 수는 틀려먹었으니 패스...
        if i == p-1:
            Fanswer.append(p)
            count= count+1
            #끝까지 잘 갔다면 +1


Fanswer_fin = sum(Fanswer)

if count == 0:
    Fanswer_fin=-1
    
    print(Fanswer_fin)
if count !=0:
    print(Fanswer_fin)
    Sanswer=min(Fanswer)
    print(Sanswer)
    

