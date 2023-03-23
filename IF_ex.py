# #if문의 사용 형식
# # 조건이 참일때 실행할 문장이 2개인 경우
# num =200
# if num>100:
#     print("100보다", end='')
#     print(" 큽니다")
#     print("프로그램 종료")

# # 70점 이상을 받으면 합격, 아니면 불합격 출력
# score = int(input("성적을 입력하세요. : "))
# if(score>=70): print("합격입니다.")
# else: print("불합격입니다.")

num =200
if(num <100):
    print("100보다 작군요")
    print("여기는 참입니다.")
else:
     print("100보다 크군요")
     print("여기는 거짓입니다.")
print("프로그램 끝!")

# #입력한 숫자의 홀짝 판단
# num = int(input("숫자를 입력 ==> "))
# if(num%2==0): print("짝수입니다.")
# else: print("홀수입니다.")
