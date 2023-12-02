# -*- coding: utf-8 -*-
###---(oﾟvﾟ)ノ---###
#Author Start
# hint Date: 2023-11-29 16:07:51
# hint LastEditors: Jupiter.Q.Peng
# hint LastEditTime: 2023-12-02 17:26:07
# hint Description:
# hint FilePath: \GBKGR\transMat.py
# Author End

import pandas as pd
from scipy.io import loadmat, savemat
import numpy as np
from tools import *


# 写一个用于转换mat文件为Datafrarame的函数, 并存储为csv文件

def transMat(data_path:str):
    datas = loadmat(data_path)

    features = datas['data']
    labels = datas['target']
    partial_target = datas['partial_target']

    labels, partial_target = process_csc_matrix(labels, partial_target)

    pd_features = pd.DataFrame(features)
    pd_labels = pd.DataFrame(labels)
    pd_partial_target = pd.DataFrame(partial_target)

    pd_features.to_csv('features.csv')
    pd_labels.to_csv('labels.csv')
    pd_partial_target.to_csv('partial_target.csv')

if __name__ == '__main__':
    transMat('demo.mat')