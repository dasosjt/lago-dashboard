#!/usr/env python 
# -*- encoding: utf-8 -*-
""" 
Code to do basic analysis (chrage histograms) of LAGO data

Usage: ./charge_histo.py [datafile]

Date: 22/11/2015
L. Horacio Arnaldi
LabDPR - CAB - IB

"""
#-------------------------------------------------------------------------------
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import bz2
import sys
from datetime import datetime as dt

if (len(sys.argv)!=1):
    datafile=sys.argv[1]

#start recording
dt1 = dt.now()

#datafile extension must be *.dat.bz2
ch1,ch2,ch3=np.loadtxt(datafile,unpack=1, dtype=int)

#Charge histograms
h1=[ch1[i:i+12].sum()/12 for i in np.arange(0,len(ch1),12)]
h2=[ch2[i:i+12].sum()/12 for i in np.arange(0,len(ch2),12)]
h3=[ch3[i:i+12].sum()/12 for i in np.arange(0,len(ch3),12)]

n1,bins1=np.histogram(h1,np.arange(0,4096))
n2,bins2=np.histogram(h2,np.arange(0,4096))
n3,bins3=np.histogram(h3,np.arange(0,4096))

#plt.semilogx(bins1[:-1],n1,bins2[:-1],n2,bins3[:-1],n3)
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
#CH1
ax1.plot(bins1[:-1],n1,'g<--',linewidth=2,label='CH1')
ax1.legend()
ax1.set_ylabel('# of events')
ax1.set_xlabel('ADC bins')
#CH2
ax2.plot(bins2[:-1],n2,'r<--',linewidth=2,label='CH2')
ax2.legend()
ax2.set_ylabel('# of events')
ax2.set_xlabel('ADC bins')
#CH3
ax3.plot(bins3[:-1],n3,'b<--',linewidth=2,label='CH3')
ax3.legend()
ax3.set_ylabel('# of events')
ax3.set_xlabel('ADC bins')
ax1.grid()
#ax3.set_xlim(40,1000)
#ax3.set_ylim(0,1e3)

print(dt.now() - dt1)

plt.savefig('histo_charge_chan.pdf')
plt.show()

