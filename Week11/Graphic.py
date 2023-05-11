# 훈민정음 그래픽 디자인
"""
세종대왕께서 창제하신 훈민정음을 거북이가 화면에 예쁘게 씀.
랜덤한 위치 및 크기, 랜점 색상으로 한 글자씩 써지도록 하시오
"""
import turtle
import random
def getXYAS():
    x,y,angle,size =0,0,0,0
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    angle = random.randint(-250,250)
    size = random.randint(10,50)
    return x,y,size
koreanStr =""" 나랏말싸미 듕귁에 달아 문자와 서르 사맛디 아니랗쎄
이런 젼차로 어린 백셩이 느니르고져 홀 배 이셔도
마참내 제 뜨들 시러펴디 몯 할 노미 하니라
내 이랄 위하야 어엿비 너겨 새로 스물 여듪 짜랄 맹가노니
사람마다 해여 수비 니겨 날로 쑤메 뼌한킈 하고져 할따라미니라
"""
colorList =["red", "green","blue","black","magenta","orange","gray"]
tx,ty,txtsize =0,0,0

turtle.shape('turtle')
turtle.setup(550,550)
turtle.screensize(500,500)
turtle.penup()
turtle.speed(5)

for ch in koreanStr:
    tx, ty, txtsize = getXYAS()
    color = random.choice(colorList)
    turtle.goto(tx,ty)
    turtle.pencolor(color)
    turtle.write(ch, font=('맑은고딕', txtsize,'bold'))
turtle.done()

# 파일 읽기와 쓰기

inFile =None #입력 파일
inStr="" #읽어온 문자열

inFile = open("C:\Python_Workspace\Week11/myData1.txt","r", encoding="UTF-8")
inStr = inFile.readline()
print(inStr,end="")
inStr = inFile.readline()
print(inStr,end="")
inStr = inFile.readline()
print(inStr,end="")

inFile.close()

