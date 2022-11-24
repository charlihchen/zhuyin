# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 22:35:13 2022

@author: charl
"""
from bopomofo import to_bopomofo
file1 = open("4698ch.txt","r+", encoding="utf8")
chword=file1.read()
print(chword)
res = to_bopomofo(u'{}',first_tone_symbol=True).format(chword)


with open("ch2zhuyin.txt", "w", encoding="utf8") as file2:
    file2.write({}+" : "+res+"\n").format(chword)
    file2.close()
#res = to_bopomofo(u'{}',first_tone_symbol=True).format(chword)
#TypeError: get_pinyin() got an unexpected keyword argument 'show_tone_marks'
#这个问题是由于包的问题，新版本的show_tone_marks已经没有了，换成了tone_marks