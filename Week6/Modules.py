# 난수 모듈: random
# import random
# random.randrange(10):0-9사이 난수 출력
# random.randint(0,9): 0-9사이 난수 출력
# random.choice([여러값]): 여러 값 중 하나 출력

#동전 던지기 게임1
# 사용자가 동전 앞/뒤 선택, 컴퓨터 랜덤 동전던지기. 값이 같으면 WIN
import random
print("동전 던지기 게임을 시작합니다.")
user = input("동전 앞뒤를 선택하세요. (앞/뒤) =>")
com = random.choice(["앞","뒤"])
if(com == user): 
    print("컴퓨터의 동전은",com,"면으로 정답입니다.")
else: 
    print("컴퓨터의 동전은",com,"면으로 오답입니다.")

# 동전 던지기 게임2
#앞/뒤가 아닌 다른 값을 입력 시 다시 반복
import random
print("동전 던지기 게임을 시작합니다.")
while True:
    user = input("동전 앞뒤를 선택하세요. (앞/뒤) => ")
    if(user=="앞" or user=="뒤"):
        com = random.choice(["앞","뒤"])
        if(com == user): 
            print("컴퓨터의 동전은",com,"으로 정답입니다.")
        else: 
            print("컴퓨터의 동전은",com,"으로 오답입니다.")
        print("게임을 종료합니다.")
        break;
    else: print("앞 / 뒤 중 하나를 선택하세요."); continue

# 가위 바위 보 게임
"""
사용자가 가위/바위/보 선택
컴퓨터가 가위/바위/보 선택
사용자가 컴퓨터를 이기는 게임
가위/ 바위/ 보 외의 값을 입력시 1번부터 다시 반복
"""
import random
check = -1
user = input("나의 가위/바위/보==> ")
com = random.choice(["가위","바위","보"])

print("컴퓨터의 가위/바위/보 ==> ", com)
if(user==com):
    print("비겼습니다.")
elif(user =="가위"):
    if(com =="바위"): check=0
    else: check =1   
elif(user=="바위"):
    if(com =="보"): check=0
    else: check =1
else:
    if(com=="가위"): check=0
    else: check=1
if(check==1): print("이겼습니다^^")
elif(check==0): print("졌습니다ㅠㅠ")
            
