import random
import turtle
lyhgl=0
lyhbl=0
lyhbg=0
print("人名请写中文或拼音首字母!")
#a for hugger;b for huggee;gendera for hugger;genderb for huggee;1 for boys;2 for girls
while True:
    print('抱一抱_VER1.6')
    input('按Enter继续(下同)')
    input('FOR TFLS 初中部 17级-20届8班同学')
    input('Made by 孟庆睿')
    y=0
    z=0
    while True:
        w1=0
        a=input('你的名字:')
        if a!="":
            w1=1
        if w1==1:break    
    if a in ['wyx','WYX']:
        a='王翊轩'
    if a in ['mqr','MQR']:
        a='孟庆睿'
    if a in ['cwjy','CWJY']:
        a='陈王俊逸'
    if a in ['csy','CSY']:
        a='陈思源'
    if a in ['qt','QT']:
        a='齐天'
    if a in ['ht','HT']:
        a='胡涛'
    if a in ['jbh','JBH']:
        a='靳博涵'
    if a in ['zhy','ZHY']:
        a='张泓洋'
    if a in ['lcp','LCP']:
        a='刘传鹏'
    if a in ['cxy','CXY']:
        a='陈旭阳'
    if a in ['zbh','ZBH']:
        a='张博涵'
    if a in ['dsd','DSD']:
        a='杜圣迪'
    if a in ['lyh','LYH']:
        a='罗奕恒'
    if a in ['lwz','LWZ']:
        a='娄文喆'
    if a in ['lzx','LZX']:
        a='栾智翔'
    if a in ['qzq','QZQ']:
        a='祁子荃'
    if a in ['ljs','LJS']:
        a='李佳澍'
    if a in ['yns','YNS']:
        a='伊楠斯'
    if a in ['ly','LY']:
        a='刘屹'
    if a in ['lyt','LYT']:
        a='刘益同'
    if a in ['wxr','WXR']:
        a='武昕冉'
    if a in ['wyz','WYZ']:
        a='汪妍竹'
    if a in ['wsy','WSY']:
        a='王思颖'
    if a in ['lxw','LXW']:
        a='刘晓薇'
    if a in ['hgx','HGX']:
        a='黄淦欣'
    if a in ['cyj','CYJ']:
        a='陈奕伽'
    if a in ['wty','WTY']:
        a='吴亭颐'
    if a in ['csh','CSH']:
        a='陈思涵'
    if a in ['lst','LST']:
        a='刘书彤'
    if a in ['lxm','LXM']:
        a='李潇曼'
    if a in ['hr','HR']:
        a='韩睿'
    if a in ['dr','DR']:
        a='戴睿'
    if a in ['yh','YH']:
        a='运涵'
    if a in ['hzy','HZY']:
        a='胡泽伊'
    if a in ['txy','TXY']:
        a='田馨雅'
    if a in ['cyy','CYY']:
        a='崔玉莹'
    if a in ['zzh','ZZH']:
        a='赵梓涵'
    if a in ['sjl','SJL']:
        a='邵佳琳'
    if a in ['clp','CLP']:
        a='陈露萍'
    if a in ['wtr','WTR']:
        a='王泰然'
    if a in ['lxr','LXR']:
        a='李欣然'
    if a in ['mgl','MGL']:
        a='梅古里'
    if a in ['王翊轩','孟庆睿','陈王俊逸','陈思源','齐天','胡涛','靳博涵','张泓洋','刘传鹏','陈旭阳','张博涵','杜圣迪','罗奕恒','娄文喆','栾智翔','祁子荃','李佳澍','伊楠斯']:#去除了一大堆or
        gendera=1
    elif a in ['刘屹','刘益同','武昕冉','汪妍竹','王思颖','刘晓薇','黄淦欣','陈奕伽','吴亭颐','陈思涵','刘书彤','李潇曼','韩睿','戴睿','运涵','胡泽伊','田馨雅','崔玉莹','赵梓涵','邵佳琳','陈露萍','王泰然','李欣然','梅古里']:
        gendera=2
    else:
        print('你不是TFLS 17届8班同学')
        gendera=0
        genderb=0
        a=""
        b=""
        d=""
    if gendera==1 or gendera==2:
        while True:
            w1=0
            b=input('你想拥抱谁:')
            if b!="":
                w1=1
            if w1==1:break
        if b in ['wyx','WYX']:
            b='王翊轩'
        if b in ['mqr','MQR']:
            b='孟庆睿'
        if b in ['cwjy','CWJY']:
            b='陈王俊逸'
        if b in ['csy','CSY']:
            b='陈思源'
        if b in ['qt','QT']:
            b='齐天'
        if b in ['ht','HT']:
            b='胡涛'
        if b in ['jbh','JBH']:
            b='靳博涵'
        if b in ['zhy','ZHY']:
            b='张泓洋'
        if b in ['lcp','LCP']:
            b='刘传鹏'
        if b in ['cxy','CXY']:
            b='陈旭阳'
        if b in ['zbh','ZBH']:
            b='张博涵'
        if b in ['dsd','DSD']:
            b='杜圣迪'
        if b in ['lyh','LYH']:
            b='罗奕恒'
        if b in ['lwz','LWZ']:
            b='娄文喆'
        if b in ['lzx','LZX']:
            b='栾智翔'
        if b in ['qzq','QZQ']:
            b='祁子荃'
        if b in ['ljs','LJS']:
            b='李佳澍'
        if b in ['yns','YNS']:
            b='伊楠斯'
        if b in ['ly','LY']:
            b='刘屹'
        if b in ['lyt','LYT']:
            b='刘益同'
        if b in ['wxr','WXR']:
            b='武昕冉'
        if b in ['wyz','WYZ']:
            b='汪妍竹'
        if b in ['wsy','WSY']:
            b='王思颖'
        if b in ['lxw','LXW']:
            b='刘晓薇'
        if b in ['hgx','HGX']:
            b='黄淦欣'
        if b in ['cyj','CYJ']:
            b='陈奕伽'
        if b in ['wty','WTY']:
            b='吴亭颐'
        if b in ['csh','CSH']:
            b='陈思涵'
        if b in ['lst','LST']:
            b='刘书彤'
        if b in ['lxm','LXM']:
            b='李潇曼'
        if b in ['hr','HR']:
            b='韩睿'
        if b in ['dr','DR']:
            b='戴睿'
        if b in ['yh','YH']:
            b='运涵'
        if b in ['hzy','HZY']:
            b='胡泽伊'
        if b in ['txy','TXY']:
            b='田馨雅'
        if b in ['cyy','CYY']:
            b='崔玉莹'
        if b in ['zzh','ZZH']:
            b='赵梓涵'
        if b in ['sjl','SJL']:
            b='邵佳琳'
        if b in ['clp','CLP']:
            b='陈露萍'
        if b in ['wtr','WTR']:
            b='王泰然'
        if b in ['lxr','LXR']:
            b='李欣然'
        if b in ['mgl','MGL']:
            b='梅古里'
        if b in ['王翊轩','孟庆睿','陈王俊逸','陈思源','齐天','胡涛','靳博涵','张泓洋','刘传鹏','陈旭阳','张博涵','杜圣迪','罗奕恒','娄文喆','栾智翔','祁子荃','李佳澍','刘屹','刘益同','武昕冉','汪妍竹','王思颖','刘晓薇','黄淦欣','陈奕伽','吴亭颐','陈思涵','刘书彤','李潇曼','韩睿','戴睿','运涵','胡泽伊','田馨雅','崔玉莹','赵梓涵','邵佳琳','陈露萍','王泰然','李欣然','梅古里','伊楠斯']:      
            genderb=1
            if a!=b:
                d=input('你想对'+b+'说什么?')
            else:
                d=""
            if b in ['刘屹','刘益同','武昕冉','汪妍竹','王思颖','刘晓薇','黄淦欣','陈奕伽','吴亭颐','陈思涵','刘书彤','李潇曼','韩睿','戴睿','运涵','胡泽伊','田馨雅','崔玉莹','赵梓涵','邵佳琳','陈露萍','王泰然','李欣然','梅古里']:
                genderb=2    
            if a==b:
                print(a+"自'抱'自弃")
            else:
                if b=='孟庆睿':
                    if a=='武昕冉':
                        input("孟庆睿紧紧地抱住了你")
                        input("他充满爱意地凝视着你")
                        input("他抚摸了一下你的头")
                        input("他用双手托住你的大腿和腰背,轻轻地把你抱了起来")
                        y=9
                    elif a=='梅古里':
                        input("你抱住了创造了你的“上帝”")
                        input("他的初一下学期时的回忆、幻想、心理、人格与你发生了强烈的共鸣")
                    elif a=='伊楠斯':
                        input("你抱住了创造了你的“上帝”")
                        input("他的初二初三时的回忆、幻想、心理、人格与你发生了强烈的共鸣")
                    elif gendera==1:
                        input("你抱了孟庆睿一下")
                        input("他轻轻地闭上了眼睛，对你说:'You're a gay.'")
                    elif d in ["我是WXR","我是wxr","我是武昕冉","把我当成WXR吧","把我当成wxr吧","把我当成武昕冉吧","把我当成WXR","把我当成wxr","把我当成武昕冉","我也爱你","我也是WXR","我也是wxr","我也是武昕冉","我叫WXR","我叫wxr","我叫武昕冉","我也叫WXR","我也叫wxr","我也叫武昕冉","我是WXR变的","我是wxr变的","我是武昕冉变的"]:
                        input("孟庆睿紧紧地抱住了你")
                        input("他充满爱意地凝视着你,仿佛真的在抱着武昕冉")
                        input("他抚摸了一下你的头")
                        input("他用双手托住你的大腿和腰背,轻轻地把你抱了起来")
                        y=9
                    elif a in['李潇曼','王思颖','戴睿']:
                        input("你抱了孟庆睿一下")
                        input("他被吓了一大跳,但面色依然冷漠")
                        input("他说:'我等的并不是你。'")
                        y=5
                    elif a=='刘屹':
                        input("你抱了孟庆睿一下")
                        input("他被吓了一大跳,但面色依然冷漠")
                        input("他说:'你就是那列不在铁轨上跑的火车吗?'")
                        y=3
                    else:
                        input("你抱了孟庆睿一下")
                        input("他用力地扭动了他的身体,推了你的肩膀")
                        input("你被狠狠地推开了")
                        y=1
                elif b=='武昕冉' and a!='梅古里' and a!='伊楠斯':
                    if a=='孟庆睿':
                        input("你抱向了你心爱的武昕冉")
                        input("她向下一躲,从你的胸前逃走了")
                        y=1
                    elif a=='娄文喆':
                        input("你抱了娇小的武昕冉一下")
                        input("她推开了你,你喊道:'大仙快来管管你媳妇儿.'却适得其反")
                        input("你试图逃跑,但他们俩追打了你很久")
                        input("孟庆睿像一堵墙一样出现在你面前,后面的武昕冉也追了上来")
                        input("你被逮到后门与后墙之间的缝隙中,怎么推门都推不动")
                        input("武昕冉向你逼近,你已无路可逃")
                        input("她捏了捏你的脸,打了你几下")
                        y=1
                    elif a=='运涵':
                        input("你抱住了娇小的武昕冉")
                        input("她紧紧地贴着你")
                        input("(=  )时-=-空- [\]发 \生[  错 ]乱")
                        input("你与她被传送回2019年4月23日的小外")
                        input("(=  )时-=-空- [\]发 \生[  错 ]乱")
                        input("你与她被传送回2018年4月24日的小外")
                        input("-==奇  \ 怪 \|的 ;'日';子")
                    elif gendera==1:
                        input("你抱住了娇小的武昕冉")
                        input("几秒后,一个沉重的脚步声从你后面靠近")
                        input("你被狠狠地推了一下,倒在了地上,晕倒了")
                        y=2
                    else:
                        input("你抱住了娇小的武昕冉")
                        input("几秒后,一个沉重的脚步声从你后面靠近")
                        input("你感到了一丝不祥的预感.但什么也没发生")
                elif b=='刘屹' and a!='梅古里' and a!='伊楠斯':
                    if a=='陈王俊逸':
                        input("你与刘屹紧紧地拥抱在了一起")
                        input("你与她深情地对视着,害羞地低下了头")
                        input("你坐回了你的座位")
                        input("她弯下腰来,轻轻地抚摸了一下你的后背")
                        input("你倚靠在她胸前,甜蜜贯穿全身,心中幸福无比")
                        y=9
                    elif gendera==1:
                        input("你刚抱到刘屹,她就与陈王俊逸一起对你说了‘太过分了’")
                        input("你试图逃跑,但他们俩追打了你很久")
                        y=4
                    else:
                        input("你抱住了娇小的"+b)
                elif b=='陈王俊逸' and a!='梅古里' and a!='伊楠斯':
                    if a=='刘屹':
                        input("你与陈王俊逸紧紧地拥抱在了一起")
                        input("你与他深情地对视着,害羞地低下了头")
                        input("他坐回了他的座位")
                        input("你弯下腰来,轻轻地抚摸了一下他的后背")
                        input("他倚靠在你胸前,甜蜜贯穿全身,心中幸福无比")
                        y=9
                    elif gendera==2:
                        input("你刚抱到陈王俊逸,他就与刘屹一起对你说了‘太过分了’")
                        input("你试图逃跑,但他们俩追打了你很久")
                        y=4
                    else:
                        input("你抱住了"+b)
                elif b=='罗奕恒' and a!='梅古里' and a!='伊楠斯':
                    if a=='戴睿' or a=='李潇曼':
                        input("你抱住了罗奕恒")
                        input("他差点当场被吓死")
                    elif a=='武昕冉':
                        input("你抱住了罗奕恒")
                        input("他差点当场被吓死")
                        input("他说:'最想被你抱的并不是我'")
                    elif gendera==2:
                        input("你抱住了罗奕恒")
                        input("他吓了一大跳")
                    else:
                        input("你抱住了"+b)
                elif b=='戴睿' and a!='梅古里' and a!='伊楠斯':
                    if a=='罗奕恒':
                        input('你.')
                        input('根.')
                        input('本....')
                        input('不.....')
                        input('敢.')
                        input('去....')
                        input('抱.')
                        input('戴.........')
                        input('睿.')
                        input('.........')
                        input('........')
                        input('.')
                        input('')
                    else:
                        input("你抱住了"+b)
                elif b=='李潇曼' and a!='梅古里' and a!='伊楠斯':
                    if a=='罗奕恒' and d in ["我喜欢你","我喜欢LXM","我喜欢lxm","我喜欢李潇曼","我爱上你","我爱上LXM","我爱上lxm","我爱上李潇曼","我爱你","我爱LXM","我爱lxm","我爱李潇曼","我喜欢上你","我喜欢上LXM","我喜欢上lxm","我喜欢上李潇曼"]:
                        input("你那是馋她身子")
                        input("你下贱")
                        lyhgl=1
                        y=6
                    elif a=='孟庆睿':
                        input("你抱住了娇小的李潇曼")
                        input("她脸红了,对你喊道:'What f**k with your eyes?'")
                    elif a=='杜圣迪':
                        input("你抱住了娇小的李潇曼")
                        input("她脸红了,对你喊道:'渣男!滚!'")
                        input("yh wty甩你了?")
                        input("你绝对是馋我身子")
                        y=1
                    elif a=='靳博涵':
                        input("你抱住了娇小的李潇曼")
                        input("她脸红了,对你喊道:'流氓!滚!'")
                        input("我听mqr说,你和杜圣迪对我有大胆的想法")
                        input("你绝对是馋我身子")
                        y=1
                    elif gendera==1:
                        input("你抱住了娇小的李潇曼")
                        input("她脸红了,对你喊道:'别碰我!'")
                    else:
                        input("你抱住了"+b)
                elif b=='娄文喆' and a!='梅古里' and a!='伊楠斯':
                    if a=='罗奕恒':
                        if d in["我完全爱上你","我完全爱上LWZ","我完全爱上lwz","我完全爱上娄文喆"]:
                            input("你抱住了娄文喆")
                            input("他瞪大了双眼看着你，脸上露出滑稽的微笑")
                            lyhbl=1
                            y=7
                        elif d in["我喜欢你","我喜欢LWZ","我喜欢lwz","我喜欢娄文喆"]:
                            input("你抱住了娄文喆")
                            input("他瞪大了双眼看着你，脸上露出滑稽的微笑")
                            lyhbl=1
                            y=8
                        else:
                            input("你抱住了娄文喆")
                            input("他好像已经习惯了")
                    elif a=='武昕冉':
                        input("你抱了娄文喆一下")
                        input("他拍了你一下,他喊道:'大仙快来管管你媳妇儿.'")
                        input("他试图逃跑,孟庆睿也赶了过来")
                        input("孟庆睿像一堵墙一样出现在他面前,你从他的后面追了上来")
                        input("他被逮到后门与后墙之间的缝隙中,怎么推门都推不动")
                        input("你向他逼近,他已无路可逃")
                        input("你捏了捏他的脸,打了你几下")
                        y=1
                    else:
                        input("你抱住了"+b)
                elif b=='伊楠斯':
                    if a=='梅古里':
                        input("你从水中跑向站在沙滩上看着大海的伊楠斯,扑过去抱住了他")
                        input("你与他紧紧地贴在了一起,可以感知到彼此的心跳在加速")
                        input("他托住你的腰和大腿，用公主抱的姿势把你抱了起来")
                        input("过了一小会儿,他轻轻地把你放在沙滩上,躺在你身旁,拉着你的手")
                        input("你看着辽阔的大海,回忆起今年春夏和他的每一次共处")
                        y=9
                    elif a=='孟庆睿':
                        input("你抱住了你的幻想")
                        input("你的初二初三时的回忆、幻想、心理、人格与他发生了强烈的共鸣")
                    else:
                        input("你撞上了小说与现实之间的次元壁")
                elif b=='梅古里':
                    if a=='伊楠斯':
                        input("梅古里从水中跑向站在沙滩上看着大海的你,扑过去抱住了你")
                        input("你与她紧紧地贴在了一起,可以感知到彼此的心跳在加速")
                        input("你托住她的腰和大腿，用公主抱的姿势把她抱了起来")
                        input("过了一小会儿,你轻轻地把她放在沙滩上,躺在她身旁,拉着她的手")
                        input("你看着辽阔的大海,回忆起今年春夏和她的每一次共处")
                        y=9
                    elif a=='孟庆睿':
                        input("你抱住了你的幻想")
                        input("你的初一下学期时的回忆、幻想、心理、人格与她发生了强烈的共鸣")
                    else:
                        input("你撞上了小说与现实之间的次元壁")
                elif b=='杜圣迪' and a not in ['梅古里','伊楠斯']:
                    if a=='吴亭颐':
                        input("你抱住了你的杜圣迪")
                        input("“I love you.”")
                        y=9
                    elif gendera==1:
                        input("你抱住了"+b)
                        input("他对你说:“基佬，来VANVAN”")
                        y=10
                    else:
                        input("你抱住了"+b)
                elif b=='吴亭颐' and a not in ['梅古里','伊楠斯']:
                    if a=='杜圣迪':
                        input("你抱住了你的吴亭颐")
                        input("“I love you.”")
                        y=9
                    elif gendera==1:
                        input("你抱住了"+b)
                        input("她对你说:“你不配做我的男人”")
                        y=1
                    else:
                        input("你抱住了"+b)
                elif b=='运涵' and a not in ['梅古里','伊楠斯']:
                    if a=='武昕冉':
                        input("你抱住了"+b)
                        input("她紧紧地贴着你")
                        input("(=  )时-=-空- [\]发 \生[  错 ]乱")
                        input("你与她被传送回2019年4月23日的小外")
                        input("(=  )时-=-空- [\]发 \生[  错 ]乱")
                        input("你与她被传送回2018年4月24日的小外")
                        input("-==奇  \ 怪 \|的 ;'日';子")
                    else:
                        input("你抱住了"+b)
                else:
                    if a=='梅古里' or a=='伊楠斯':
                        input("你撞上了小说与现实之间的次元壁")
                    else:
                        input("你抱住了"+b)
        else:
            print('你想抱的人不在TFLS 17届8班')
            gendera=0
            b=""
            d=""
            genderb=0
    if gendera==1 and genderb==1 and a not in['梅古里','伊楠斯'] and b not in['梅古里','伊楠斯']:
        if b!='孟庆睿':
            print("Are you a gay?")
    if gendera==2 and genderb==2 and a not in['梅古里','伊楠斯'] and b not in['梅古里','伊楠斯']:
        if a!=b:
            print("Are you a lesbian?")
    if a=='武昕冉' and genderb==1 and b not in['梅古里','伊楠斯','孟庆睿']:
        y=2
        if b=='陈王俊逸':
            z=1                            
    if ((a=='刘屹' and genderb==1 and b!='陈王俊逸') or (a=='陈王俊逸' and genderb==2 and b!='刘屹')) and a not in['梅古里','伊楠斯'] and b not in['梅古里','伊楠斯']:
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
        if lyhbg==1 and a=='罗奕恒' and 6<=y<=8:
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
        if y==10:
            t.pensize(5)
            for k in range(20):
                t.seth(0)
                n=random.randint(-300,300)
                m=random.randint(-300,300)
                o=random.randint(20,30)
                t.color(random.randint(20,40)*0.01,random.randint(20,40)*0.01,random.randint(80,100)*0.01)
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
    while True:
        w2=0
        x=input("input 1 for restart  input 2 for exit")
        if x in ['1','2']:
            w2=1
        if w2==1:break
    t.clear()
    if x=='2':break
turtle.bye()
