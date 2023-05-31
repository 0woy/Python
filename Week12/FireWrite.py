# writeLines()
outFile = None
outStr = ""
outFile = open("C:\Python_Workspace\Week12\myData2.txt", "w")

outStr = "안녕하세요?"
outFile.writelines(outStr + "\n")

outStr = "반갑습니다."
outFile.writelines(outStr + "\n")

outStr = "자주만나요. ^^"
outFile.writelines(outStr + "\n")
outFile.close()
print("---myData2.txt 파일이 저장됨 ---")

# 사용자에게 입력받은 내용을 파일에 쓰기
outFile = None
outStr = ""
outFile = open("C:\Python_Workspace\Week12\myData3.txt", "w")
while True:
    outStr = input("내용 입력 ==>")
    if outStr != "":
        outFile.writelines(outStr + "\n")
    else:
        break
outFile.close()
print("---myData3.txt 파일이 저장됨 ---")


# 필기 노트 복사하기
inFile, outFile = None, None
inStr, inList = "", []

inFile = open("C:\Python_Workspace\Week12\pythonNote.txt", "r", encoding="UTF-8")
outFile = open("C:\Python_Workspace\Week12\myNote.txt", "w", encoding="UTF-8")

inList = inFile.readlines()
for inStr in inList:
    outFile.writelines(inStr)
inFile.close()
outFile.close()
print("--- pythonNote.txt가 myNote.txt로 복사되었음")

# 문자 암호화 하기
print(ord("난"))
print(chr(45212))
num = ord("난")
print(chr(num + 100))  # 암호화
num = ord("넀")
print(chr(num - 100))  # 복호화

# 스파이에게 암호화 문자 보내기
secureFile = None
inStr, secure = "", ""

secureFile = open("C:\Python_Workspace\Week12\secure.txt", "w", encoding="UTF-8")
while True:
    inStr = input("스파이에게 전달할 메시지 ==> ")
    if inStr == "":
        break
    for ch in inStr:
        num = ord(ch)
        num += 100
        secure += chr(num)
    secureFile.writelines(secure)
secureFile.close()
print("--- secure.txt 암호화 완료 ---")

# 파일 삭제 및 크기 확인
import os

os.remove("C:/Temp/myNote.exe")
print(os.path.getsize("C:\Python_Workspace\Week12\secure.txt"))

# 파일 압축 및 압축 풀기
import zipfile

# 압축기능
newZip = zipfile.Zipfile("C:Temp\new.zip", "w")
newZip.write("C:\Windows\notepad.ext", compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

# 압축 풀기
extZip = zipfile.ZipFile("C:\Temp\new.zip", "r")
extZip.extractall("c:/Temp/")
extZip.close()
