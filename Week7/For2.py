#글자 수 세기 프로그램: 짝/쩍으로 구성된 문자열에서 글자 수 개수 세기
str = "짝짝쩍쩍짝쩍짝짝쩍쩍짝쩍짝"
n = input("찾으시는 글자는 무엇인가요?(짝/쩍) ")
count =0
for i in str:
    if(n==i):
        count+=1
    else: 
        continue
print("찾으시는 글자는 ",count,"개 입니다.")

#숫자 비교 프로그램: 7개의 정수를 입력 받아 크기 비교, 가장 큰 수 반환
numList = []
max = 0
for i in range(7):
    print(i+1,"번째 숫자 입력: ", end="")
    numList.append(int(input()))
    if(max < numList[i]): max = numList[i]
print("가장 큰 수는 ", max,"입니다.")

#소수 판단 프로그램
check = False
num = int(input("정수 입력: "))
for i in range(2,int(num/2+1)):
    if(num % i == 0): 
        print(num,"은 소수가 아닙니다.")
        break;
    else: 
        check = True
if(check): print(num,"은 소수입니다.")

#구구단 프로그램 2
for i in range(2,10):
    print(i,"단")
    for j in range(1,10):
        print(i,"X",j,"=",i*j)
    print("\n")

#별 찍기 프로그램
n = int(input("별 최대 개수: "))
for i in range(1,n+1,2):
    blank=" "*((n-i)//2)
    star ="*"*i
    print(blank+star)
for i in range(n-2,0,-2):
    blank=" "*((n-i)//2)
    star ="*"*i
    print(blank+star)
    
    
    