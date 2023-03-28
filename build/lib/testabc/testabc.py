# -*- coding: utf-8 -*-

'''
通过reference.ymal文件为参考，结合突变数据，计算STR处的MSI状态，即MSI score值
'''
import sys
import re
import glob
import yaml
import os

#定义数据库
class STR(object):
    def __init__(self,id):
        self.id=id
        self.geneName=""
        self.site=""
        self.chr=""
        self.sequence=""
        self.length=""
#加载参考数据库
def load(reference):
    with open(reference, "rb") as f:
        return yaml.safe_load(f)        
        
#计算样本的MSI
def calculateMSI(filein):
    tmp={}
    data_path = os.path.join(os.path.dirname(__file__),'reference.yaml')
    ref=load(data_path)
    with open(filein, "r") as f:
        fs=f.readlines()
    for records in fs:
        rs=records.split("\t")
        ids=rs[2]+"_"+rs[3]
        tmp[ids]=STR(ids)
        tmp[ids].geneName=rs[10]
        tmp[ids].chr=rs[2]
        tmp[ids].site=rs[3]
        tmp[ids].sequence=rs[6]
        tmp[ids].length=len(rs[6])
    res={}
    for id in ref:
        if id in tmp:
            if tmp[id].length != ref[id]["length"] :
                res[id]=1
            else:
                res[id]=0
        else:
            res[id]=0
    return(sum(res.values()))

#计算MSI
def calMSI(sampleList):
    samples={}
    msi={}
    with open(sampleList) as f:
        fs=f.readlines()
        for records in fs:
            rs=records.split(" ")
            samples[rs[0]]=rs[1].strip("\n")
    for k,v in samples.items():
        msi[k]=calcuateMSI(v,ref)
    return(msi)

#输出结果
def outMSI(msi,fileout):
    with open(fileout,"w") as f:
        f.writelines("Sample\tScore\n")
        for k,v in msi.items():
            f.writelines(k+"\t"+str(v)+"\n")