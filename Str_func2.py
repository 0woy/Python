# count(): 문자열에서 어떤 글자가 몇 번 등장하는지 확인
ss ="난생처음 파이썬을 처음으로 학습 중입니다 파이썬을 처음 공부하지만 재미나네요"
sd ="난생처음을 공부하는 게 처음이네요"
print(ss.count("처음"));

# find(): 어떤 글자가 문자열의 몇 번째에 위치하는지 찾음
# 똑같은 문자가 여러개 나올 때 위치 찾기 : find("찾을 단어", "시작 위치")
ss ="난생처음 Python"
print(ss.find("난생"))
print(ss.find("P"))
print(sd.find("처음",4))