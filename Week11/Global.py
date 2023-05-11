# 글로벌 예약어
def func1():
    global a
    a=10
    print("func1()에서 a의 값",a)

def func2():
    print("func2()에서 a의 값",a)
a=20
func1()
func2()

# 100일 기념일 날짜 구하기
from datetime import datetime, timedelta
def getCurrent():
    cDate = datetime.now()
    return cDate

def getAfter(now, day):
    rDate = now +timedelta(days=day)
    return rDate

nowDate, afterDate = None,None
nowDate = getCurrent()
print("햔재 날짜와 시간 ==>",nowDate)
afterDate = getAfter(nowDate, 100)
print("100일 후 날짜와 시간 ==>", afterDate)

# 비밀번호 생성하기
"""
입력한 비밀번호가 비밀번호 규칙에 맞으면 생성, 맞지 않으면 다시 생성
1. 8글자 이상
2. 영문자 및 숫자로만 생성해야 하며 기호는 불가능
"""
pword =""
def checkPassword(pwd):
    if len(pwd) <8: return False
    if pwd.isalnum(): return True
    else: return False

while True:
    pword = input("새로운 비밀번호를 입력하세요: ")
    if checkPassword(pword):
        print("Good~ 비밀번호가 올바르게 생성되었어요")
        break
    else:
        print("오류! 비밀번호가 규칙에 맞지 않습니다.")
    