# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 22:35:13 2022

@author: Charlih Chen
"""
from bopomofo import to_bopomofo
from pypinyin import pinyin,lazy_pinyin,Style
#from pyzhuyin import pinyin_to_zhuyin, zhuyin_to_pinyin
with open("4698ch.txt","r", encoding="utf8") as f: 
    for line in f: #Read File Line by Line
        #do something here
        for char in line:
            #do something here
#            res = to_bopomofo(u'%char') #,first_tone_symbol=True
            res = to_bopomofo(u'{}').format(char) #,first_tone_symbol=True
            #Why there is '\n' for the res?
            res2 = pinyin({res}, style = Style.BOPOMOFO)
            #res2 is not getting the right pinin becasue the pinin hs the [' and ']
#            print(pinyin('中心鸞',style=Style.BOPOMOFO))
#            print(len(res))
#            print(len(res2))
            word2zhuyin="{}:{}".format(char, res2)
            with open("ch2zhuyin.txt", "a", encoding="utf8") as file2:
                file2.write(word2zhuyin)
                file2.close()
#res = to_bopomofo(u'{}',first_tone_symbol=True).format(chword)
#TypeError: get_pinyin() got an unexpected keyword argument 'show_tone_marks'
#这个问题是由于包的问题，新版本的show_tone_marks已经没有了，换成了tone_marks
#C:\Users\charlihchen.FORTINET-US\Anaconda3\Lib\site-packages\bopomofo\__init__.py
