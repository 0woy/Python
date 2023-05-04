# 사용자 정의 함수가 필요한 이유
def hapFunc():
    num1 = int(input("정수1==>"))
    num2 = int(input("정수2==>"))
    return num1+num2    

for i in ['A','B','C']:
    print(i,"님, 두 숫자를 입력하세요")
    hap = hapFunc()
    print("결과:", hap)

# 계산기 프로그램
def Calc(op):
    num1 = int(input("첫 번째 숫자 입력:"))
    num2 = int(input("두 번째 숫자 입력:"))
    print("## 계산기:",num1,op,num2,"=", end='')
    if op =='+':
        return num1+num2
    elif op =='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        return num1/num2

op = input("계산 입력(+, -, *, /):")
print(Calc(op))

# 계산기 프로그램2
def Calc(num1,op,num2):
    if op =='+':
        res = num1+num2
    elif op =='-':
        res =  num1-num2
    elif op=='*':
        res =  num1*num2
    elif op=='/':
        if num2 == 0: 
            print("0으로는 나누면 안 됩니다 ㅠㅠ")
            return
        res =  num1/num2
    elif op =='**':
        res =  num1**num2
    print("## 계산기:",num1,op,num2,"=",res)    

num1 = int(input("첫 번째 숫자 입력: "))
op = input("계산 입력(+, -, *, /, **): ")
num2 = int(input("두 번째 숫자 입력: "))
Calc(num1, op,num2)

# 지역변수와 전역변수
def func1():
    a=10    # 지역변수
    print("func1()에서의 a 값 ",a)

def func2():    
    print("func2()에서의 a 값 ",a)

a=20    # 전역변수

# 메인 코드 부분
func1()
func2()

# 숫자 2개의 합과 3개의 합을 구하는 함수
def para2_func(v1,v2):
    return v1+v2

def para3_func(v1,v2,v3):
    return v1+v2+v3

hap =0
hap = para2_func(10,20)
print("매개변수 2개 함수 호출 결과==>", hap)
hap =para3_func(10,20,30)
print("매개변수 3개 함수 호출 결과==>", hap)

# 매개변수에 기본값을 설정해 놓는 방법
def para3_func(v1,v2,v3=0):
    return v1+v2+v3

hap =0
hap = para3_func(10,20)
print("매개변수 2개 함수 호출 결과==>", hap)
hap =para3_func(10,20,30)
print("매개변수 3개 함수 호출 결과==>", hap)

# 매개변수의 개수를 지정하지 않고 전달하는 방법
def para_func(*para):
    res = 0
    for num in para:
        res = res+num
    return res

hap =0

hap = para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==>%d" % hap)
hap = para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과 ==>%d" % hap)
hap =para_func(10,20,30,40,50,60,70,80,90,100)
print("매개변수가 10개인 함수를 호출한 결과 ==>%d" % hap)