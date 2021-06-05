"""그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오."""
#입력받아 드르륵해서 현재 위치 +1 이외에 발견되면 해당 라운드의 count는 그대로?
#이건 헛점이 많은 로직이다. 
#
#정답: 슬라이싱을 이용하는 것이 좋은 생각이었다. 
n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:  
        group_word += 1  # error가 0이면 그룹단어
print(group_word)

for whatever in range(n):
  word = input()
  count = 0
  error = 0
  for i in range(len(word)-1):
    if word[index]!= word[index+1]: # 앞에서 range-1을 해둔 덕에, index가 튈 일은 없다.
      new_word = word[index:]
      if new_word.count(word[index])>0:
        error = error +1 
  if error == 0:
    count = count +1
print(count)