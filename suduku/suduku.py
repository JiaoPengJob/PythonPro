#!/usr/bin/env python
# -*- coding : utf-8 -*-

import random as rd

import numpy as np
import wx


class MySuduku(wx.Frame):

    def __init__(self, parent, title="我的数独", ndarrs=[]):
        super(MySuduku, self).__init__(parent, title=title, size=(440, 440))
        self.init_ui(ndarrs)
        self.Centre()
        self.Show()

    def init_ui(self, ndarrs):
        # 设置为一维数组
        # news = np.ravel(ndarrs, order="A")
        p = wx.Panel(self)
        gs = wx.GridSizer(3, 3, 4, 4)
        for i in range(0, 9):
            ges = wx.GridSizer(3, 3, 4, 4)
            for j in range(0, 9):
                btn = str(ndarrs[i][j])
                ges.Add(wx.Button(p, label=btn, size=(40, 40)), 0, wx.EXPAND)
            gs.Add(ges, 0, wx.EXPAND)
            p.SetSizer(gs)


mList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rd.shuffle(mList)

numbers = np.array(mList)

for x in range(1, 9):
    mList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rd.shuffle(mList)
    numbers = np.append(numbers, mList, axis=0)

sNumbers = np.split(numbers, 9)
newsArrs = []

for x in range(0, 9):
    news = np.split(sNumbers[x], 3)
    newsArrs.append(news)

# print(newsArrs)

ns = np.stack(newsArrs, 1)
# print(ns)

one = []
two = []
three = []

for y in range(0, 9):
    one.append(np.ravel(ns[0][y]))

on = np.ravel(one, order="A")
ont = np.split(on, 3)
print(ont)


# app = wx.App()
# MySuduku(None, ndarrs=sNumbers)
# app.MainLoop()
