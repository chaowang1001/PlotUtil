#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 10:54:02 2017

Set the appearance of the plots

@author: chaowang
"""

def setaxfont(ax, axtitle=None, axtitlesize=16, axtitleweight='bold', \
              xlabel='x', ylabel='y', zlabel=None, \
              axlabelsize=16, axlabelweight='bold', \
              axticklabelsize=16, axticklabelweight='bold'):
    if axtitle is not None:
        ax.set_title(axtitle)
        ax.title.set_fontsize(axtitlesize)
        ax.title.set_fontweight(axtitleweight)
        
    if xlabel is not None:
        ax.set_xlabel(xlabel)
        ax.xaxis.label.set_fontsize(axlabelsize)
        ax.xaxis.label.set_fontweight(axlabelweight)
        
    if ylabel is not None:
        ax.set_ylabel(ylabel)
        ax.yaxis.label.set_fontsize(axlabelsize)
        ax.yaxis.label.set_fontweight(axlabelweight)
        
    if zlabel is not None:
        ax.set_zlabel(zlabel)
        ax.zaxis.label.set_fontsize(axlabelsize)
        ax.zaxis.label.set_fontweight(axlabelweight)
        
        for item in (ax.get_zticklabels()):
            item.set_fontsize(axticklabelsize)
            item.set_fontweight(axticklabelweight)
        
    if axticklabelsize is not None:
        for item in (ax.get_xticklabels() + ax.get_yticklabels()):
            item.set_fontsize(axticklabelsize)
            item.set_fontweight(axticklabelweight)
    
    return ax

def setaxtickstylesci(ax,xsci=True,ysci=True, \
                      xfs=14,yfs=14,xfw='bold',yfw='bold', \
                      xps=None,yps=(-0.2,0), \
                      xrt=None,yrt=90):
    ax.xaxis.major.formatter._useMathText = True
    ax.yaxis.major.formatter._useMathText = True
    if xsci:
        ax.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        ax.xaxis.offsetText.set_fontsize(xfs)
        ax.xaxis.offsetText.set_fontweight(xfw)
        
    if ysci:
        ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        ax.yaxis.offsetText.set_fontsize(yfs)
        ax.yaxis.offsetText.set_fontweight(yfw)
        
    if xps is not None:
        ax.get_xaxis().get_offset_text().set_position(xps)
        
    if xrt is not None:
        ax.get_xaxis().get_offset_text().set_rotation(xrt)
        
    if yps is not None:
        ax.get_yaxis().get_offset_text().set_position(yps)
        
    if yrt is not None:
        ax.get_yaxis().get_offset_text().set_rotation(yrt)
    
    return ax

def setcbarfont(cbar, label=None, labelsize=12, labelweight='bold',\
                ticksize=12, tickweight='bold'):
    if label is not None:
        cbar.set_label(label=label,weight=labelweight,size=labelsize)
        
    for item in cbar.ax.yaxis.get_ticklabels():
        item.set_fontsize(ticksize)
        item.set_fontweight(tickweight)
        
    return cbar

def markers(nmk):
#    nmk Different Markers
#    Modified from markers.m
#    ChaoWang201804081759
    
#    mks = ['o','+','*','.','x','s','d','^','v','>','<','p','h','none']
    mks = ['o','s','d','^','v','>','<','p','h','+','*','.','x','none']
    
    return mks[0:nmk]

def linecolorsmpl(ncolor):
#    Line Color Cycles from matplotlib 2.1.2
#    Modified from linecolorsmatlab.m
    
#    https://stackoverflow.com/questions/42086276/get-default-line-colour-cycle?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
#    https://matplotlib.org/users/dflt_style_changes.html#colors-in-default-property-cycle
    
#    import matplotlib.pyplot as plt
#    plt.rcParams['axes.prop_cycle'].by_key()['color']

#    ChaoWang201804081821
    lcs = ['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b', \
           '#e377c2','#7f7f7f','#bcbd22','#17becf']
    
    if ncolor <= 10:
        lc = lcs[0:ncolor]
        return lc
    else:
        ValueError('Please add more colors!')
        
def linestyles(nls):
#    nls Line Styles
#    Modified from linestyles.m
#    ChaoWang201804121845

    ls = ['-','--','-.',':','-','--',':','-.','-','--',':','-.']
    if nls <= 12:
        ls = ls[0:nls]
        return ls
    else:
        ValueError('Please add line styles!')
        
    