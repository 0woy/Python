# 문자열에서 개별 문자 추출
# 문자열이 저장된 변수 s에서 s[a:b]는 인덱스 a부터 b-1까지의 문자열 의미
#ex) s[a:b:c]: a<b이고, c>0: a부터 b-1까지의 c간격의 문자열
# a>b이고, c>0: a부터 b-1까지의 c간격의 문자열

s="Hello Python"
print(s[6:10])
print(s[-6:-2])
print(s[0:10:2])
print(s[-1:-7:-1])


var1= "트와이스"
print("원본 문자열 ==> "+var1)
print("반대 문자열 ==> "+var1[-1:-6:-1])