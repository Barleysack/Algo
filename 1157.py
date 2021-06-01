s = input()
templist = []
secondtemp=[]
x="a b c d e f g h i j k l m n o p q r s t u v w x y z"
for i in s:
  templist.append(i)

print(templist)

#이제 templist는 각 단어의  알파벳 리스트.
for j in x:
  secondtemp=templist.count(j)
  #이제 secondtemp는 각 알파벳의 숫자를 센 리스트.

print(secondtemp)

for k in x:
  if  int(max(secondtemp)) == templist.count(k):
    print(k)
  else:
    pass

    


