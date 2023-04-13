# 무한루프 숫자 더하기
while True:
    n1 = int(input("숫자1 ==> "))
    if(n1==0): 
        print("0을 입력해서 계산을 종료합니다.")
        break;
    n2 = int(input("숫자2 ==> "))
    print(n1,"+",n2,"=",n1+n2)

#1~100까지 더하되 4의 배수는 더하지 않음
i=0
sum =0
while(i<100):
    i+=1
    if(i%4==0): continue
    else: sum+=i
print("1~100의 합계(4의 배수 제외):", sum) 

# 주사위 3개를 동시에 던져 모두 동일한 숫자가 나오면 반복문 탈출
# 난수, while, if 사용
import random
count = 0

while True:
    count+=1
    dice = []
    for i in range(3):
        dice.append(random.randrange(1,7))
    if(dice[0]!=dice[1] or dice[1]!=dice[2]):
       continue;
    else:
        print("3개 주사위는 모두",dice[0],"입니다.")
        print("같은 숫자가 나오기까지",count,"번 던졌습니다.")
        break;

# 숫자 맞추기 게임
import random
print("숫자 맞추기 게임을 시작합니다.\n1부터 100사이의 숫자를 맞춰보세요.")
print("10번의 기회가 주어집니다.\n")
com = random.randrange(1,101)

i=1
while(i<=10):
    print("기회",i,end="")
    user = int(input("- 예상 숫자를 입력하세요: "))
    if(user < com): print("그것보다 큰 숫자를 선택하세요")
    elif(user > com): print("그것보다 작은 숫자를 선택하세요")
    else:
        print("정답입니다!", i,"번 만에 맞췄습니다.")
        break;
    i+=1
if(i>10):
    print("10번의 기회가 모두 끝났습니다. 정답은",com,"입니다.")