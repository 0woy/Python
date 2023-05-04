# 리스트
numlist =[0,0,0,0]
hap =0

numlist[0] = int(input("숫자: "))
numlist[1] = int(input("숫자: "))
numlist[2] = int(input("숫자: "))
numlist[3] = int(input("숫자: "))

hap = numlist[0]+numlist[1]+numlist[2]+numlist[3]
print("합계 ==> ", hap);

# 리스트 추가 
numlist =[]
numlist.append(0)
numlist.append(0)
numlist.append(0)
numlist.append(0)
print(numlist)

# 오늘의 명언 출력하기 프로그램
import random
wiseSay=[
    "삶이 있는 한 희망은 있다",
    "언제나 현재에 집중할 수 있다면 행복할 것이다.",
    "피할 수 없으면 즐겨라",
    "신은 용기있는 자를 결코 버리지 않는다.",
    "행복한 삶을 살기위해 필요한 것은 거의 없다.",
    "내일은 내일의 태양이 뜬다.",
    "계단을 밟아야 계단 위에 올라설 수 있다.",
    "행복은 습관이다, 그것을 몸에 지니라",
    "1퍼센트의 가능성, 그것이 나의 길이다.",
    "작은 기회로 부터 종종 위대한 업적이 시작된다."
]

today = random.randint(0,len(wiseSay)-1)
print("오늘의 명언 ==>", wiseSay[today])

#리스트 값 변경하기 1,2,3
numlist =[10,20,30]
numlist[1]=200
print(numlist)

numlist=[10,20,30]
numlist[1:2] =[200,201]
print(numlist)

numlist=[10,20,30]
numlist[1] =[200,201]
print(numlist)

# 리스트 값 삽입하기
numlist=[10,20,30]
numlist.insert(1,123)
print(numlist)

# 리스트 값 삭제하기
numlist=[10,20,30]
del(numlist[1])
print(numlist)

# 리스트 값 삭제하기2
numlist=[10,20,30]
del(numlist)
print(numlist)

# 리스트 값 삭제하기3
numlist=[10,20,30]
numlist.remove(10)
print(numlist)

numlist=[10,20,30,10,10]
numlist.remove(10)
print(numlist)

# 리스트 값 추출하기
numlist=[10,20,30]
numlist.pop()
print(numlist)

# 리스트 특정 값 개수 세시
numlist=[10,20,30,10,10]
print(numlist.count(10))

#리스트 값 정렬하기
numlist = [20,10,40,50,30]
numlist.sort()
print(numlist)
numlist = [20,10,40,50,30]
numlist.sort(reverse=True)
print(numlist)


# 도서관 예약 확인 프로그램
library = [[0,0,1,0],[1,0,1,1],[0,1,0,0],[1,1,0,1]]

for i in range(0,4):
    for j in range(0,4):
        print(" ",library[i][j],end="")
    print(" ")

row = int(input("행 입력(0~3):"))
column = int(input("열 입력(0~3):"))

if(library[row][column] == 1):
    print("해당 자리는 예약되어 있습니다.")
else:
    print("해당 자리는 예약되어 있지 않습니다.")

#심사위원 점수 결과 출력
print("홍길동 선수 경기 끝났습니다~~ 짝짝")
score=[]
for i in range(5):
    num = int(input("평가 점수==>"))
    score.append(num)

sum =0
for i in score:
    sum=sum+i

print("심사위원 평균 점수: ",sum/len(score))

