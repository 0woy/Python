# class Rabbit:
#     # 토끼의 속성
#     shape = ""
#     xpos = 0
#     ypos = 0

#     def __init__(self, value):
#         self.shape = value

#     def goto(self, x, y):
#         self.xpos = x
#         self.ypos = y

#     def position(self):
#         print("**토끼의 현재 위치는 (", str(self.xpos), ",", str(self.ypos), ")")


# ## 3번
# rabbit1 = Rabbit("원")
# print("rabbit1의 모양:", rabbit1.shape)
# rabbit2 = Rabbit("삼각형")
# print("rabbit2의 모양:", rabbit2.shape)
# rabbit3 = Rabbit("토끼")
# print("rabbit3의 모양:", rabbit3.shape)

# ## 2번
# rabbit = Rabbit()
# print("rabbit의 모양:", rabbit.shape)

## 1번
# rabbit1 = Rabbit()
# rabbit2 = Rabbit()
# rabbit3 = Rabbit()

# rabbit1.shape = "원"
# rabbit2.shape = "삼각형"
# rabbit3.shape = "토끼"

# # 깡총깡총 뛰어다니는 토끼
# rabbit = Rabbit()
# rabbit.shape = "토끼"
# while True:
#     x = int(input("토끼가 이동할 X좌표 ==> "))
#     y = int(input("토끼가 이동할 Y좌표 ==> "))
#     rabbit.goto(x, y)
#     rabbit.position()


# class Rabbit:
#     # 토끼의 속성
#     shape = ""

#     # def __del__(self):
#     #     print("이제", self.shape, "는 자유에요~~")

#     def __add__(self, other):
#         print("객체", self.shape, "와", other.shape, "가 친구가 되었습니다.")


# # 객체끼리의 덧셈
# rabbit1 = Rabbit()
# rabbit1.shape = "엽기토끼"
# rabbit2 = Rabbit()
# rabbit2.shape = "도비"
# rabbit1 + rabbit2


# # 선을 객체로 활용하기
# class Line:
#     length = 0

#     def __init__(self, length):
#         self.length = length
#         print(self.length, "길이의 선이 생성되었습니다.")

#     def __del__(self):
#         print(self.length, "길이의 선이 제거되었습니다.")

#     def __add__(self, other):
#         return self.length + other.length

#     def __lt__(self, other):
#         return self.length < other.length

#     def __eq__(self, other):
#         return self.length == other.length


# line1 = Line(10)
# line2 = Line(5)
# print("두 선의 합:", line1 + line2)
# if line1 < line2:
#     print("선2가 더깁니다.")
#     del line1
# elif line1 == line2:
#     print("두 선의 길이가 같습니다.")
# else:
#     print("선1이 더 깁니다.")
#     del line2


# # 상속 구현하기
# class Rabbit:
#     shape = ""
#     xpos = 0
#     ypos = 0

#     def __init__(self, value):
#         self.shape = value

#     def goto(self, x, y):
#         self.xpos = x
#         self.ypos = y

# class HouserRabbit(Rabbit):
#     owner = ""

#     def eatFood():
#         print("집토끼가 모이를 먹습니다.")

# class MountainRabbit(Rabbit):
#     mountain = ""

#     def eatWildglasS():
#         print("산토끼가 들풀을 먹습니다.")

# hRabbit = HouserRabbit()
# mRabbit = MountainRabbit()

# hRabbit.shape = "원"
# mRabbit.goto(100, 100)


# 바다 거북과 모래거북
import turtle


class SeaTurtle(turtle.Turtle):
    name = ""
    body = None

    def __init__(self):
        self.body = turtle.Turtle("triangle")
        self.body.color("blue")
        self.name = "바다거북"

    def swim(self, x, y):
        self.body.goto(x, y)


class Sandurtle(turtle.Turtle):
    name = ""
    body = None

    def __init__(self):
        self.body = turtle.Turtle("circle")
        self.body.color("red")
        self.name = "모래거북"

    def walk(self, x, y):
        self.body.goto(x, y)


seaTut, sandTut = None, None
seaTut = SeaTurtle()
sandTut = Sandurtle()
seaTut.swim(100, 100)
seaTut.body.write(seaTut.name, font=("Arial", 20))
sandTut.walk(100, -100)
sandTut.body.write(sandTut.name, font=("Arial", 20))
