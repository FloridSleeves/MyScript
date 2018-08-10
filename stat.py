#!/usr/bin/python
#coding=utf8
"""
# Author: lily
# Created Time : 2018-07-26 14:23:25

# File Name: avg.py
# Description:

"""
import sys
filein=open(sys.argv[1])
lines=filein.readlines()
count=0
stat=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
number=0
visit_storage_number=0
for line in lines:
    if line.find("READ")==-1:
        continue;
    number+=1 
    place= line.split(':')[-1].strip()
    if place[-1]!='E':
        count+=int(place)
        visit_storage_number+=1
        stat[int(place)]+=1
    else:
        stat[0]+=1
avg=float(count)/number
vi_avg=float(count)/visit_storage_number
print(avg,list(enumerate(stat)))
#[7:x,6:x,5:x...]
#stat.reverse()
res=0
accu=[]
total=sum(stat)
rate=[]
for iter in enumerate(stat):
    res+=iter[1]
    accu.append(res)
    rate.append(float(iter[1])/total)
#accu.reverse()

for i in enumerate(accu):
    accu[i[0]]=float(i[1])/float(total)
print(list(enumerate(accu)))

x=range(len(accu))
y=accu
import matplotlib.pyplot as plt
plt.plot(x,y,marker='.',linestyle='-',color='r')
stat.reverse()
plt.bar(x,rate)

for i,v in enumerate(rate):
    if v==0:
        continue
    plt.text(i-0.5,v+0.01,'%.2f'%v)
plt.savefig(sys.argv[2])



