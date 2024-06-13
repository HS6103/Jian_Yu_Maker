#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os
from ArticutAPI import Articut


with open("userDefined.json", encoding="utf-8") as userdefinedDICT:
    userdefined = json.load(userdefinedDICT)

#簡語化函數
def jianyu(inputSTR):
    #articut = Articut(username=os.environ.get("loki_username"), apikey=os.environ.get("articut_key"))
    
    #初始化
    jianyu_result = ""
    
    if len(inputSTR) != 4:
        jianyu_result += "請輸入四字詞語!"
    else:
        jianyu_result += inputSTR[0] + inputSTR[2]
    
    return jianyu_result


#test程式進入點
if __name__ == "__main__":
    resultDICT = []
    while True:
        inputSTR = input("請輸入你要轉換成簡語的句子:\n")
        
        jianyu_resultSTR = jianyu(inputSTR)
        
        print ("\n" + jianyu_resultSTR + "\n")
        
    
        