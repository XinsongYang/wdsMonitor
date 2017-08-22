# -*- coding: utf-8 -*-

import Wds
import time
import os
import socket

socket.setdefaulttimeout(50)
interval = 180

info1 = {
    'url': 'https://wds.modian.com/show_weidashang_pro/5630#1',
    'group': 'GNZ48-高源婧应援会',
    'qq': '340077049',
    'name': '小狐狸',
    'activity': '总选举中报冲刺3.0',
    'slogan': '聚聚们的每一份心意对小狐狸都非常重要，2017年的夏天，让我们守护她的梦想，陪她奋力一战！',
    'isTurnOn': True,
}

def qqReport(msg, group):
    msg = "'" + msg + "'"
    cmd = 'qq send group ' + group + ' ' + msg
    os.system(cmd)
    # print(msg)

def singleSend1(mainWds):
    if mainWds.isChanged == False:
        return False
    msg = ''
    for user in mainWds.addedUserMoney:
        msg += user + '刚刚支持了' + str(mainWds.addedUserMoney[user]) + '元，'
    msg += '感谢大家对小狐狸的支持！\n'
    msg += mainWds.activity + '正在进行中，目前总额' + str(mainWds.amount) + '元，' + '参加人数' + str(mainWds.peopleNum) + '，'
    msg += '距离本次活动结束还有' + str(mainWds.time) + '。\n'
    msg += mainWds.slogan + '\n微打赏链接：' + mainWds.url
    qqReport(msg, mainWds.qq)

wds1 = Wds.Wds(info1)

while True:
    time.sleep(interval)
    try:
        wds1.refreshInfo()
    except:
        print('refresh error')
    if wds1.isTurnOn and wds1.isChanged:
        singleSend1(wds1)

