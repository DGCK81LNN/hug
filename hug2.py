# -*- coding: utf-8 -*-
import turtle
import random # 备用
import time # 时间延迟用
import json # 解码数据文件用
import math # 备用
import re # 匹配要说的话用
import os # 更改控制台标题用

VERSION='v2.2.1 fix' # 程序版本
GENDERS={ # 男女有别
1: '男',
2: '女'
}
COLORS={ # 颜色统一规定表
1: '#48F', # 男生
2: '#D18', # 女生
'green': '#080'
}
CUSTOM_DATA_CONTAINER={}

load0='-----loading...-----' # 加载进度条（未点亮）
load1='>>>>>LOADING~~~>>>>>' # 加载进度条（点亮）
showdebug=False # 是否显示debug信息，输入DEBUG切换
debugging=False # 当前是否正在输出debug信息
t=None # 存放Turtle
ee=None # 存放人名彩蛋

def pl(text, end="\n", wait=0.5, delay=0.1):
    """逐字输出字符串

    参数：

    text(0): 要输出的文本

    end: 换行符

    wait: 输出完成后等待的时间

    delay: 每个字符等待的时间
    """
    for i in range(len(text)):
        if(text[i]!='\0'):
            print(text[i], end='', flush=True)
        time.sleep(delay)
    time.sleep(wait)
    print(end,end='')

def il(prompt):
    """逐字输出提示文本，然后要求用户输入

    参数：

    prompt(0): 提示文本

    返回值：用户输入的值

    当用户输入RESTART和EXIT时分别会抛出RestartProgramException和
    ExitProgramException
    """
    pl(prompt+"\n抱一抱>>> ",end='')
    answer=input()
    print('')
    if answer=='RESTART':
        raise RestartProgramException()
    elif answer=='EXIT':
        raise ExitProgramException()
    elif answer=='DEBUG':
        pl('DEBUG开关已切换！')
        global showdebug
        showdebug=not showdebug
        return il(prompt)
    return answer

def fakeloading():
    """显示假进度条"""
    i=0.0
    while True:
        i = i + random.random()*5
        if(i>100):
            i=100
        j = -int(-i / 5)
        k = int(i)
        print('[',end='')
        for c in range(20):
            if(c>=j):
                print(load0[c],end='')
            else:
                print(load1[c],end='')
        print('] {0}%'.format(k),end='',flush=True)
        if(i>=100):
            print('\n',end='')
            return
        time.sleep(0.03)
        print('\r',end='')

def findname(prompt):
    """在data中查找人名或缩写

    返回值：(姓名, 缩写, 性别（1男2女）)"""
    global data,ee
    ee=None
    if prompt in data['nameees']:
        ee=data['nameees'][prompt]
    if prompt in data['people']['boys']:
        return (data['people']['boys'][prompt],prompt,1)
    if prompt in data['people']['girls']:
        return (data['people']['girls'][prompt],prompt,2)
    for abbr in data['people']['boys'].keys():
        if prompt == data['people']['boys'][abbr]:
            return (prompt,abbr,1)
    for abbr in data['people']['girls'].keys():
        if prompt == data['people']['girls'][abbr]:
            return (prompt,abbr,2)

def askname(prompt, s=None):
    '''输入一个名字

    参数：

    prompt(0): 提示文字

    self(1): 自“抱”自弃

    返回值：(姓名, 缩写, 性别（1男2女）)'''
    global ee
    while True:
        find=findname(il(prompt))
        if ee != None:
            pl(ee)
        elif find == None:
            pl('花名册上没有找到这个名字...请重试')
            pl('请输入汉字或首字母缩写(小写)！')
        elif prompt == s:
            pl('自“抱”自弃')
        if find:
            return find

def noMessage(find1,find2):
    if find1[2]==1 and find2[2]==1:
        pl("Are you a gay?")
    elif find1[2]==2 and find2[2]==2:
        pl("Are you a lesbian?")
    else:
        pl("你抱住了{0}".format(find2[0]))

def debug(msg,done=False):
    """如果DEBUG开启则输出调试信息

    参数：

    msg(0): 要输出的信息

    done(1): debug块是否已结束"""
    global debugging
    if showdebug:
        if not debugging:
            debugging=True
            pl('\n##########DEBUG##########',delay=0.003,wait=0)
        pl(msg,delay=0.003,wait=0)
        if done:
            debugging=False
            pl('#########################\n',delay=0.003)
        else:
            print('')

def bye():
    """按回车退出"""
    print("")
    while(il('按回车退出...')):
        pl("?")
    exit()

class RestartProgramException(Exception):
    """用于在中途重新开始程序"""

class ExitProgramException(Exception):
    """用于在中途结束程序"""

def main():
    """主程序"""
    global t
    if t:
        t.getscreen().bye()
        t=None
    os.system('title 抱一抱 {0}'.format(VERSION))
    # 输入人名
    find1=askname('你的名字：')
    find2=askname('你想拥抱谁？',find1)
    # 输入要说的话
    pl('你想对[{0}]说什么？'.format(find2[0]))
    message=il('请输入中文！')
    # （调试信息）
    debug("""Hugger信息
姓名：{0}
缩写：{1}
性别：{2}
Huggee信息
姓名：{3}
缩写：{4}
性别：{5}
要说的话：
{6}""".format(find1[0],find1[1],GENDERS[find1[2]],find2[0],find2[1],GENDERS[find2[2]],message))

    # 遍历触发条件
    found=False
    debugPersonMatchedBy={(True,False,False):"姓名匹配",(False,True,False):"缩写匹配",(False,False,True):"性别匹配",(False,False,False):"不匹配",None:"任意"} # 调试用
    for condition in data['conditions']: # 开始遍历
        # Hugger
        if 'hugger' in condition:
            hugger=condition['hugger']
            if(isinstance(hugger,list)):
                for h in hugger:
                    huggerMatch=(h==find1[0],h==find1[1],h==find1[2])
                    if huggerMatch != (False,False,False):
                        break
            else:
                huggerMatch=(hugger==find1[0],hugger==find1[1],hugger==find1[2])
        else:
            hugger=None
            huggerMatch=None
        # Huggee
        if 'huggee' in condition:
            huggee=condition['huggee']
            if(isinstance(huggee,list)):
                for h in huggee:
                    huggeeMatch=(h==find2[0],h==find2[1],h==find2[2])
                    if huggeeMatch != (False,False,False):
                        break
            else:
                huggeeMatch=(huggee==find2[0],huggee==find2[1],huggee==find2[2])
        else:
            huggee=None
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
Msgre:{3}（{6}）""".format(data['conditions'].index(condition),hugger,huggee,msgre,debugPersonMatchedBy[huggerMatch],debugPersonMatchedBy[huggeeMatch],msgreDebug))
        # 判断是否匹配
        if huggerMatch!=(False,False,False) and huggeeMatch!=(False,False,False) and msgreMatch!=False:
            # 匹配成功
            debug('匹配成功',True)# （调试信息）
            if('message' in condition):
                for line in condition['message']:
                    pl(line) # 逐行逐字输出结果
            else:
                noMessage(find1,find2)
            found=True
            break
    if not found:
        # 未匹配任何条件
        condition=None
        debug('未匹配任何条件',True)# （调试信息）
        noMessage(find1,find2)
    os.system('title 抱一抱 {0}: Turtle运行中...'.format(VERSION))
    runTurtle(find1,find2,message,condition)
    os.system('title 抱一抱 {0}'.format(VERSION))

def runTurtle(find1,find2,message,condition):
    """运行Turtle"""
    global t
    try:
        t=turtle.Turtle()
    except turtle.Terminator:
        t=turtle.Turtle()
    hugger=find1; huggee=find2 # compatibility aliases
    t.getscreen().title('抱一抱 {0}: 运行中...'.format(VERSION))
    t.color('red')
    debug('画心...')
    # 红心
    t.left(90)
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
    t.up()
    debug('Hugger名字...')
    # Hugger名字
    t.goto(-50,-20)
    t.color(COLORS[find1[2]])
    t.write(find1[0],font=(None,20),align='right')
    # 小朋友你是否有很多问号？
    if not (condition and 'confirmed' in condition and condition['confirmed']):
        debug('小朋友你是否有很多问号？')
        t.goto(0,20)
        t.color('black')
        t.write('?',font=(None,30),align='center')
    else:
        debug('小朋友没有问号...')
    debug('Huggee名字...')
    # Huggee名字
    t.goto(50,-20)
    t.color(COLORS[find2[2]])
    t.write(find2[0],font=(None,20),align='left')
    debug('说的话...')
    # 说的话
    t.goto(-60,-60)
    t.color(COLORS[find1[2]])
    t.write(message,font=(None,15),align='center')
    # 自定义指令
    if condition and 'eval' in condition:
        debug('自定义指令：\n    {0}'.format(condition['eval']))
        exec(condition['eval'])
    else:
        debug('无自定义指令...')
    debug('完成',True)
    t.hideturtle()
    t.getscreen().title('抱一抱 {0}'.format(VERSION))

#########################

os.system('title 抱一抱 {0}: 读取数据文件...'.format(VERSION))
pl('读取数据文件...')
try:
    with open("hug.json", 'rb') as fp: # 打开数据文件
        content=fp.read() # 读取文件内容
        fakeloading() # 显示假进度条
        data=json.loads(content) # 解析JSON
except FileNotFoundError:
    # 如果找不到文件
    pl('找不到hug.json，请确认已解压缩且在同一文件夹')
    bye()
except json.decoder.JSONDecodeError as error:
    # 如果解析JSON失败
    pl('hug.json有语法错误，无法读取')
    pl('错误详情：{0}'.format(error))
    bye()
os.system('title 抱一抱 {0}'.format(VERSION))
pl('加载完成！')
os.system('title 抱一抱 {0}: 天　堂　制　造'.format(VERSION))

# 输出credits
pl(r'''CREDITS:
Idea by 天府灵山行者
turtle编程 by 天府灵山行者
控制台美化 by DGCK81LNN
可扩展 by DGCK81LNN
-----数据文件元数据------
{0}
FOR: {1}
-------------------------
 |  /---          |  /---
---  _ |         ---  _ |
 |  |_|| _______, |  |_||
--- | _|         --- | _|
 |  |             |  |   
\|   \_/         \|   \_/
{2}
-------------------------
当“抱一抱>>>”提示出现时，
输入RESTART即可重新开始，
输入EXIT即可退出！


'''.format(data['credits'],data['for'],VERSION),delay=0.01)
os.system('title 抱一抱 {0}'.format(VERSION))

# 运行主程序
while True:
    try:
        main()
        # 中途如需重新开始或退出，main()会抛出异常
        bye()
        # 结束后如需重新开始，bye()会抛出异常
    except RestartProgramException:
        # 重新开始
        os.system('title 抱一抱 {0}: 重新开始...'.format(VERSION))
        pl('\n---------RESTART---------\n',delay=0.05)
        continue
    except ExitProgramException:
        # 直接关闭
        exit()
    # 如果没有抛出以上两种异常，直接跳出循环
    break