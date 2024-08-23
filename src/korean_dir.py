import os
# -*- coding: UTF-8 -*-
# korean(19,21,28)
# IC for 19 are ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ
# V for 21 are ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
# FC for 28 are (b)ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅄ ㅅ ㅆ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ

# ␢ is blank character with code: U+2422
IC = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"] #initial consonant
V = ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"] #vowel
FC = ["␢","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]  #final consonant 

#korean_path = "\\index\\korean\\"
#korean_path = "C:\\Users\\charlihchen.FORTINET-US\\Python\\indexbox\\language\\korean\\"
korean_path = "C:\\Users\\charl\\Python\\indexbox\\language\\korean\\"

for i in IC:
    for j in V:
        for k in FC:
            filename=i+j+k
            #print(filename)
            path=korean_path+i+"\\"+filename
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
#print(zhuyin_path,filename[0],"\\",filename,".txt",sep="") #use the sep parameter to get rid of the space
