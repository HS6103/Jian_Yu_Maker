#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from pprint import pprint
from ArticutAPI import Articut

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.load(f)
articut = Articut(username=accountDICT["username"], apikey=accountDICT["api_key"])

#簡語化函數
def jianyu(inputSTR):
    jianyu_result = ""
    
    resultDICT= articut.parse(inputSTR, level="lv2")['result_obj']
    
    
    if len(inputSTR) == 4:
        jianyu_result += inputSTR[0] + inputSTR[2]
    
    else:
        for i in range(len(resultDICT)):
            
            for j in range(len(resultDICT[i])):
                if (len(resultDICT[i])) == 1:
                    if (len(resultDICT[i][j]['text']) == 4):
                        jianyu_result += resultDICT[i][j]['text'][0] + resultDICT[i][j]['text'][2]
                        break
                
                else:
                    if resultDICT[i][j]['pos'] in ['CLAUSE_AnotAQ', 'MODIFIER', 'ENTITY_DetPhrase', 'DegreeP', 'TIME_justtime', 'ENTITY_classifier']:
                        jianyu_result += resultDICT[i][j]['text']
                        
                    else:
                        if j == 0:
                            if 'ENTITY' in resultDICT[i][j]['pos']:
                                if (len(resultDICT[i])) == 2:
                                    jianyu_result += resultDICT[i][j]['text'][0]
                                else:
                                    jianyu_result += resultDICT[i][j]['text']
                                    
                            elif 'ACTION' in resultDICT[i][j]['pos']:
                                jianyu_result += resultDICT[i][j]['text']
                            else:
                                jianyu_result += resultDICT[i][j]['text'][0]
                                
                        else:
                            jianyu_result += resultDICT[i][j]['text'][0]
                            
    return jianyu_result


#程式進入點
if __name__ == "__main__":
    resultDICT = []
    while True:
        inputSTR = input("請輸入你要轉換成簡語的句子:\n")
        
        jianyu_resultSTR = jianyu(inputSTR)
        
        print ("\n" + jianyu_resultSTR + " (" + inputSTR + ")" +"\n")
        
    
        