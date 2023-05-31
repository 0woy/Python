# # try-except 문
# import os

# try:
#     os.remove("C:/Temp/noFile.exe")
# except:
#     print("파일이 없네요 확인 바랍니다.")

# import os

# inFile = None
# inStr = ""
# fName = ""

# fName = input("파일 명을 입력하세요: ")
# try:
#     os.path.exists(fName)
#     inFile = open(fName, "r", encoding="UTF-8")
#     inStr = inFile.readline()
#     inStr = inFile.readline()
#     print(inStr, end="")
#     inStr = inFile.readline()
#     print(inStr, end="")
#     inFile.close()
# except:
#     print(fName, "파일이 없습니다.")

# # 오류의 종류에 따라서 다른 처리를 하는 코드
# num1 = input("숫자1--> ")
# num2 = input("숫자1--> ")

# try:
#     num1 = int(num1)
#     num2 = int(num2)
#     while True:
#         res = num1 / num2
# except ValueError:
#     print("문자열은 숫자로 변환할 수 없습니다.")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except KeyboardInterrupt:
#     print("Ctrl+c를 눌렀군요")


# try, except, els, finally
num1 = input("숫자1--> ")
num2 = input("숫자1--> ")

try:
    num1 = int(num1)
    num2 = int(num2)
except:
    print("오류가 발생했습니다.")
else:
    print(num1, "/", num2, "=", num1 / num2)
finally:
    print("이 부분은 무조건 나옵니다.")
