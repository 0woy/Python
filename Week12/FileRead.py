# with~as
inFile = None
inStr = ""

with open("myData1.txt", "r", encoding="UTF-8") as inFile:
    inStr = inFile.readline()
    print(inStr, end="")

    inStr = inFile.readline()
    print(inStr, end="")

    inStr = inFile.readline()
    print(inStr, end="")

# os.path.exist
import os

inFile = None
inStr = ""
fName = ""

fName = input("파일 명을 입력하세요: ")
if os.path.exists(fName):
    inFile = open(fName, "r", encoding="UTF-8")
    inStr = inFile.readline()
    inStr = inFile.readline()
    print(inStr, end="")
    inStr = inFile.readline()
    print(inStr, end="")
    inFile.close()
else:
    print(fName, "파일이 없습니다.")

# 파일의 모든 행 읽기
inFile = None
inStr = ""

inFile = open("myData1.txt", "r", encoding="UTF-8")
while True:
    inStr = inFile.readline()
    if inStr == "":
        break
    print(inStr, end="")
inFile.close()

# 파일의 내용 한꺼번에 읽기
inFile = None
inStr = ""

inFile = open("myData1.txt", "r", encoding="UTF-8")
inList = inFile.readlines()
print(inList)
inFile.close()

inFile = None
inStr = ""

inFile = open("myData1.txt", "r", encoding="UTF-8")
inList = inFile.readlines()
for inStr in inList:
    print(inStr, end="")
inFile.close()

# read() 함수
inFile = None
inStr = ""
inRead = ""

inFile = open("myData1.txt", "r", encoding="UTF-8")
# inStr = inFile.read()
inRead = inFile.read(10)
# print(inStr, end="")
print(inRead, end="")

inFile.close()

# 행 번호 붙이는 프로그램
inFile = None
inStr = ""
lineNum = 1

inFile = open("myData1.txt", "r", encoding="UTF-8")
while True:
    inStr = inFile.readline()
    if inStr == "":
        break
    print(lineNum, ":", inStr, end="")
    lineNum += 1

inFile.close()
