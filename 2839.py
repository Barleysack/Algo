N = int(input())
count = 0
manil = -1

count = N//5

latermock = (N-(5*count))//3
if latermock <3 and latermock >0:
    print(-1)
if latermock == 0:
    latermock = 1
    
count = count + latermock

print(count)


        
