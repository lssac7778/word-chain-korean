import sys
import math

# ord - char

# 음절단위 변환 (예 : 간, 당, ...)
t1 = ['r','R','s','e','E','f','a','q','Q','t','T','d','w','W','c','z','x','v','g','k','o','i','O','j','p','u','P','h','hk','ho','hl','y','n','nj','np','nl','b','m','ml','l','r','R','rt','s','sw','sg','e','f','fr','fa','fq','ft','fx','fv','fg','a','q','qt','t','T','d','w','c','z','x','v','g']
# 음소단위 변환 (예 : ㄱ, ㄴ, ...)
t2 = ['r','R','rt','s','sw','sg','e','E','f','fr','fa','fq','ft','fx','fv','fg','a','q','Q','qt','t','T','d','w','W','c','z','x','v','g','k','o','i','O','j','p','u','P','h','hk','ho','hl','y','n','nj','np','nl','b','m','ml','l']


def KorTransform2Eng(istr) :
    ostr = ""
    #istr = unicode(istr)
    for i in range(0, len(istr)) :
        
        ch = istr[i]
        
        # 가 - 힣 : 0xAC00 - 0xD7A3
        if (ord(ch) >= 0xac00) & (ord(ch) <= 0xd7a3) :
            a = int(math.floor((ord(ch)-44032)/588))            # 초성
            b = int(math.floor(((ord(ch)-44032)%588)/28)) + 19  # 중성
            c = (ord(ch)-44032)%28 + 39                         # 종성
    
            if c == 39 : # 종성유무 판단
                ostr = ostr + t1[a]+t1[b]
            else :
                ostr = ostr + t1[a]+t1[b]+t1[c]
            
        # ㄱ - ㅣ : 0x3131 - 0x3163
        elif (ord(ch) >= 0x3131) & (ord(ch) <= 0x3163) :
            a = ord(ch) - 12593
            ostr = ostr + t2[a]
            
        else :
            ostr = ostr + ch

    return ostr


