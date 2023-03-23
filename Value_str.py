# 문자열에 변수 값을 삽입하여 출력
username= input("이름 ==> ")
userPhone = input("전화번호 ==> ")
print("제 이름은", username,"이고, 연락처는",userPhone,"입니다.")
print("제 이름은 %s 이고, 연락처는 %s 입니다." %(username,userPhone))
