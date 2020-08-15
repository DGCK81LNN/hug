import turtle
import time
import re
import random

def p(text, end="\n", wait=0.5):
    for i in range(len(text)):
        print(text[i], end='',flush=True)
        time.sleep(0.03)
    time.sleep(wait)
    print(end,end='')

def i(prompt):
    p(prompt,end='')
    return input()

p('FOR TFLS 初中部 17级-20届8班同学')
p('by 孟庆睿 & 罗奕恒')
p('2.0.0 ALPHA')
x=0
y=0
a=i('你的名字:')
if a=='王翊轩'or a=='孟庆睿' or a=='陈王俊逸' or a=='陈思源' or a=='齐天' or a=='胡涛' or a=='靳博涵' or a=='张泓洋' or a=='刘传鹏' or a=='陈旭阳' or a=='张博涵' or a=='杜圣迪' or a=='罗奕恒' or a=='娄文喆' or a=='栾智翔' or a=='祁子荃' or a=='李佳澍':
    ge=1
elif a=='刘屹' or a=='刘益同' or a=='武昕冉' or a=='汪妍竹' or a=='王思颖' or a=='刘晓薇' or a=='黄淦欣' or a=='陈奕伽' or a=='吴亭颐' or a=='陈思涵' or a=='刘书彤' or a=='李潇曼' or a=='韩睿' or a=='戴睿' or a=='运涵' or a=='胡泽伊' or a=='田馨雅' or a=='崔玉莹' or a=='赵梓涵' or a=='邵佳琳' or a=='陈露萍' or a=='王泰然' or a=='李欣然':
    ge=2
else:
    p('你不是TFLS 17届8班同学')
    ge=0
    gee=0
    a="none"
    b="none"
    d="none"
if ge==1 or ge==2:
    b=i('你想拥抱谁:')
    if b=='王翊轩'or b=='孟庆睿' or b=='陈王俊逸' or b=='陈思源' or b=='齐天' or b=='胡涛' or b=='靳博涵' or b=='张泓洋' or b=='刘传鹏' or b=='陈旭阳' or b=='张博涵' or b=='杜圣迪' or b=='罗奕恒' or b=='娄文喆' or b=='栾智翔' or b=='祁子荃' or b=='李佳澍' or b=='刘屹' or b=='刘益同' or b=='武昕冉' or b=='汪妍竹' or b=='王思颖' or b=='刘晓薇' or b=='黄淦欣' or b=='陈奕伽' or b=='吴亭颐' or b=='陈思涵' or b=='刘书彤' or b=='李潇曼' or b=='韩睿' or b=='戴睿' or b=='运涵' or b=='胡泽伊' or b=='田馨雅' or b=='崔玉莹' or b=='赵梓涵' or b=='邵佳琳' or b=='陈露萍' or b=='王泰然' or b=='李欣然':      
        gee=1
        if a!=b:
            d=i('你想对'+b+'说什么?')
        else:
            d="none"
        if b=='刘屹' or b=='刘益同' or b=='武昕冉' or b=='汪妍竹' or b=='王思颖' or b=='刘晓薇' or b=='黄淦欣' or b=='陈奕伽' or b=='吴亭颐' or b=='陈思涵' or b=='刘书彤' or b=='李潇曼' or b=='韩睿' or b=='戴睿' or b=='运涵' or b=='胡泽伊' or b=='田馨雅' or b=='崔玉莹' or b=='赵梓涵' or b=='邵佳琳' or b=='陈露萍' or b=='王泰然' or b=='李欣然':
            gee=gee+1    
        if a==b:
            p(a+"自'抱'自弃")
        else:
            if b=='孟庆睿':
                if a=='武昕冉':
                    p("孟庆睿紧紧地抱住了你")
                    p("他充满爱意地凝视着你")
                    p("他抚摸了一下你的头")
                    p("他用双手托住你的大腿和腰背,轻轻地把你抱了起来")
                elif ge==1:
                    p("你抱了孟庆睿一下")
                    p("他轻轻地闭上了眼睛，对你说:'You're a gay.'")
                elif d=="我是武昕冉" or d=="把我当成武昕冉吧" or d=="把我当成武昕冉" or d=="我也爱你" or d=="我也是武昕冉" or d=="我叫武昕冉" or d=="我也叫武昕冉" or d=="我是武昕冉变的":
                    p("孟庆睿紧紧地抱住了你")
                    p("他充满爱意地凝视着你,仿佛真的在抱着武昕冉")
                    p("他抚摸了一下你的头")
                    p("他用双手托住你的大腿和腰背,轻轻地把你抱了起来")
                else:
                    p("你抱了孟庆睿一下")
                    p("他用力地扭动了他的身体,推了你的肩膀")
                    p("你被狠狠地推开了")
                    y=1
            elif b=='武昕冉':
                if a=='孟庆睿':
                    p("你抱向了你心爱的武昕冉")
                    p("她向下一躲,从你的胸前逃走了")
                    y=1
                elif a=='娄文喆':
                    p("你抱了娇小的武昕冉一下")
                    p("她推开了你,你喊道:'大仙快来管管你媳妇儿.'却适得其反")
                    p("你试图逃跑,但他们俩追打了你很久")
                    p("孟庆睿像一堵墙一样出现在你面前,后面的武昕冉也追了上来")
                    p("你被逮到后门与后墙之间的缝隙中,怎么推门都推不动")
                    p("武昕冉向你逼近,你已无路可逃")
                    p("她捏了捏你的脸,打了你几下")
                    y=1
                elif ge==1:
                    p("你抱住了娇小的武昕冉")
                    p("几秒后,一个沉重的脚步声从你后面靠近")
                    p("你被狠狠地推了一下,倒在了地上,晕倒了")
                    y=2
                else:
                    p("你抱住了娇小的武昕冉")
                    p("几秒后,一个沉重的脚步声从你后面靠近")
                    p("你感到了一丝不祥的预感.但什么也没发生")
            elif b=='刘屹':
                if a=='陈王俊逸':
                    p("你与刘屹紧紧地拥抱在了一起")
                    p("你与她深情地对视着,害羞地低下了头")
                    p("你坐回了你的座位")
                    p("她弯下腰来,轻轻地抚摸了一下你的后背")
                    p("你倚靠在她胸前,甜蜜贯穿全身,心中幸福无比")
                elif ge==1:
                    p("你刚抱到刘屹,她就与陈王俊逸一起对你说了‘太过分了’")
                    p("你试图逃跑,但他们俩追打了你很久")
                    y=3
            elif b=='陈王俊逸':
                if a=='刘屹':
                    p("你与陈王俊逸紧紧地拥抱在了一起")
                    p("你与他深情地对视着,害羞地低下了头")
                    p("他坐回了他的座位")
                    p("你弯下腰来,轻轻地抚摸了一下他的后背")
                    p("他倚靠在你胸前,甜蜜贯穿全身,心中幸福无比")
                elif ge==2:
                    p("你刚抱到陈王俊逸,他就与刘屹一起对你说了‘太过分了’")
                    p("你试图逃跑,但他们俩追打了你很久")
                    y=3
            else:
                p("你抱住了"+b)
    else:
        p('你想抱的人不在TFLS 17届8班')
        gee=0
        b="none"
        d="none"
if ge==1 and gee==1:
    if b!='孟庆睿':
        p("Are you a gay?")
if ge==2 and gee==2:
    if a!=b:
        p("Are you a lesbian?")
c=turtle.Turtle()
c.color('red')
c.left(90)
c.begin_fill()
c.circle(10,195)
c.goto(-16,-11)
c.goto(-12,-18)
c.goto(-8,-23)
c.goto(-4,-27)
c.goto(0,-30)
c.up()
c.goto(0,0)
c.down()
c.right(195)
c.circle(-10,195)
c.goto(16,-11)
c.goto(12,-18)
c.goto(8,-23)
c.goto(4,-27)
c.goto(0,-30)
c.end_fill()
c.up()
c.goto(-80,-14)
if ge==1:
    c.color(0.3,0.6,1)
else:
    c.color(0.9,0.1,0.6)
c.write(a,font=20)
c.goto(22,-14)
if gee==1:
    c.color(0.3,0.6,1)
else:
    c.color(0.9,0.1,0.6)
c.write(b,font=20)
c.ht()
c.goto(-110,-40)
if ge==1:
    c.color(0.3,0.6,1)
else:
    c.color(0.9,0.1,0.6)
c.write(d,font=20)
if y==1:
    c.goto(25,-30)
    if gee==1:
        c.color(0.3,0.6,1)
    else:
        c.color(0.9,0.1,0.6)
    c.write('NO')
if y==2:
    c.goto(25,-30)
    c.color(0,0.6,0)
    c.write('NO')
if y==3:
    for aa in range(30):
        c.goto(random.randint(-300,300),random.randint(-300,300))
        c.color(random.randint(0,30)*0.01,random.randint(60,100)*0.01,random.randint(0,30)*0.01)
        c.write('太过分了',font=(30))
c.speed('slowest')
c.goto(1000,0)

