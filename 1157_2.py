x=input()
s=str.upper(x)

스펠리스트=[]
빈도수 = []


for i in s:
  스펠리스트.append(i)


for 부분 in 스펠리스트:
  빈도 = 스펠리스트.count(부분)
  빈도수.append(빈도)

print(빈도수)

인덱스 = 빈도수.index(max(빈도수))
print(인덱스)

print(str.upper(스펠리스트[인덱스]))

#나는 두개 이상일 시 ?를 띄우는 로직을 생각해내지 못했다.
#도와줘요 서선생님.


