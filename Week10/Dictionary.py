#딕셔너리와 관련된 유용한 함수
empDict ={'사번':1000,'이름':'홍길동','부서':'케이팝'}
print(empDict.keys())
print(list(empDict.keys()))

print('이름' in empDict)            # 딕셔너리 안에 키가 있는지 확인
print('주소' in empDict)            
print('홍길동' in empDict.values()) # 딕셔너리 안에 값이 있는지 확인

#영한사전 프로그램
word = {'apple':'사과','banana':'바나나','cherry':'체리'}
print(word)
eng = input("영문 입력: ")
if eng in word:
    print("뜻:", word[eng])
else:
    print("사전에 등재되어 있지 않은 단어입니다.")

#가수 정보 딕셔너리 저장 및 출력
group ={}
group['이름'] ='트와이스'
group['구성원수'] ='9'
group['데뷰'] ='서바이벌 식스틴'
group['대표곡'] ='CRY FOR ME'

for k in group.keys():
    print(k,'==>',group[k])

#편의점 물품 재고량 딕셔너리
store ={}
while True:
    a = input("입력 물품==>")
    if a == 'z': break
    num = int(input("재고량==>"))
    store[a] = num
print("*** 물품의 재고량 확인 ***")
while True:
    item = input("찾을 물품==>")
    if item =="": break

    if item in store.keys():
        print(store[item],"개 남았어요")
    else : print("그 물품은 없어요")