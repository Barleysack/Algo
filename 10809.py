word = input()
alphabet = list(range(97,123))

for item in alphabet:
  print(word.find(chr(item)))
  

  #chr과 ord를 기억합시다. 
  #chr는 아스키코드를 받아 문자를 알려준다. 
  #ord는 문자를 받아 아스키코드값을 찾아준다
