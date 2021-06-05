A,B,V=map(int,input().split())
간거리 = 0
날짜=1
while True:
    
    if 간거리<V:
        간거리=간거리+A
    if 간거리<V:
        간거리=간거리-B
        날짜=날짜+1
    else:
        break;

    

print(날짜)