def func2():    # 함수 정의 
    result =100
    return result

hap =0          # 전역변수 선언

hap = func2()   # 메인 코드
print("func2()에서 돌려준 값 ==>", hap)

#반환 값이 2개 있는 함수
def func3():
    result1 = 100
    result2 = 200
    return result1,result2
hap1, hap2 =0,0

hap1, hap2 =func3()
print("func3()에서 돌려준 값 ==>", hap1,hap2)

# 반환 값이 없는 함수
def func1():
    print("반환 값이 없는 함수 실행")

func1()

# 로또 추첨 하기
import random
lotto = []
num=0
def lottoFunc():
    lottoNum = random.randint(1,45)
    return lottoNum

print("** 로또 추첨을 시작합니다. **")
while True:
    num = lottoFunc()
    if num in lotto:   continue
    else:   lotto.append(num)
    if len(lotto) ==6: break
lotto.sort()
print("오늘의 로또 번호 ==> ", end="")
for i in lotto: print(i," ", end="")


