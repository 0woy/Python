# For문의 형식
# for 변수 in range(시작값, 끝값+1,증가값):
#     반복한 문장
# range(0,3,1): 0에서 시작해서 2까지 1씩 증가하는 값들을 반환
# 증가값을 생략할 경우 1로 인식
# 따라서 range(0,3,1) == range(0,3)
# 시작값은 0이므로 시작값도 생략가능
# 즉, range(0,3,1) == range(0,3) == range(3)

# range() 함수를 이용해 10부터 1까지 반복
for i in range(10,0,-1):
    print(i,end=" ")


# 리스트: 여러개의 변수를 사용하고 싶은 경우
# 4개의 정수형 변수 선언 및 합계 출력 with List

numList = []
sum =0
for i in range(4):
    num = int(input("숫자: "))
    numList.append(num)
for i in (numList):
    sum+=i
print("합계 ==> ", sum)

# 학생 줄 세우기
sum =1
for i in range(5,0,-1):
    sum*=i;
print("A,B,C,D,E 학생들을 순서대로 세우는 경우의 수: ", sum)


#For문을 활용한 반복 덧셈1, 1000~2000 사이 홀수 합
sum =0
for i in range(1000,2001):
    if(i%2!=0): sum+=i
    else: continue
print("1000에서 2000까지 홀수의 합:", sum)

#구구단 프로그램: 값을 입력하여 해당 값의 구구단 출력
a = int(input("몇 단을 출력할까요?: "))
for i in range(1,10):
    print(a," X ",i," = ", a*i)

#글자 수 세기 프로그램: 짝/쩍으로 구성된 문자열에서 글자 수 개수 세기


#숫자 비교 프로그램: 7개의 정수를 입력 받아 크기 비교, 가장 큰 수 반환
numList = []
max = 0
for i in range(7):
    print(i+1,"번째 숫자 입력: ", end="")
    numList.append(int(input()))
    if(max < numList[i]): max = numList[i]
print("가장 큰 수는 ", max,"입니다.")

