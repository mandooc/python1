



print('제작자: 원주삼육고 홍민기')

w = input("점의 개수를 정해주세요!")
times = int(w)




import math

import turtle as t
t.shape('turtle')
t.speed(0)



def place_a_dot(x,y,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.dot(5, color)

def pythagorean(x,y):
    import math
    a = x**2
    b = y**2
    c = math.sqrt(a+b)
    return c
    


t.penup()
t.goto(-250,-250)
t.pendown()
t.fd(500)
t.lt(90)
t.fd(500)
t.lt(90)
t.fd(500)
t.lt(90)
t.fd(500)
t.penup()
t.goto(0,250)
t.pendown()
t.fd(500)
t.penup()
t.goto(-250,0)
t.pendown()
t.lt(90)
t.fd(500)
t.penup()
t.goto(0,-250)
t.pendown()
t.color('green')
t.circle(250)
t.color('black')

i=0
o=0
count = 1

for x in range(times):
    import random
    x = random.randint(-250,250)
    y = random.randint(-250,250)



    if pythagorean(x,y) <= 250:
        color = 'blue'
        i += 1
        print(count)
        count = count + 1
        
        
    else:
        color = 'red'
        o += 1
        print(count)
        count = count + 1
        

    place_a_dot(x,y,color)

print('점의 총 개수는', times, '개, 그중 원 안의 점은', i, '개 입니다.')
print('계산된 원주율은', float(i)/times*4, '이고 실제 원주율과 ',float(math.pi-float(i)/times*4),'만큼 차이가 납니다.')

    




