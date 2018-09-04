print("이차방정식 프로그램입니다.")
print("제작 = 원주삼육고등학교 홍민기")


#식의 정보 조사
a = int(input("x^2의 계수를 입력해주세요."))

b = int(input("x의 계수를 입력해주세요."))

c = int(input("상수를 입력해주세요."))

print('y=',a,'*x**2+',b,'*x +',c, '<<<이 식을 복사하여 입력해주세요.')

quad = str(input())

#거북이 그래픽 범위와 속도, 펜 굵기 설정
import turtle as t
x_min = -10
x_max = +10

y_min = -10
y_max = +10

space = 0.1

func_list = [quad]  #이차식

t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.speed(0)
t.pensize(2)

#x축
t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)

#y축
t.up()
t.goto(0, y_min)
t.down()
t.goto(0, y_max)

#그래프 색깔
t.color('blue')

#식 그리기
for func in func_list:
    x = x_min
    exec(func)
    t.up()
    t.goto(x,y)
    t.down()

    while x <= x_max:       # 설정한 x 최대값에 가면 정지
        x = x + space
        exec(func)
        t.goto(x,y)


import math
import sys

#판별식을 사용하여 근의 개수 판단하기

if a == 0:
    print('이차 방정식이 아닙니다.')
    sys.exit()


D = b**2-4*a*c        #D=b^2-4ac


if D > 0:
    fst = (-b+math.sqrt(D))/(2*a)
    snd = (-b-math.sqrt(D))/(2*a)
    print("2개의 해:", fst, snd, "를 가집니다!")

if D == 0:
    trd = -b/(2*a)
    print("1개의 해:",trd,'를 가집니다.')

if D < 0:
    print("해를 가지지 않는 식입니다.")
    
