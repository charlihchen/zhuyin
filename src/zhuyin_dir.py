import os
# -*- coding: UTF-8 -*-
# Zuyin(22,4,14,5)
# I for 22 are (b)ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙ
# j for 4 are (b)ㄧㄨㄩ
# k for 14 are (b)ㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦ
# l for 5 are —/V\. (ˉˊˇˋ˙)

# ␢ is blank character with code: U+2422
consonant = ["␢","ㄅ","ㄆ","ㄇ","ㄈ","ㄉ","ㄊ","ㄋ","ㄌ","ㄍ","ㄎ","ㄏ","ㄐ","ㄑ","ㄒ","ㄓ","ㄔ","ㄕ","ㄖ","ㄗ","ㄘ","ㄙ"] #聲母
medial = ["␢","ㄧ","ㄨ","ㄩ"]#介音
rhyme = ["␢","ㄚ","ㄛ","ㄜ","ㄝ","ㄞ","ㄟ","ㄠ","ㄡ","ㄢ","ㄣ","ㄤ","ㄥ","ㄦ"]  #韻母 
tone = ["ˉ","ˊ","ˇ","ˋ","˙"] #聲調 ('-','/','v','\','.')
#zhuyin_path = "\\index\\chinese\\zhuyin\\"
#zhuyin_path = "C:\\Users\\charlihchen.FORTINET-US\\Python\\indexbox\\language\\chinese\\zhuyin\\"
zhuyin_path = "C:\\Users\\charl\\Python\\indexbox\\language\\chinese\\zhuyin\\"

for c in consonant:
    for m in medial:
        for r in rhyme:
            for t in tone:
                filename=c+m+r+t
                #print(filename)
                if c=='␢' and m=='␢' and r=='␢': #condition1 ␢␢␢ˉ
                    path=zhuyin_path+c+"\\"+filename #expr1 or value_when_true
                    #print(path)
                elif c=='␢' and m=='␢' and r!='␢': #condition2 ␢␢ㄚˉ
                    path=zhuyin_path+r+"\\"+filename #expr2 or value_when_true
                    #print(path)
                elif (c=='␢' and m!='␢' and r=='␢') or (c=='␢' and m!='␢' and r!='␢'): #condition3 ␢ㄧ␢ˉ or ␢ㄧㄚˉ
                    path=zhuyin_path+m+"\\"+filename #expr3 or value_when_true
                    #print(path)
                elif c!='␢' and m=='␢' and r!='␢': #condition4 ㄅ␢ㄚˉ
                    path=zhuyin_path+c+"\\"+filename #expr2 or value_when_true
                    #print(path)                    
                else: #value_when_false       
                    path=zhuyin_path+c+"\\"+filename
                    
                #print(path)
                #File Handling
                filename_ext=filename+'.txt'
                #print(filename_ext)
                if not os.path.exists(path):
                    os.makedirs(path)
                    #print("Created Directory : ", path)
                    os.chdir(path)
                    f=open(filename_ext,'w+',encoding ='UTF-8') # Create fileName.txt
                    #f.close()
                    #html="""<html><head><meta charset="utf-8"></head><body></body></html>"""
                    html="""<html><head><meta charset="utf-8"></head><body><?php require ''; ?></body></html>"""
                    index=html.find("';") #find string '; to insert filename.txt for the PHP code require 'filename.txt'
                    html2=html[:index]+filename_ext+html[index:]
                    #print(html2)
                    with open("index.php","w", encoding="utf-8") as file:
                        file.write(html2)
                        file.close()
                else:
                    print("Directory already existed : ", path)
            print('\n') #return
        print('\n') #return
    print('\n') #return
print('\n') #return
#print(zhuyin_path,filename[0],"\\",filename,".txt",sep="") #use the sep parameter to get rid of the space
