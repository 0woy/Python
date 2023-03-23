# 파이썬의 기본 내장 함수, 문자열의 길이 파악시 사용
# 한글, 기호, 영문, 공백 숫자까지 모두 글자로 취급

var = "난생처음! Python"
print(len(var))

# 두 문자열을 입력, 두 문자열 길이 차이 체크
var1 = input("첫번째 문자열 ===> ")
var2=  input("두 번째 문자열 ==> ")

print("두 문자열의 길이 차는 ", len(var1)-len(var2),"입니다.")

# upper(), lower()
# 영문을 제외한 한글, 숫자, 기호 등은 위 함수의 영향을 받지 않음
ss ='First Python을 밤 12시까지 열공 중!'
var1 =ss.upper()
print(var1)
var2 = ss.lower()
print(var2)

#isupper(), islower(): 문자열이 모두 대/소 문자이면 True 반환
ss = 'first python'
print(ss.isupper())
