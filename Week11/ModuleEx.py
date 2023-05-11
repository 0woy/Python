"""
모듈의 종류
- 표준 모듈, 사용자 정의 모듈, 서드 파티 모듈로 구분
표준 모듈: Python에서 제공하는 모듈
사용자 정의 모듈: 직접 만들어서 사용하는 모듈
서드 파티(3rd Party)모듈: Python이 아닌 외부 회사나 단체에서 제공하는 모듈

Python 표준 모듈이 모든 기능을 제공하지 않으며, 서드 파티 모듈 덕분에 
Python에서도 고급 프로그래밍 가능
"""
# 모듈의 생성과 사용
import Module1
Module1.func1()
Module1.func2()
Module1.func3()
# 또는
from Module1 import func1, func2, func3
func1()
func2()
func3()

# 재귀 함수
def selfCall():
    print("하", end="")
    selfCall()
selfCall()

# 입력한 숫자를 1까지 세는 재귀 함수
def count(num):
    if num>=1:
        print(num," ",end="")
        count(num-1)
    else: return
count(10)
print()
count(20)

# 팩토리얼 값을 구하는 함수
fact =0
def factorial(x):
    global fact
    fact =1
    for i in range(1,x+1):
        fact *=i
    return print(f'{x}! = {fact}')

num=int(input("수를 입력하세요. "))
factorial(num)

# 팩토리얼 값을 구하는 함수2
def factorial(x):
    if x==1: return 1
    return x * factorial(x-1)
num = int(input("수를 입력하세요. "))
print(f'{num}! = {factorial(num)}')
