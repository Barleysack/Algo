x=input()
s=str.upper(x)

스펠리스트=[]
빈도수 = []


for i in set(s):
  스펠리스트.append(i)

print(스펠리스트)

for 부분 in 스펠리스트:
  빈도 = 스펠리스트.count(부분)
  빈도수.append(빈도)



인덱스 = 빈도수.index(max(빈도수))


print(str.upper(스펠리스트[인덱스]))

#나는 두개 이상일 시 ?를 띄우는 로직을 생각해내지 못했다.
#도와줘요 서선생님.

words = input().lower()
words_list = list(set(words))
word_count = list()

for i in words_list:
    count = words.count(i)
    word_count.append(count)



