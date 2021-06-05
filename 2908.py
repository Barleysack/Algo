"""상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는
상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 수 두 개를 칠판에 써주었다. 
그 다음에 크기가 큰 수를 말해보라고 했다.

상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 
437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오."""

a,b = map(str,input().split())
rev= 0
rev2=0
emp1 = []
emp2 = []
stringy = ""
string2 = ""
for i in a:
    emp1.append(i)
for j in b:
    emp2.append(j)

emp1.reverse()
emp2.reverse()


for k in emp1:
    stringy+=k
    
for l in emp2:
    string2+=l
    
inty1 = int(stringy)
inty2 = int(string2)

if inty1>inty2:
    print(inty1)
else:
    print(inty2)