# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:47:00 2017

@author: kingsoft
"""
import os  # 引入文件操作库
import codecs
import sys
import pandas as pd
from random import shuffle
#from tgrocery import Grocery
reload(sys)
sys.setdefaultencoding('utf8')

def readFileTolist(filename):
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    fileList = []
    for ilines in lines:
        fileList.append(ilines)
    return fileList

if  __name__=='__main__':
    filelist = ['E:/127.txt','E:/185.txt']
    Allword = pd.DataFrame([])
    index = 0
    #grocery = Grocery('test')
    for ifile in filelist:
        iword = readFileTolist(ifile)
        wordFrame = pd.DataFrame(iword)
        num = len(iword)
        print ('There are %d samples in %s'%(num,ifile))
        Allword = pd.concat([Allword,(pd.concat([pd.Series([index]*num),wordFrame],axis = 1))],axis = 0)
        index += 1
    #train_and_test_split三次，每次都shuffle，判断准确率
    p = 0.8
    tryNum = 1
    for i in range(tryNum):
        shuffle(Allword)
        train = data[:int(len(Allword)*p),:] #前80%为训练集
        test =  data[int(len(Allword)*p),:] #前20%为测试集
        grocery.train(train)
        print grocery.get_load_status()
        test_result = grocery.test(test) 
        print test_result.accuracy_labels            
        print test_result.recall_labels
    
