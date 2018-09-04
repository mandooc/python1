print("제작: 원주삼육고등학교 3학년 홍민기")

t = 1
while t <= 100000000:
    
    x = input("점수를 입력해주세요. :")
    z = float(x)

    x = input("평균 점수를 입력해주세요. :")
    평균 = float(x)

    x = input("표준편차를 입력해주세요. :")
    표준편차 = float(x)

    x = input("수강자 수를 입력해주세요. :")
    명수 = float(x)


    import math
    f = lambda z: (1/(표준편차*math.sqrt(2*math.pi))) * math.e ** (-1*(((z - 평균)**2)/(2*표준편차**2)))
    a = 평균
    b = z
    n = 5
    h = (b - a) /n
    s = 0.5 * (f(a) + f(b))
    for i in range(1,n):
        s += f(a + i*h)
    integral = h * s


    퍼센트 = (1-(integral+0.5))*100

    print("당신은 상위 (약)",(1-(integral+0.5))*100,"% 입니다.")
    print(명수,"명 기준 (약)",명수*(1-(integral+0.5)),"등 입니다.")
    print("크고 작은
          오차가 존재할 수 있습니다.")

    aaa = "공부 좀 하시네요 ㅋ"

    bbb = "조금 더 열심히 합시다!"

    ccc = "공부 할 생각이 없는거죠?"

    grade = "0"
    pg = aaa


    if 퍼센트 <= 4:
        grade = "1"
        pg = aaa

    if 4 < 퍼센트 <= 11:
        grade = "2"
        pg = aaa

    if 11 < 퍼센트 <= 23:
        grade = "3"
        pg = aaa

    if 23 < 퍼센트 <= 40:
        grade = "4"
        pg = bbb
    
    if 40 < 퍼센트 <= 60:
        grade = "5"
        pg = bbb
    
    if 60 < 퍼센트 <= 77:
        grade = "6"
        pg = ccc
    
    if 77 < 퍼센트 <= 89:
        grade = "7"
        pg = ccc
    
    if 89 < 퍼센트 <= 96:
        grade = "8"
        pg = ccc
    
    if 96 < 퍼센트 <= 100:
        grade = "9"
        pg = ccc

    print("예상 등급은",grade,"등급입니다.",pg)

    t = t + 1



    
