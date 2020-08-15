import random
import turtle
lyhgl=0
lyhbl=0
lyhbg=0
print("人名请写中文!")
#a for hugger;b for huggee;gendera for hugger;genderb for huggee;1 for boys;2 for girls
while True:
    print('FOR TFLS 初中部 17级-20届8班同学')
    print('VER1.4')
    y=0
    z=0
    a=input('你的名字(请写中文):')
    if a=='王翊轩'or a=='孟庆睿' or a=='陈王俊逸' or a=='陈思源' or a=='齐天' or a=='胡涛' or a=='靳博涵' or a=='张泓洋' or a=='刘传鹏' or a=='陈旭阳' or a=='张博涵' or a=='杜圣迪' or a=='罗奕恒' or a=='娄文喆' or a=='栾智翔' or a=='祁子荃' or a=='李佳澍':
        gendera=1
    elif a=='刘屹' or a=='刘益同' or a=='武昕冉' or a=='汪妍竹' or a=='王思颖' or a=='刘晓薇' or a=='黄淦欣' or a=='陈奕伽' or a=='吴亭颐' or a=='陈思涵' or a=='刘书彤' or a=='李潇曼' or a=='韩睿' or a=='戴睿' or a=='运涵' or a=='胡泽伊' or a=='田馨雅' or a=='崔玉莹' or a=='赵梓涵' or a=='邵佳琳' or a=='陈露萍' or a=='王泰然' or a=='李欣然':
        gendera=2
    else:
        print('你不是TFLS 17届8班同学')
        gendera=0
        genderb=0
        a=""
        b=""
        d=""
    if gendera==1 or gendera==2:
        b=input('你想拥抱谁(请写中文):')
        if b=='王翊轩'or b=='孟庆睿' or b=='陈王俊逸' or b=='陈思源' or b=='齐天' or b=='胡涛' or b=='靳博涵' or b=='张泓洋' or b=='刘传鹏' or b=='陈旭阳' or b=='张博涵' or b=='杜圣迪' or b=='罗奕恒' or b=='娄文喆' or b=='栾智翔' or b=='祁子荃' or b=='李佳澍' or b=='刘屹' or b=='刘益同' or b=='武昕冉' or b=='汪妍竹' or b=='王思颖' or b=='刘晓薇' or b=='黄淦欣' or b=='陈奕伽' or b=='吴亭颐' or b=='陈思涵' or b=='刘书彤' or b=='李潇曼' or b=='韩睿' or b=='戴睿' or b=='运涵' or b=='胡泽伊' or b=='田馨雅' or b=='崔玉莹' or b=='赵梓涵' or b=='邵佳琳' or b=='陈露萍' or b=='王泰然' or b=='李欣然':      
            genderb=1
            if a!=b:
                d=input('你想对'+b+'说什么?')
            else:
                d=""
            if b=='刘屹' or b=='刘益同' or b=='武昕冉' or b=='汪妍竹' or b=='王思颖' or b=='刘晓薇' or b=='黄淦欣' or b=='陈奕伽' or b=='吴亭颐' or b=='陈思涵' or b=='刘书彤' or b=='李潇曼' or b=='韩睿' or b=='戴睿' or b=='运涵' or b=='胡泽伊' or b=='田馨雅' or b=='崔玉莹' or b=='赵梓涵' or b=='邵佳琳' or b=='陈露萍' or b=='王泰然' or b=='李欣然':
                genderb=2    
            if a==b:
                print(a+"自'抱'自弃")
            else:
                if b=='孟庆睿':
                    if a=='武昕冉':
                        print("孟庆睿紧紧地抱住了你")
                        print("他充满爱意地凝视着你")
                        print("他抚摸了一下你的头")
                        print("他用双手托住你的大腿和腰背,轻轻地把你抱了起来")
                        y=9
                    elif gendera==1:
                        print("你抱了孟庆睿一下")
                        print("他轻轻地闭上了眼睛，对你说:'You're a gay.'")
                    elif d=="我是武昕冉" or d=="把我当成武昕冉吧" or d=="把我当成武昕冉" or d=="我也爱你" or d=="我也是武昕冉" or d=="我叫武昕冉" or d=="我也叫武昕冉" or d=="我是武昕冉变的":
                        print("孟庆睿紧紧地抱住了你")
                        print("他充满爱意地凝视着你,仿佛真的在抱着武昕冉")
                        print("他抚摸了一下你的头")
                        print("他用双手托住你的大腿和腰背,轻轻地把你抱了起来")
                        y=9
                    elif a=='李潇曼' or a=='王思颖' or a=='戴睿':
                        print("你抱了孟庆睿一下")
                        print("他被吓了一大跳,但面色依然冷漠")
                        print("他说:'我等的并不是你。'")
                        y=5
                    elif a=='刘屹':
                        print("你抱了孟庆睿一下")
                        print("他被吓了一大跳,但面色依然冷漠")
                        print("他说:'你就是那列不在铁轨上跑的火车吗?'")
                        y=3
                    else:
                        print("你抱了孟庆睿一下")
                        print("他用力地扭动了他的身体,推了你的肩膀")
                        print("你被狠狠地推开了")
                        y=1
                elif b=='武昕冉':
                    if a=='孟庆睿':
                        print("你抱向了你心爱的武昕冉")
                        print("她向下一躲,从你的胸前逃走了")
                        y=1
                    elif a=='娄文喆':
                        print("你抱了娇小的武昕冉一下")
                        print("她推开了你,你喊道:'大仙快来管管你媳妇儿.'却适得其反")
                        print("你试图逃跑,但他们俩追打了你很久")
                        print("孟庆睿像一堵墙一样出现在你面前,后面的武昕冉也追了上来")
                        print("你被逮到后门与后墙之间的缝隙中,怎么推门都推不动")
                        print("武昕冉向你逼近,你已无路可逃")
                        print("她捏了捏你的脸,打了你几下")
                        y=1
                    elif gendera==1:
                        print("你抱住了娇小的武昕冉")
                        print("几秒后,一个沉重的脚步声从你后面靠近")
                        print("你被狠狠地推了一下,倒在了地上,晕倒了")
                        y=2
                    else:
                        print("你抱住了娇小的武昕冉")
                        print("几秒后,一个沉重的脚步声从你后面靠近")
                        print("你感到了一丝不祥的预感.但什么也没发生")
                elif b=='刘屹':
                    if a=='陈王俊逸':
                        print("你与刘屹紧紧地拥抱在了一起")
                        print("你与她深情地对视着,害羞地低下了头")
                        print("你坐回了你的座位")
                        print("她弯下腰来,轻轻地抚摸了一下你的后背")
                        print("你倚靠在她胸前,甜蜜贯穿全身,心中幸福无比")
                        y=9
                    elif gendera==1:
                        print("你刚抱到刘屹,她就与陈王俊逸一起对你说了‘太过分了’")
                        print("你试图逃跑,但他们俩追打了你很久")
                        y=4
                    else:
                        print("你抱住了"+b)
                elif b=='陈王俊逸':
                    if a=='刘屹':
                        print("你与陈王俊逸紧紧地拥抱在了一起")
                        print("你与他深情地对视着,害羞地低下了头")
                        print("他坐回了他的座位")
                        print("你弯下腰来,轻轻地抚摸了一下他的后背")
                        print("他倚靠在你胸前,甜蜜贯穿全身,心中幸福无比")
                        y=9
                    elif gendera==2:
                        print("你刚抱到陈王俊逸,他就与刘屹一起对你说了‘太过分了’")
                        print("你试图逃跑,但他们俩追打了你很久")
                        y=4
                    else:
                        print("你抱住了"+b)
                elif b=='罗奕恒':
                    if a=='戴睿' or a=='李潇曼':
                        print("你抱住了罗奕恒")
                        print("他差点当场被吓死")
                    elif a=='武昕冉':
                        print("你抱住了罗奕恒")
                        print("他差点当场被吓死")
                        print("他说:'最想被你抱的并不是我'")
                    elif gendera==2:
                        print("你抱住了罗奕恒")
                        print("他吓了一大跳")
                    else:
                        print("你抱住了"+b)
                elif b=='戴睿':
                    if a=='罗奕恒':
                        print('你.')
                        print('根.')
                        print('本....')
                        print('不.....')
                        print('敢.')
                        print('去....')
                        print('抱.')
                        print('戴.........')
                        print('睿.')
                        print('.........')
                        print('........')
                        print('.')
                        print('')
                    else:
                        print("你抱住了"+b)
                elif b=='李潇曼':
                    if a=='罗奕恒' and (d=="我喜欢你" or d=="我喜欢李潇曼" or d=="我爱上你" or d=="我爱上李潇曼"  or d=="我爱你" or d=="我爱李潇曼" or d=="我喜欢上你" or d=="我喜欢上李潇曼"):
                        print("你那是馋她身子")
                        print("你下贱")
                        lyhgl=1
                        y=6
                    elif a=='杜圣迪':
                        print("你抱住了娇小的李潇曼")
                        print("她脸红了,对你喊道:'渣男!滚!'")
                        print("yh wty甩你了?")
                        print("你绝对是馋我身子")
                        y=1
                    elif a=='靳博涵':
                        print("你抱住了娇小的李潇曼")
                        print("她脸红了,对你喊道:'流氓!滚!'")
                        print("我听mqr说,你和杜圣迪对我有大胆的想法")
                        print("你绝对是馋我身子")
                        y=1
                    else:
                        print("你抱住了"+b)
                elif b=='娄文喆':
                    if a=='罗奕恒':
                        if d=="我完全爱上你" or d=="我完全爱上娄文喆":
                            print("你抱住了娄文喆")
                            print("他瞪大了双眼看着你，脸上露出滑稽的微笑")
                            lyhbl=1
                            y=7
                        elif d=="我喜欢你" or d=="我喜欢娄文喆":
                            print("你抱住了娄文喆")
                            print("他瞪大了双眼看着你，脸上露出滑稽的微笑")
                            lyhbl=1
                            y=8
                        else:
                            print("你抱住了娄文喆")
                            print("他好像已经习惯了")
                    elif a=='武昕冉':
                        print("你抱了娄文喆一下")
                        print("他拍了你一下,他喊道:'大仙快来管管你媳妇儿.'")
                        print("他试图逃跑,孟庆睿也赶了过来")
                        print("孟庆睿像一堵墙一样出现在他面前,你从他的后面追了上来")
                        print("他被逮到后门与后墙之间的缝隙中,怎么推门都推不动")
                        print("你向他逼近,他已无路可逃")
                        print("你捏了捏他的脸,打了你几下")
                        y=1
                    else:
                        print("你抱住了"+b)
                else:
                    print("你抱住了"+b)
        else:
            print('你想抱的人不在TFLS 17届8班')
            gendera=0
            b="none"
            d="none"
    if gendera==1 and genderb==1:
        if b!='孟庆睿':
            print("Are you a gay?")
    if gendera==2 and genderb==2:
        if a!=b:
            print("Are you a lesbian?")
    if a=='武昕冉' and genderb==1 and b!='孟庆睿':
        y=2
        if b=='陈王俊逸':
            z=1
    if (a=='刘屹' and genderb==1 and b!='陈王俊逸') or (a=='陈王俊逸' and genderb==2 and b!='刘屹'):
        print("远处传来一声:'你怎么能这样?太过分了'")
        z=1
    if lyhgl==1 and lyhbl==1:
        lyhbg=1
    t=turtle.Turtle()
    if gendera!=0:
        t.st()
        t.speed(6)          
        t.color('red')
        t.left(90)
        t.pensize(1)
        t.down()
        t.begin_fill()
        t.circle(10,195)
        t.goto(-16,-11)
        t.goto(-12,-18)
        t.goto(-8,-23)
        t.goto(-4,-27)
        t.goto(0,-30)
        t.up()
        t.goto(0,0)
        t.down()
        t.right(195)
        t.circle(-10,195)
        t.goto(16,-11)
        t.goto(12,-18)
        t.goto(8,-23)
        t.goto(4,-27)
        t.goto(0,-30)
        t.end_fill()
        t.right(-195)
        t.up()
        t.goto(-22,-20)
        if gendera==1:
            t.color(0.3,0.6,1)
        else:
            t.color(0.9,0.1,0.6)
        t.write(a,font=('none',20),align='right')
        t.goto(22,-20)
        if genderb==1:
            t.color(0.3,0.6,1)
        else:
            t.color(0.9,0.1,0.6)
        t.write(b,font=('none',20),align='left')
        t.ht()
        t.goto(-110,-40)
        if gendera==1:
            t.color(0.3,0.6,1)
        else:
            t.color(0.9,0.1,0.6)
        t.write(d,font=20)
        if y==1:
            t.goto(30,-40)
            if genderb==1:
                t.color(0.3,0.6,1)
            else:
                t.color(0.9,0.1,0.6)
            t.write('NO',font=('none',20))
        if y==2:
            t.goto(-10,40)
            t.color(0,0.6,0)
            t.write('NO',font=('none',15))
        if y==3:
            t.goto(30,-40)
            t.color(0.3,0.6,1)
            t.write('I have already loved another girl',font=('none',8))
            t.goto(30,-60)
            t.write('And you have already loved another boy,too',font=('none',8))
        if y==4 or z==1:
            for aa in range(50):
                t.goto(random.randint(-300,300),random.randint(-300,300))
                t.color(random.randint(0,30)*0.01,random.randint(60,100)*0.01,random.randint(0,30)*0.01)
                t.write('太过分了',font=('Arial',30))
        if y==5:
            t.goto(30,-40)
            t.color(0.3,0.6,1)
            t.write('I have already loved another girl',font=('none',8))
        if y==6 and lyhbg!=1:
            t.goto(-25,-60)
            t.write('我有..点喜欢李潇曼？',font=('none',8),align='right')
        if y==7 and lyhbg!=1:
            t.goto(-25,-60)
            t.write('我爱娄文喆',font=('none',15),align='right')
        if y==8 and lyhbg!=1:
            t.goto(-25,-60)
            t.write('我喜欢娄文喆',font=('none',15),align='right')
        if lyhbg==1 and a=='罗奕恒' and (y==6 or y==7 or y==8):
            t.goto(-25,-60)
            t.write('我是双性恋',font=('none',15),align='right')
        if y==9 and z!=1:
            t.speed(0)
            for k in range(20):
                n=random.randint(-300,300)
                m=random.randint(-300,300)
                t.color(random.randint(80,100)*0.01,random.randint(0,20)*0.01,random.randint(0,100)*0.01)
                t.up()
                t.goto(n,m)
                t.down()
                t.begin_fill()
                t.circle(10,195)
                t.goto(n-16,m-11)
                t.goto(n-12,m-18)
                t.goto(n-8,m-23)
                t.goto(n-4,m-27)
                t.goto(n,m-30)
                t.up()
                t.goto(n,m)
                t.down()
                t.right(195)
                t.circle(-10,195)
                t.goto(n+16,m-11)
                t.goto(n+12,m-18)
                t.goto(n+8,m-23)
                t.goto(n+4,m-27)
                t.goto(n,m-30)
                t.end_fill()
                t.right(-195)
            t.speed(6)
    x=input("input 1 for restart")
    if gendera!=0:
        t.ht()
        t.color('white')
        t.pensize(5000)
        t.goto(0,0)
        t.down()
        t.goto(1,0)
        t.up()
        t.goto(0,0)
    if x!='1':break
turtle.bye()
