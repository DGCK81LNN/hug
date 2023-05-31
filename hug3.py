# -*- coding: utf-8 -*-
import turtle
import random
import time
import json
import math
import re

VERSION = 'v3.3.3 fix'
DEBUG_GENDERS = {1: '男', 2: '女'}
COLORS = {
    1: "#48F",
    2: "#D18",
    "green": "#080",
    "t_border": "black",
    "t_fill": "#f88",
    "tui_normal": "white",
    "tui_special": "#ccc",
    "tui_done": "#88f",
    "tui_quit": "#f44",
    "tui_start": "#fcc"
}
CUSTOM_DATA_CONTAINER = {}
FONT_FAMILY = '等线'
buttons = []
showdebug = False
uiDrawing = False
data = {}
hugger = None
huggee = None
message = None
cond = {}

scr = turtle.Screen()
scr.setup(512,512)
scr.title("抱一抱 {0}".format(VERSION))
def onclick(x, y):
    if not uiDrawing:
        for button in buttons:
            if x >= button['x'] and y >= button['y'] and x < button['x']+button['w'] and y < button['y']+button['h']:
                return button['callback']()
scr.onclick(onclick)
cvs = scr.getcanvas()
tui = turtle.Turtle() # tui -> turtle-UI
tui.pensize(3)
tui.speed(0)
tui.ht()
t = turtle.Turtle()
tis = turtle.Turtle() # tui -> turtle-InputString
tis.ht()

def debug(msg):
    if showdebug:
        print(msg)

def goto(tu, x, y, rot = True):
    dx = x - tu.xcor()
    dy = y - tu.ycor()
    rad = math.atan2(dy, dx)
    if rot and (dx != 0 or dy != 0):
        tu.seth(rad / math.pi * 180)
    tu.goto(x, y)

def moveTo(tu, x, y, rot = True):
    tu.up()
    goto(tu, x, y, rot)
def lineTo(tu, x, y, rot = True):
    tu.down()
    goto(tu, x, y, rot)
def squBezierTo(tu, p1, p2, splits = 16, rot = True):
    p0 = (tu.xcor(), tu.ycor())
    for i in range(splits + 1):
        t = i / splits
        x = (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t**2*p2[0]
        y = (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t**2*p2[1]
        lineTo(tu, x, y, rot)
    rad = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    if rot:
        tu.seth(rad / math.pi * 180)
def uiDrawBegin():
    global uiDrawing
    uiDrawing = True
    scr.tracer(False)
def uiDrawEnd():
    global uiDrawing
    uiDrawing = False
    scr.tracer(True)
    scr.update()
    scr.delay(10)

def clearT():
    scr.tracer(False)
    t.clear()
    t.up()
    t.home()
    t.seth(0)
    t.st()
    t.color(COLORS['t_border'], COLORS['t_fill'])
    scr.tracer(True)
    scr.update()
def pl(list):
    y = 192
    t.speed(3)
    for line in list:
        moveTo(t, -192, y)
        t.seth(0)
        for i in range(len(line)):
            if t.xcor() > 192:
                y -= 32
                if y < -160:
                    t.clear()
                    y = 192
                moveTo(t, -192, y)
                t.seth(0)
            else:
                time.sleep(0.05)
            if(line[i] != '\0'):
                t.write(line[i], move=True, font=(FONT_FAMILY, 24))
        time.sleep(0.5)
        y -= 48
        if y < -160:
            t.clear()
            y = 192
def noMessage(hugger,huggee):
    if hugger[2]==1 and huggee[2]==1:
        pl(["Are you a gay?"])
    elif hugger[2]==2 and huggee[2]==2:
        pl(["Are you a lesbian?"])
    else:
        pl(["你抱住了{0}".format(huggee[0])])

def clearTUI():
    tui.clear()
    buttons.clear()
    tis.clear()
    tis.ht()
def addButton(x, y, w, h, text, callback, fillcolor):
    buttons.append({'x': x, 'y': y, 'w': w, 'h': h, 'callback': callback})
    tui.fillcolor(fillcolor)
    moveTo(tui, x, y, False)
    tui.begin_fill()
    lineTo(tui, x + w, y, False)
    lineTo(tui, x + w, y + h, False)
    lineTo(tui, x, y + h, False)
    lineTo(tui, x, y, False)
    tui.end_fill()
    moveTo(tui, x + w/2, y + h/2 - 8, False)
    tui.write(text, align='center', font=(FONT_FAMILY, 16))

inputStr = ""
def displayInputStr():
    global inputStr
    tis.st()
    tis.clear()
    tis.seth(90)
    moveTo(tis, 0, 0, False)
    tis.write(inputStr, move=True, align='center', font=(FONT_FAMILY, 16))
def keyboardPress(letter):
    global inputStr
    if letter == '\b':
        inputStr = inputStr[0:-1]
    else:
        inputStr += letter
    displayInputStr()
def keyboard(callback, allowChinese = False):
    clearTUI()
    displayInputStr()
    uiDrawBegin()
    addButton(-240, -64, 32, 32, "Q", lambda: keyboardPress("q"), COLORS['tui_normal'])
    addButton(-192, -64, 32, 32, "W", lambda: keyboardPress("w"), COLORS['tui_normal'])
    addButton(-144, -64, 32, 32, "E", lambda: keyboardPress("e"), COLORS['tui_normal'])
    addButton(-96, -64, 32, 32, "R", lambda: keyboardPress("r"), COLORS['tui_normal'])
    addButton(-48, -64, 32, 32, "T", lambda: keyboardPress("t"), COLORS['tui_normal'])
    addButton(0, -64, 32, 32, "Y", lambda: keyboardPress("y"), COLORS['tui_normal'])
    addButton(48, -64, 32, 32, "U", lambda: keyboardPress("u"), COLORS['tui_normal'])
    addButton(96, -64, 32, 32, "I", lambda: keyboardPress("i"), COLORS['tui_normal'])
    addButton(144, -64, 32, 32, "O", lambda: keyboardPress("o"), COLORS['tui_normal'])
    addButton(192, -64, 32, 32, "P", lambda: keyboardPress("p"), COLORS['tui_normal'])
    addButton(-224, -112, 32, 32, "A", lambda: keyboardPress("a"), COLORS['tui_normal'])
    addButton(-176, -112, 32, 32, "S", lambda: keyboardPress("s"), COLORS['tui_normal'])
    addButton(-128, -112, 32, 32, "D", lambda: keyboardPress("d"), COLORS['tui_normal'])
    addButton(-80, -112, 32, 32, "F", lambda: keyboardPress("f"), COLORS['tui_normal'])
    addButton(-32, -112, 32, 32, "G", lambda: keyboardPress("g"), COLORS['tui_normal'])
    addButton(16, -112, 32, 32, "H", lambda: keyboardPress("h"), COLORS['tui_normal'])
    addButton(64, -112, 32, 32, "J", lambda: keyboardPress("j"), COLORS['tui_normal'])
    addButton(112, -112, 32, 32, "K", lambda: keyboardPress("k"), COLORS['tui_normal'])
    addButton(160, -112, 32, 32, "L", lambda: keyboardPress("l"), COLORS['tui_normal'])
    addButton(-192, -160, 32, 32, "Z", lambda: keyboardPress("z"), COLORS['tui_normal'])
    addButton(-144, -160, 32, 32, "X", lambda: keyboardPress("x"), COLORS['tui_normal'])
    addButton(-96, -160, 32, 32, "C", lambda: keyboardPress("c"), COLORS['tui_normal'])
    addButton(-48, -160, 32, 32, "V", lambda: keyboardPress("v"), COLORS['tui_normal'])
    addButton(0, -160, 32, 32, "B", lambda: keyboardPress("b"), COLORS['tui_normal'])
    addButton(48, -160, 32, 32, "N", lambda: keyboardPress("n"), COLORS['tui_normal'])
    addButton(96, -160, 32, 32, "M", lambda: keyboardPress("m"), COLORS['tui_normal'])
    addButton(160, -160, 64, 32, "←Bksp", lambda: keyboardPress("\b"), COLORS['tui_special'])
    addButton(-64, -240, 128, 64, "确定", callback, COLORS['tui_done'])
    addButton(96, -240, 128, 64, "重新开始", inputHuggerScreen, COLORS['tui_quit'])
    if allowChinese:
        addButton(-240, -240, 64, 64, "汉字", lambda: keyboardChinese(callback), COLORS['tui_special'])
    uiDrawEnd()
def keyboardChinese(callback):
    clearTUI()
    displayInputStr()
    uiDrawBegin()
    addButton(-192, -64, 32, 32, "上", lambda: keyboardPress("上"), COLORS['tui_normal'])
    addButton(-144, -64, 32, 32, "不", lambda: keyboardPress("不"), COLORS['tui_normal'])
    addButton(-96, -64, 32, 32, "也", lambda: keyboardPress("也"), COLORS['tui_normal'])
    addButton(-48, -64, 32, 32, "了", lambda: keyboardPress("了"), COLORS['tui_normal'])
    addButton(0, -64, 32, 32, "你", lambda: keyboardPress("你"), COLORS['tui_normal'])
    addButton(48, -64, 32, 32, "全", lambda: keyboardPress("全"), COLORS['tui_normal'])
    addButton(96, -64, 32, 32, "喜", lambda: keyboardPress("喜"), COLORS['tui_normal'])
    addButton(-192, -112, 32, 32, "完", lambda: keyboardPress("完"), COLORS['tui_normal'])
    addButton(-144, -112, 32, 32, "对", lambda: keyboardPress("对"), COLORS['tui_normal'])
    addButton(-96, -112, 32, 32, "就", lambda: keyboardPress("就"), COLORS['tui_normal'])
    addButton(-48, -112, 32, 32, "已", lambda: keyboardPress("已"), COLORS['tui_normal'])
    addButton(0, -112, 32, 32, "当", lambda: keyboardPress("当"), COLORS['tui_normal'])
    addButton(48, -112, 32, 32, "想", lambda: keyboardPress("想"), COLORS['tui_normal'])
    addButton(96, -112, 32, 32, "成", lambda: keyboardPress("成"), COLORS['tui_normal'])
    addButton(-192, -160, 32, 32, "我", lambda: keyboardPress("我"), COLORS['tui_normal'])
    addButton(-144, -160, 32, 32, "把", lambda: keyboardPress("把"), COLORS['tui_normal'])
    addButton(-96, -160, 32, 32, "是", lambda: keyboardPress("是"), COLORS['tui_normal'])
    addButton(-48, -160, 32, 32, "欢", lambda: keyboardPress("欢"), COLORS['tui_normal'])
    addButton(0, -160, 32, 32, "爱", lambda: keyboardPress("爱"), COLORS['tui_normal'])
    addButton(48, -160, 32, 32, "经", lambda: keyboardPress("经"), COLORS['tui_normal'])
    addButton(96, -160, 32, 32, "起", lambda: keyboardPress("起"), COLORS['tui_normal'])
    addButton(160, -160, 64, 32, "←Bksp", lambda: keyboardPress("\b"), COLORS['tui_special'])
    addButton(-64, -240, 128, 64, "确定", callback, COLORS['tui_done'])
    addButton(-240, -240, 64, 64, "字母", lambda: keyboard(callback, True), COLORS['tui_special'])
    addButton(96, -240, 128, 64, "重新开始", inputHuggerScreen, COLORS['tui_quit'])
    uiDrawEnd()
    # 上 不 也 了 你 全 喜 完 对 就 已 当 想 成 我 把 是 欢 爱 经 起
def fileNotFoundScreen():
    clearT()
    clearTUI()
    t.speed(3)
    moveTo(t, 0, 48)
    t.write("找不到hug.json", align='center', font=(FONT_FAMILY, 32))
    moveTo(t, 0, -72)
    t.write("请确认已解压缩且在同一文件夹", align='center', font=(FONT_FAMILY, 16))
    t.ht()
def jsonDecodeFailedScreen(error):
    clearT()
    clearTUI()
    t.speed(3)
    moveTo(t, 0, 48)
    t.write("hug.json有语法错误", align='center', font=(FONT_FAMILY, 32))
    moveTo(t, 0, -128)
    t.write(error, align='center', font=(FONT_FAMILY, 16))
    t.ht()
def titleScreen(quick = False):
    """显示标题画面"""
    clearT()
    clearTUI()
    if(quick):
        scr.tracer(False)
    # 写大字
    t.speed(8)
    t.pensize(3)
    # 抱
    moveTo(t, -240, 192)
    lineTo(t, -192, 192)
    moveTo(t, -208, 224)
    lineTo(t, -208, 32)
    lineTo(t, -224, 48)
    moveTo(t, -240, 96)
    lineTo(t, -192, 96)
    moveTo(t, -144, 224)
    lineTo(t, -176, 192)
    moveTo(t, -160, 208)
    lineTo(t, -96, 208)
    lineTo(t, -96, 112)
    lineTo(t, -112, 128)
    moveTo(t, -176, 176)
    lineTo(t, -128, 176)
    lineTo(t, -128, 128)
    moveTo(t, -176, 128)
    lineTo(t, -128, 128)
    moveTo(t, -176, 176)
    lineTo(t, -176, 48)
    lineTo(t, -160, 32)
    lineTo(t, -112, 32)
    lineTo(t, -96, 48)
    # 一
    moveTo(t, -64, 128)
    lineTo(t, 48, 128)
    t.begin_fill()
    squBezierTo(t, (32, 140), (32, 156), 4)
    t.down()
    t.circle(-8, 180)
    t.left(180)
    t.circle(-8, 180)
    squBezierTo(t, (64, 140), (48, 128), 4)
    t.end_fill()
    lineTo(t, 64, 128)
    # 抱
    moveTo(t, 96, 192)
    lineTo(t, 144, 192)
    moveTo(t, 128, 224)
    lineTo(t, 128, 32)
    lineTo(t, 112, 48)
    moveTo(t, 96, 96)
    lineTo(t, 144, 96)
    moveTo(t, 192, 224)
    lineTo(t, 160, 192)
    moveTo(t, 176, 208)
    lineTo(t, 240, 208)
    lineTo(t, 240, 112)
    lineTo(t, 224, 128)
    moveTo(t, 160, 176)
    lineTo(t, 208, 176)
    lineTo(t, 208, 128)
    moveTo(t, 160, 128)
    lineTo(t, 208, 128)
    moveTo(t, 160, 176)
    lineTo(t, 160, 48)
    lineTo(t, 176, 32)
    lineTo(t, 224, 32)
    lineTo(t, 240, 48)
    # 版本号
    t.speed(3)
    moveTo(t, 0, 48)
    t.write(VERSION, align='center', font=(FONT_FAMILY, 16))
    # FOR
    moveTo(t, 0, 0)
    t.write("for {0}".format(data['for']), align='center', font=(FONT_FAMILY, 16))
    # 开始按钮
    uiDrawBegin()
    addButton(-64, -216, 128, 64, '开始', inputHuggerScreen, COLORS['tui_start'])
    addButton(128, -216, 64, 64, '关于', aboutScreen, COLORS['tui_special'])
    uiDrawEnd()
def aboutScreen():
    clearT()
    clearTUI()
    l=["程序主体 by DGCK81LNN","剧情文件元数据："]
    l.extend(data['credits'].split("\n"))
    pl(l)
    addButton(-64, -240, 128, 64, "返回", lambda:titleScreen(True), COLORS['tui_done'])
def inputHuggerScreen():
    global inputStr
    clearTUI()
    clearT()
    t.speed(3)
    moveTo(t, 0, 64)
    t.write("你的名字：\n（首字母缩写）", align='center', font=(FONT_FAMILY, 24))
    inputStr=""
    keyboard(checkHuggerValidityScreen)
def checkHuggerValidityScreen():
    global inputStr, data, hugger
    clearT()
    clearTUI()
    hugger = None
    if inputStr in data['people']['boys']:
        hugger = (data['people']['boys'][inputStr],inputStr,1)
    elif inputStr in data['people']['girls']:
        hugger = (data['people']['girls'][inputStr],inputStr,2)
    if inputStr in data['nameees']:
        ee = data['nameees'][inputStr]
        moveTo(t, 0, 128)
        t.write(ee, align='center', font=(FONT_FAMILY, 24))
    elif not hugger:
        moveTo(t, 0, 160)
        t.write("花名册上没有找到这个名字...", align='center', font=(FONT_FAMILY, 24))
        moveTo(t, 0, 128)
        t.write("请重试", align='center', font=(FONT_FAMILY, 24))
    else:
        return inputHuggeeScreen()
    if not hugger:
        moveTo(t, 0, 64)
        t.write("你的名字：\n（首字母缩写）", align='center', font=(FONT_FAMILY, 24))
        inputStr=""
        keyboard(checkHuggerValidityScreen)
    else:
        addButton(-64, -240, 128, 64, "继续", inputHuggeeScreen, COLORS['tui_start'])
def inputHuggeeScreen():
    global inputStr
    clearTUI()
    clearT()
    t.speed(3)
    moveTo(t, 0, 64)
    t.write("你想拥抱谁？\n（首字母缩写）", align='center', font=(FONT_FAMILY, 24))
    inputStr=""
    keyboard(checkHuggeeValidityScreen)
def checkHuggeeValidityScreen():
    global inputStr, data, hugger, huggee
    clearT()
    clearTUI()
    huggee = None
    if inputStr in data['people']['boys']:
        huggee = (data['people']['boys'][inputStr],inputStr,1)
    elif inputStr in data['people']['girls']:
        huggee = (data['people']['girls'][inputStr],inputStr,2)
    if inputStr in data['nameees']:
        ee = data['nameees'][inputStr]
        moveTo(t, 0, 128)
        t.write(ee, align='center', font=(FONT_FAMILY, 24))
    elif not huggee:
        moveTo(t, 0, 160)
        t.write("花名册上没有找到这个名字...", align='center', font=(FONT_FAMILY, 24))
        moveTo(t, 0, 128)
        t.write("请重试", align='center', font=(FONT_FAMILY, 24))
    elif hugger == huggee:
        moveTo(t, 0, 128)
        t.write("自“抱”自弃", align='center', font=(FONT_FAMILY, 24))
    else:
        return inputMessageScreen()
    if not huggee or hugger == huggee:
        moveTo(t, 0, 64)
        t.write("你想拥抱谁？\n（首字母缩写）", align='center', font=(FONT_FAMILY, 24))
        inputStr=""
        keyboard(checkHuggeeValidityScreen)
    else:
        addButton(-64, -240, 128, 64, "继续", inputMessageScreen, COLORS['tui_start'])
def inputMessageScreen():
    global inputStr
    clearTUI()
    clearT()
    t.speed(3)
    moveTo(t, 0, 64)
    t.write("你想对{0}说什么？".format(huggee[0]), align='center', font=(FONT_FAMILY, 24))
    inputStr=""
    keyboardChinese(preDrawScreen)
def preDrawScreen():
    global inputStr, data, hugger, huggee, message, cond
    clearTUI()
    clearT()
    message = inputStr
    debug("""Hugger信息
姓名：{0}
缩写：{1}
性别：{2}
Huggee信息
姓名：{3}
缩写：{4}
性别：{5}
要说的话：
{6}\n""".format(hugger[0],hugger[1],DEBUG_GENDERS[hugger[2]],huggee[0],huggee[1],DEBUG_GENDERS[huggee[2]],message))
        # 遍历触发条件
    found=False
    debugPersonMatchedBy={(True,False,False):"姓名匹配",(False,True,False):"缩写匹配",(False,False,True):"性别匹配",(False,False,False):"不匹配",None:"任意"} # 调试用
    for condition in data['conditions']: # 开始遍历
        # Hugger
        if 'hugger' in condition:
            h1=condition['hugger']
            if(isinstance(h1,list)):
                for h in h1:
                    huggerMatch=(h==hugger[0],h==hugger[1],h==hugger[2])
                    if huggerMatch != (False,False,False):
                        break
            else:
                huggerMatch=(h1==hugger[0],h1==hugger[1],h1==hugger[2])
        else:
            h1=None
            huggerMatch=None
        # Huggee
        if 'huggee' in condition:
            h2=condition['huggee']
            if(isinstance(h2,list)):
                for h in h2:
                    huggeeMatch=(h==huggee[0],h==huggee[1],h==huggee[2])
                    if huggeeMatch != (False,False,False):
                        break
            else:
                huggeeMatch=(h2==huggee[0],h2==huggee[1],h2==huggee[2])
        else:
            h2=None
            huggeeMatch=None
        # Msgre
        if 'msgre' in condition:
            msgre=condition['msgre']
            msgreMatch=re.search(msgre,message) or False
            if msgreMatch:
                msgreDebug="匹配到“{0}”".format(msgreMatch.group())
            else:
                msgreDebug="不匹配"
        else:
            msgre=None
            msgreMatch=None
            msgreDebug="任意"
        # （调试信息）
        debug("""遍历触发条件 #{0}
Hugger:{1}（{4}）
Huggee:{2}（{5}）
Msgre:{3}（{6}）\n""".format(data['conditions'].index(condition),h1,h2,msgre,debugPersonMatchedBy[huggerMatch],debugPersonMatchedBy[huggeeMatch],msgreDebug))
        # 判断是否匹配
        if huggerMatch!=(False,False,False) and huggeeMatch!=(False,False,False) and msgreMatch!=False:
            # 匹配成功
            debug('匹配成功：{0}'.format(condition))# （调试信息）
            cond=condition
            if('message' in condition):
                pl(condition['message'])
            else:
                noMessage(hugger,huggee)
            found=True
            break
    if not found:
        # 未匹配任何条件
        cond=None
        debug('未匹配任何条件')# （调试信息）
        noMessage(hugger,huggee)
    addButton(-64, -240, 128, 64, "继续", drawScreen, COLORS['tui_start'])
def drawScreen():
    global t, hugger, huggee, cond, message
    find1=hugger; find2=huggee # compatibility aliases
    clearT()
    t.speed(5)
    t.down()
    clearTUI()
    t.color('red')
    debug('画心...')
    # 红心
    t.left(90)
    t.begin_fill()
    t.circle(20,195)
    t.goto(-32,-22)
    t.goto(-24,-36)
    t.goto(-16,-46)
    t.goto(-8,-54)
    t.goto(0,-60)
    t.up()
    t.goto(0,0)
    t.down()
    t.right(195)
    t.circle(-20,195)
    t.goto(32,-22)
    t.goto(24,-36)
    t.goto(16,-46)
    t.goto(8,-54)
    t.goto(0,-60)
    t.end_fill()
    t.up()
    debug('Hugger名字...')
    # Hugger名字
    t.goto(-100,-40)
    t.color(COLORS[hugger[2]])
    t.write(hugger[0],font=(None,20),align='right')
    # 小朋友你是否有很多问号？
    if not (cond and 'confirmed' in cond and cond['confirmed']):
        debug('小朋友你是否有很多问号？')
        t.goto(0,20)
        t.color('black')
        t.write('?',font=(None,30),align='center')
    else:
        debug('小朋友没有问号...')
    debug('Huggee名字...')
    # Huggee名字
    t.goto(100,-40)
    t.color(COLORS[huggee[2]])
    t.write(huggee[0],font=(None,20),align='left')
    debug('说的话...')
    # 说的话
    t.goto(-60,-90)
    t.color(COLORS[hugger[2]])
    t.write(message,font=(None,15),align='center')
    # 自定义指令
    if cond and 'eval' in cond:
        debug('自定义指令：\n'+cond['eval'])
        exec(cond['eval'])
    else:
        debug('无自定义指令...')
    debug('完成')
    t.hideturtle()
    addButton(32, -240, 128, 64, "重新开始", lambda:(debug("\n---------RESTART---------\n"),scr.bgcolor("white"),titleScreen(True)), COLORS['tui_quit'])
    addButton(-160, -240, 128, 64, "退出", exit, COLORS['tui_done'])

try:
    data=json.loads(open("hug.json", 'rb').read())
except FileNotFoundError:
    # 如果找不到文件
    fileNotFoundScreen()
except json.decoder.JSONDecodeError as error:
    # 如果解析JSON失败
    jsonDecodeFailedScreen(error)
else:
    titleScreen()

while True:
    if input() == "DEBUG":
        showdebug = not showdebug
        if showdebug:
            print("DEBUG信息已开启")
        else:
            print("DEBUG信息已关闭")