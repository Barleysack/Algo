c=int(input())
b=[]
f=[]
for i in range(c):
  a = int(input())
  b=list(map(int,input().split()))

  for i in range(len(b)):
    if b[i]>=(sum(b)/a):
      f.append(b[i])
      
  d=(len(f)/len(b))*100
  print("%0.3f%%"%d)

n = int(input())
"""
for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함 (nums[0]: 학생수, nums[1:] 점수)
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생 수
    rate = cnt/nums[0] *100
    print(f'{rate:.3f}%')"""