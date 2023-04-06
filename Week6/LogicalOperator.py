#나이가 10살 이상이고, 키가 165 이상인 경우 놀이기구 탑승
age = int(input("나이를 입력하세요 : "))
cm = int(input("키를 입력하세요 : "))
if(age >=10 and cm >=165):
   print("놀이기구에 탑승 가능")
else:
   print("놀이기구에 탑승 불가능")


#중첩 IF를 사용한 성적에 따른 학점 차등 부여 프로그램
score = int(input("점수를 입력 ===> "))
if(score>=60):
    if(score>=90): print("A", end='')
    else:
        if(score>=80): print("B", end='')
        else: 
            if(score>=70): print("C", end='')
            else: print("D", end='')
else: print("F", end='')
print("학점입니다.")

# 중첩IF, 동전을 넣으면 음료를 주는자판기, 500원 짜리 음료수 뽑은 후 잔액 출력
coin = int(input("동전을 넣어주세요: "))
if(coin >=500):
    num = int(coin/500)
    res = coin %500
    print("음료수가",num,"개 나왔습니다.")
    if(res>0):
        print("거스름돈은", res,"원 입니다.")
else: print(coin,"원이 반환되었습니다.")
