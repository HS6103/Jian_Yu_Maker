#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
from ArticutAPI import Articut

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.load(f)
articut = Articut(username=accountDICT["username"], apikey=accountDICT["api_key"])

with open("userDefined.json", encoding="utf-8") as userdefinedDICT:
    userdefined = json.load(userdefinedDICT)

#簡語化函數
def jianyu(inputSTR):
    #初始化
    #resultDICT = []
    jianyu_result = ""
    #jianyu_toadd = ""
    
    #resultDICT= articut.parse(inputSTR, level="lv2", userDefinedDictFILE=userdefined)['result_obj']
    
    jianyu_result += inputSTR[0] + inputSTR[2]
    
    #四字輸入直接先處理
    #if len(inputSTR) == 4:
        #jianyu_result += inputSTR[0] + inputSTR[2]
    
    #else:
        #for i in range(len(resultDICT)):
            #for j in range(len(resultDICT[i])):
                #if (len(resultDICT[i])) == 1:
                    #if (len(resultDICT[i][j]['text']) == 4):
                        #jianyu_toadd = resultDICT[i][j]['text'][0] + resultDICT[i][j]['text'][2] + " (" + inputSTR + ")"
                        #break
                #else:
                    #if resultDICT[i][j]['pos'] in ['CLAUSE_AnotAQ', 'MODIFIER', 'ENTITY_DetPhrase', 'DegreeP', 'TIME_justtime', 'ENTITY_classifier']:
                        #jianyu_toadd += resultDICT[i][j]['text']
                        
                    #else:
                        #if j == 0:
                            #if 'ENTITY' in resultDICT[i][j]['pos']:
                                #if (len(resultDICT[i])) == 2:
                                    #jianyu_toadd += resultDICT[i][j]['text'][0]
                                #else:
                                    #jianyu_toadd += resultDICT[i][j]['text']
                                    
                            #elif 'ACTION' in resultDICT[i][j]['pos']:
                                #jianyu_toadd += resultDICT[i][j]['text']
                                
                            #else:
                                #jianyu_toadd += resultDICT[i][j]['text'][0]
                                
                        #else:
                            #if len(resultDICT[i][j]['text']) == 2:
                                #jianyu_toadd += resultDICT[i][j]['text'][0]
                            
                            #elif len(resultDICT[i][j]['text']) == 3:
                                #if resultDICT[i][j]['pos'] in ['ENTITY_nouny']:
                                    #jianyu_toadd += resultDICT[i][j]['text'][0] + resultDICT[i][j]['text'][1]
                                #else:
                                    #jianyu_toadd += resultDICT[i][j]['text'][0]
                                
                            #elif len(resultDICT[i][j]['text']) == 4:
                                #jianyu_toadd += resultDICT[i][j]['text'][0] + resultDICT[i][j]['text'][2] 
                                
                            #else:
                                #jianyu_toadd += resultDICT[i][j]['text'][0]
                                
                #jianyu_result += jianyu_toadd
                
                #if (jianyu_toadd != resultDICT[i][j]['text']):             
                    #jianyu_result += " (" + resultDICT[i][j]['text'] + ")"
                    
                
                                
            ##判斷輸入是否經過更動
            #if (jianyu_result == "") | (jianyu_result == inputSTR):
                #jianyu_result = inputSTR
        
            #else:
                #pass
    
    #回傳結果
    return jianyu_result


#test程式進入點
if __name__ == "__main__":
    resultDICT = []
    while True:
        inputSTR = input("請輸入你要轉換成簡語的句子:\n")
        
        jianyu_resultSTR = jianyu(inputSTR)
        
        print ("\n" + jianyu_resultSTR + "\n")
        
    
        