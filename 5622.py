s=input().lower()
new=0
ㄱ=['a','b','c']
ㄴ=['d','e','f']
ㄷ=['g','h','i']
ㄹ=['j','k','l']
ㅁ=['m','n','o']
ㅂ=['p','q','r','s']
ㅅ=['t','u','v']
ㅇ=['w','x','y','z']

total = [ㄱ,ㄴ,ㄷ,ㄹ,ㅁ,ㅂ,ㅅ,ㅇ]

for 글자 in s:
    for 세상에 in total:
        if 세상에.count(글자) >=1:
            new=total.index(세상에)+new+3
            
print(new)
        
    


