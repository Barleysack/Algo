a,b,v = map(int,input().split())
k = (v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)
#부등식의 계산은 시간을 늘린다.
#먼저 손으로 식을 써보고, 간단히 하ㅏ는 것을 목표로 하자.