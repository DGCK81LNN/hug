from random import random,randint,choice
import turtle
import time
lyhgl=0
lyhbl=0
lyhbg=0
times=0
yellow=0
t1=0.5
w=0
x=""
a=""
b=""
boys=["wyx","WYX","王翊轩","mqr","MQR","孟庆睿","cwjy","CWJY","陈王俊逸","csy","CSY","陈思源","qt","QT","齐天","ht","HT","胡涛","jbh","JBH","靳博涵","zhy","ZHY","张泓洋","lcp","LCP","刘传鹏","cxy","CXY","陈旭阳","zbh","ZBH","张博涵","dsd","DSD","杜圣迪","lyh","LYH","罗奕恒","lwz","LWZ","娄文喆","lzx","LZX","栾智翔","qzq","QZQ","祁子荃","ljs","LJS","李佳澍","yns","YNS","伊楠斯"]
girls=["ly","LY","刘屹","lyt","LYT","刘益同","wxr","WXR","武昕冉","wyz","WYZ","汪妍竹","wsy","WSY","王思颖","lxw","LXW","刘晓薇","hgx","HGX","黄淦欣","cyj","CYJ","陈奕伽","wty","WTY","吴亭颐","csh","CSH","陈思涵","lst","LST","刘书彤","lxm","LXM","李潇曼","hr","HR","韩睿","dr","DR","戴睿","yh","YH","运涵","hzy","HZY","胡泽伊","txy","TXY","田馨雅","cyy","CYY","崔玉莹","zzh","ZZH","赵梓涵","sjl","SJL","邵佳琳","clp","CLP","陈露萍","wtr","WTR","王泰然","lxr","LXR","李欣然","mgl","MGL","梅古里"]
ls=boys+girls
rd=["random","rd","rand","r"]
TITLE="抱一抱_ver1.7.3"
def heart(n,m):
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
    t.up()
def rdperson():
    return choice(ls)
def conv(x1,x2,x3,a):#首字母转换器
    if a in [x1,x2]:
        return x3
    else:
        return a
def per(text1,text2):
    while True:
        if mode=="2":
            a="r"
        else:
            a=t.screen.textinput(TITLE,text1)
        if ee=="1" and a in ["mgl","MGL","梅古里","yns","YNS","伊楠斯"]:
            p("啊这，二刺螈?")
        if ee=="1" and a in["wyh","WYH","王沿红"]:
            p("? ? ?")
        if a in rd or (a=="" and mode=="1"):
            a=rdperson()
        for o in range(42):
            a=conv(ls[0+3*o],ls[1+3*o],ls[2+3*o],a)
        if ee=="2" and a in ["梅古里","伊楠斯"]:#拦截器a
            a=""
        if a in boys:
            gendera=1
        elif a in girls:
            gendera=2
        else:
            p(text2)
            gendera=0
        if gendera in [1,2]:
            break
    return a,gendera
def p(text,end="\n"):
    t.color("black")
    global w
    t.up()
    t.goto(0,300-w)
    w+=18
    t.write(text,True,"center",font=("微软雅黑",15))
    time.sleep(t1)
t.screen.title(TITLE)
mode=t.screen.textinput(TITLE,"按Enter继续")
t=turtle.Turtle()
if mode in ["1","2"]:
    t1=0.2
    if mode=="1":
        p("Fast mode on")
    if mode=="2":
        p("Auto mode on")
p("FOR TFLS 初中部 17级-20届8班同学")
p("Made by 孟庆睿")
p("人名请写中文或拼音首字母!")
if mode=="2":
    ee=choice(["1","2"])
else:
    while True:
        ee=t.screen.textinput(TITLE,"是否开启彩蛋模式 (1)是 (2)否 输入一个数字进行选择")
        if ee in rd or (ee=="" and mode=="1"):
            ee=choice(["1","2"])
        if ee in ["1","2"]:#eastereggs
            break
#a for hugger;b for huggee;gendera for hugger;genderb for huggee;1 for boys;2 for girls
while True:
    y=0
    z=0
    per1=per("你的名字:","你不是TFLS 17届8班同学,请重新输入")
    a=per1[0]
    gendera=per1[1]
    per2=per("你想拥抱谁:","你想抱的人不在TFLS 17届8班,请重新输入")
    b=per2[0]
    genderb=per2[1]
    rdsay=["","","","","我是"+rdperson(),"我叫"+rdperson(),"我喜欢你","我喜欢上"+b,"我完全爱上"+b,"我喜欢"+b,"我想抱你","我想上"+b]
    if mode=="2":
        d=choice(rdsay)
    elif a!=b:
        d=t.screen.textinput(TITLE,"你想对"+b+"说什么?")
        if d in rd or (d=="" and mode=="1"):
            d=choice(rdsay)
    else:
        d=""
    if b in ["刘屹","刘益同","武昕冉","汪妍竹","王思颖","刘晓薇","黄淦欣","陈奕伽","吴亭颐","陈思涵","刘书彤","李潇曼","韩睿","戴睿","运涵","胡泽伊","田馨雅","崔玉莹","赵梓涵","邵佳琳","陈露萍","王泰然","李欣然","梅古里"]:
        genderb=2    
    if a==b:
        p(a+"自'抱'自弃")
    else:
        if genderb==2 and ee=="1" and (d[0:4]=="我喜欢上" or d[0:4]=="我愿意上" or d[0:3]=="我想上" or d[0:3]=="我爱上"):
            p(TITLE+":“我还是白的吧”")#easteregg1
            y=11
        elif b=="孟庆睿":        
            if a=="武昕冉":
                p("孟庆睿紧紧地抱住了你")
                p("他充满爱意地凝视着你")
                p("他抚摸了一下你的头")
                p("他用双手托住你的大腿和腰背,轻轻地把你抱了起来")
                y=9
            elif a=="梅古里":
                p("你抱住了创造了你的“上帝”")
                p("他的初一下学期时的回忆、幻想、心理、人格与你发生了强烈的共鸣")
            elif a=="伊楠斯":
                p("你抱住了创造了你的“上帝”")
                p("他的初二初三时的回忆、幻想、心理、人格与你发生了强烈的共鸣")
            elif gendera==1:
                p("你抱了孟庆睿一下")
                p("他轻轻地闭上了眼睛，对你说:'You're a gay.'")
            elif d in ["我是WXR","我是wxr","我是武昕冉","把我当成WXR吧","把我当成wxr吧","把我当成武昕冉吧","把我当成WXR","把我当成wxr","把我当成武昕冉","我也爱你","我也是WXR","我也是wxr","我也是武昕冉","我叫WXR","我叫wxr","我叫武昕冉","我也叫WXR","我也叫wxr","我也叫武昕冉","我是WXR变的","我是wxr变的","我是武昕冉变的","I am wxr","I'm wxr","I am WXR","I'm WXR"]:
                p("孟庆睿紧紧地抱住了你")
                p("他充满爱意地凝视着你,仿佛真的在抱着武昕冉")
                p("他抚摸了一下你的头")
                p("他用双手托住你的大腿和腰背,轻轻地把你抱了起来")
                y=9
            elif a in["李潇曼","王思颖","戴睿"]:
                p("你抱了孟庆睿一下")
                p("他被吓了一大跳,但面色依然冷漠")
                p("他说:'我等的并不是你。'")
                y=5
            elif a=="刘屹":
                p("你抱了孟庆睿一下")
                p("他被吓了一大跳,但面色依然冷漠")
                p("他说:'你就是那列不在铁轨上跑的火车吗?'")
                y=3
            else:
                p("你抱了孟庆睿一下")
                p("他用力地扭动了他的身体,推了你的肩膀")
                p("你被狠狠地推开了")
                y=1
        elif b=="武昕冉"and a not in ["梅古里","伊楠斯"]:
            if a=="孟庆睿":
                p("你抱向了你心爱的武昕冉")
                p("她向下一躲,从你的胸前逃走了")
                y=1
            elif a=="娄文喆":
                p("你抱了娇小的武昕冉一下")
                p("她推开了你,你喊道:'大仙快来管管你媳妇儿.'却适得其反")
                p("你试图逃跑,但他们俩追打了你很久")
                p("孟庆睿像一堵墙一样出现在你面前,后面的武昕冉也追了上来")
                p("你被逮到后门与后墙之间的缝隙中,怎么推门都推不动")
                p("武昕冉向你逼近,你已无路可逃")
                p("她捏了捏你的脸,打了你几下")
                y=1
            elif a=="运涵" and ee=="1":#easteregg2
                p("你抱住了娇小的武昕冉")
                p("她紧紧地贴着你")
                p(r"(=  )时-=-空- [\]发 \生[  错 ]乱")
                p("你与她被传送回2019年4月23日的小外")
                p(r"(=  )时-=-空- [\]发 \生[  错 ]乱")
                p("你与她被传送回2018年4月24日的小外")
                p(r"-==奇  \ 怪 \|的 ;'日';子")
            elif gendera==1:
                p("你抱住了娇小的武昕冉")
                p("几秒后,一个沉重的脚步声从你后面靠近")
                p("你被狠狠地推了一下,倒在了地上,晕倒了")
                y=2
            else:
                p("你抱住了娇小的武昕冉")
                p("几秒后,一个沉重的脚步声从你后面靠近")
                p("你感到了一丝不祥的预感.但什么也没发生")
        elif b=="刘屹" and a not in ["梅古里","伊楠斯"]:
            if a=="陈王俊逸":
                p("你与刘屹紧紧地拥抱在了一起")
                p("你与她深情地对视着,害羞地低下了头")
                p("你坐回了你的座位")
                p("她弯下腰来,轻轻地抚摸了一下你的后背")
                p("你倚靠在她胸前,甜蜜贯穿全身,心中幸福无比")
                y=9
            elif gendera==1:
                p("你刚抱到刘屹,她就与陈王俊逸一起对你说了‘太过分了’")
                p("你试图逃跑,但他们俩追打了你很久")
                y=4
            else:
                p("你抱住了娇小的"+b)
        elif b=="陈王俊逸" and a not in ["梅古里","伊楠斯"]:
            if a=="刘屹":
                p("你与陈王俊逸紧紧地拥抱在了一起")
                p("你与他深情地对视着,害羞地低下了头")
                p("他坐回了他的座位")
                p("你弯下腰来,轻轻地抚摸了一下他的后背")
                p("他倚靠在你胸前,甜蜜贯穿全身,心中幸福无比")
                y=9
            elif gendera==2:
                p("你刚抱到陈王俊逸,他就与刘屹一起对你说了‘太过分了’")
                p("你试图逃跑,但他们俩追打了你很久")
                y=4
            else:
                p("你抱住了"+b)
        elif b=="罗奕恒" and a not in ["梅古里","伊楠斯"]:
            if a=="戴睿" or a=="李潇曼":
                p("你抱住了罗奕恒")
                p("他差点当场被吓死")
            elif a=="武昕冉":
                p("你抱住了罗奕恒")
                p("他差点当场被吓死")
                p("他说:'最想被你抱的并不是我'")
            elif gendera==2:
                p("你抱住了罗奕恒")
                p("他吓了一大跳")
            else:
                p("你抱住了"+b)
        elif b=="戴睿" and a not in ["梅古里","伊楠斯"]:
            if a=="罗奕恒":
                p("你.")
                p("根.")
                p("本....")
                p("不.....")
                p("敢.")
                p("去....")
                p("抱.")
                p("戴.........")
                p("睿.")
                p(".........")
                p("........")
                p(".")
                p("")
            else:
                p("你抱住了"+b)
        elif b=="李潇曼" and a not in["梅古里","伊楠斯"]:
            if a=="罗奕恒" and d in ["我喜欢你","我喜欢LXM","我喜欢lxm","我喜欢李潇曼","我爱上你","我爱上LXM","我爱上lxm","我爱上李潇曼","我爱你","我爱LXM","我爱lxm","我爱李潇曼","我喜欢上你","我喜欢上LXM","我喜欢上lxm","我喜欢上李潇曼","I love lxm","I love LXM","I love you","I like lxm","I like LXM"]:
                p("你那是馋她身子")
                p("你下贱")
                lyhgl=1
                y=6
            elif a=="孟庆睿":
                p("你抱住了娇小的李潇曼")
                p("她脸红了,对你喊道:'What f**k with your eyes?'")
            elif a=="杜圣迪":
                p("你抱住了娇小的李潇曼")
                p("她脸红了,对你喊道:'渣男!滚!'")
                p("yh wty甩你了?")
                p("你绝对是馋我身子")
                y=1
            elif a=="靳博涵":
                p("你抱住了娇小的李潇曼")
                p("她脸红了,对你喊道:'流氓!滚!'")
                p("我听mqr说,你和杜圣迪对我有大胆的想法")
                p("你绝对是馋我身子")
                y=1
            elif gendera==1:
                p("你抱住了娇小的李潇曼")
                p("她脸红了,对你喊道:'别碰我!'")
            else:
                p("你抱住了"+b)
        elif b=="娄文喆" and a not in ["梅古里","伊楠斯"]:
            if a=="罗奕恒":
                p("你抱住了娄文喆")
                if d in["我完全爱上你","我完全爱上LWZ","我完全爱上lwz","我完全爱上娄文喆"]:
                    p("他瞪大了双眼看着你，脸上露出滑稽的微笑")
                    lyhbl=1
                    y=7
                elif d in["我喜欢你","我喜欢LWZ","我喜欢lwz","我喜欢娄文喆"]:
                    p("他瞪大了双眼看着你，脸上露出滑稽的微笑")
                    lyhbl=1
                    y=8
                else:
                    p("他好像已经习惯了")
            elif a=="武昕冉":
                p("你抱了娄文喆一下")
                p("他拍了你一下,他喊道:'大仙快来管管你媳妇儿.'")
                p("他试图逃跑,孟庆睿也赶了过来")
                p("孟庆睿像一堵墙一样出现在他面前,你从他的后面追了上来")
                p("他被逮到后门与后墙之间的缝隙中,怎么推门都推不动")
                p("你向他逼近,他已无路可逃")
                p("你捏了捏他的脸,打了你几下")
                y=1
            else:
                p("你抱住了"+b)
        elif b=="伊楠斯":
            if a=="梅古里":
                p("你从水中跑向站在沙滩上看着大海的伊楠斯,扑过去抱住了他")
                p("你与他紧紧地贴在了一起,可以感知到彼此的心跳在加速")
                p("他托住你的腰和大腿，用公主抱的姿势把你抱了起来")
                p("过了一小会儿,他轻轻地把你放在沙滩上,躺在你身旁,拉着你的手")
                p("你看着辽阔的大海,回忆起今年春夏和他的每一次共处")
                y=9
            elif a=="孟庆睿":
                p("你抱住了你的幻想")
                p("你的初二初三时的回忆、幻想、心理、人格与他发生了强烈的共鸣")
            else:
                p("你撞上了小说与现实之间的次元壁")
        elif b=="梅古里":
            if a=="伊楠斯":
                p("梅古里从水中跑向站在沙滩上看着大海的你,扑过去抱住了你")
                p("你与她紧紧地贴在了一起,可以感知到彼此的心跳在加速")
                p("你托住她的腰和大腿，用公主抱的姿势把她抱了起来")
                p("过了一小会儿,你轻轻地把她放在沙滩上,躺在她身旁,拉着她的手")
                p("你看着辽阔的大海,回忆起今年春夏和她的每一次共处")
                y=9
            elif a=="孟庆睿":
                p("你抱住了你的幻想")
                p("你的初一下学期时的回忆、幻想、心理、人格与她发生了强烈的共鸣")
            else:
                p("你撞上了小说与现实之间的次元壁")
        elif b=="杜圣迪" and a not in ["梅古里","伊楠斯"]:
            if a=="吴亭颐":
                p("你抱住了你的杜圣迪")
                p("“I love you.”")
                y=9
            elif gendera==1:
                p("你抱住了"+b)
                p("他对你说:“基佬，来VANVAN”")
                y=10
            else:
                p("你抱住了"+b)
        elif b=="吴亭颐" and a not in ["梅古里","伊楠斯"]:
            if a=="杜圣迪":
                p("你抱住了你的吴亭颐")
                p("“I love you.”")
                y=9
            elif gendera==1:
                p("你抱住了"+b)
                p("她对你说:“你不配做我的男人”")
                y=1
            else:
                p("你抱住了"+b)
        elif b=="运涵" and a not in ["梅古里","伊楠斯"]:
            if a=="武昕冉" and ee=="1":#easteregg3
                p("你抱住了"+b)
                p("她紧紧地贴着你")
                p(r"(=  )时-=-空- [\]发 \生[  错 ]乱")
                p("你与她被传送回2019年4月23日的小外")
                p(r"(=  )时-=-空- [\]发 \生[  错 ]乱")
                p("你与她被传送回2018年4月24日的小外")
                p(r"-==奇  \ 怪 \|的 ;'日';子")
            elif a=="杜圣迪":
                p("你抱住了"+b)
                p("她对你说:“渣男，又来玩儿我了!”")
            else:
                p("你抱住了"+b)
        else:
            if a in ["梅古里","伊楠斯"]:
                p("你撞上了小说与现实之间的次元壁")
            else:
                p("你抱住了"+b)
    if gendera==1 and genderb==1 and a not in["梅古里","伊楠斯"] and b not in["梅古里","伊楠斯"]:
        if b!="孟庆睿":
            p("Are you a gay?")
    if gendera==2 and genderb==2 and a not in["梅古里","伊楠斯"] and b not in["梅古里","伊楠斯"]:
        if a!=b:
            p("Are you a lesbian?")
    if a=="武昕冉" and genderb==1 and b not in["梅古里","伊楠斯","孟庆睿"]:
        y=2
        if b=="陈王俊逸":
            z=1                            
    if ((a=="刘屹" and genderb==1 and b!="陈王俊逸") or (a=="陈王俊逸" and genderb==2 and b!="刘屹")) and a not in["梅古里","伊楠斯"] and b not in["梅古里","伊楠斯"]:
        p("远处传来一声:'你怎么能这样?太过分了'")
        z=1
    if lyhgl==1 and lyhbl==1:
        lyhbg=1
    t.up()
    t.st()
    t.seth(90)
    t.speed(6)          
    t.color("red")
    t.pensize(1)
    heart(0,0)
    t.goto(-22,-20)
    if gendera==1:
        t.color(0.3,0.6,1)
    else:
        t.color(0.9,0.1,0.6)
    t.write(a,font=("none",20),align="right")
    t.goto(22,-20)
    if genderb==1:
        t.color(0.3,0.6,1)
    else:
        t.color(0.9,0.1,0.6)
    t.write(b,font=("none",20))
    t.ht()
    t.goto(-22,-45)
    if gendera==1:
        t.color(0.3,0.6,1)
    else:
        t.color(0.9,0.1,0.6)
    t.write(d,font=("none",20),align="right")
    if y==1:
        t.goto(30,-40)
        if genderb==1:
            t.color(0.3,0.6,1)
        else:
            t.color(0.9,0.1,0.6)
        t.write("NO",font=("none",20))
    if y==2:
        t.goto(-10,40)
        t.color(0,0.6,0)
        t.write("NO",font=("none",15))
    if y==3:
        t.goto(30,-40)
        t.color(0.3,0.6,1)
        t.write("I have already loved another girl",font=("none",8))
        t.goto(30,-60)
        t.write("And you have already loved another boy,too",font=("none",8))
    if y==4 or z==1:
        for aa in range(50):
            t.goto(randint(-300,300),randint(-300,300))
            t.color(randint(0,30)*0.01,randint(60,100)*0.01,randint(0,30)*0.01)
            t.write("太过分了",font=("Arial",30))
    if y==5:
        t.goto(30,-40)
        t.color(0.3,0.6,1)
        t.write("I have already loved another girl",font=("none",8))
    if y==6 and lyhbg!=1:
        t.goto(-25,-60)
        t.write("我有..点喜欢李潇曼？",font=("none",8),align="right")
    if y==7 and lyhbg!=1:
        t.goto(-25,-60)
        t.write("我爱娄文喆",font=("none",15),align="right")
    if y==8 and lyhbg!=1:
        t.goto(-25,-60)
        t.write("我喜欢娄文喆",font=("none",15),align="right")
    if lyhbg==1 and a=="罗奕恒" and 6<=y<=8:
        t.goto(-25,-60)
        t.write("我是双性恋",font=("none",15),align="right")
    if y==9 and z!=1:
        t.speed(0)
        for k in range(10):
            t.color(randint(80,100)*0.01,randint(0,20)*0.01,randint(0,100)*0.01)
            heart(randint(-300,300),randint(-300,300))
        t.speed(6)
    if y==10:
        t.pensize(5)
        for k in range(20):
            t.seth(0)
            n=randint(-300,300)
            m=randint(-300,300)
            o=randint(20,30)
            t.color(randint(20,40)*0.01,randint(20,40)*0.01,randint(80,100)*0.01)
            t.up()
            t.goto(n,m)
            t.down()
            t.circle(o,360)
            t.up()
            t.goto(n+0.7*o,m+1.7*o)
            t.down()
            t.goto(n+3*o,m+4*o)
            t.goto(n+1.7*o,m+3.9*o)
            t.goto(n+3*o,m+4*o)
            t.goto(n+2.9*o,m+2.7*o)
            t.up()
    if y==11:#yellow
        if yellow<=0.99:
            yellow+=0.01
        t.screen.title(TITLE+"Yellow")
        t.goto(0,150)
        t.color(1,0.82,0.1)
        t.write("? ? ? ? ? ?",font=("none",30),align="center")
        t.goto(30,-45)
        t.color(0.9,0.1,0.6)
        t.write("啊--啊---啊你不要过来呀",font=("none",12))
        t.goto(0,0)
        time.sleep(2)
        for k in range(100):
            time.sleep(0.02)
            t.screen.bgcolor(1,1,1-yellow-0.01*k)
            if 1-yellow-0.01*k<=0.01:
                break
    times+=1
    if mode=="2":
        ee=choice(["1","2"])
    elif ee=="1":
        while True:
            x=t.screen.textinput(TITLE,"(1)重新开始 (2)退出 (3)关闭彩蛋模式并重新开始 输入一个数字进行选择")
            if x in rd:
                x=choice(["1","3"])
            if x in ["1","2","3"]:
                break
            if mode=="1" and x=="":
                break
        if x=="3":
            ee="2"
    else:
        while True:
            x=t.screen.textinput(TITLE,"(1)重新开始 (2)退出 (3)开启彩蛋模式并重新开始 输入一个数字进行选择")
            if x in rd:
                x=choice(["1","3"])
            if x in ["1","2","3"]:
                break
            if mode=="1" and x=="":
                break
        if x=="3":
            ee="1"
    if mode=="2":
        time.sleep(0.5)
    w=0
    t.clear()
    t.screen.bgcolor(1,1,1-yellow)
    t.screen.title(TITLE)
    if x=="2":
        break
t.screen.bye()
