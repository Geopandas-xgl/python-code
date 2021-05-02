import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def folder(path, name):
    path_n = path + '/' + str(name)
    folder = os.path.exists(path_n)
    if not folder:
        os.makedirs(path_n)
    return path_n

try:
    print("请在下方输入需处理的文件绝对路径：（PS：注意路径中使用‘/’连接文件夹）")
    path = input("绝对路径：")
    path_n = folder(path, 'new')
    path_im = folder(path, 'imagine')
    dirs = os.listdir(path)
    for file in dirs:
        if os.path.splitext(file)[1] == '.txt':
            position = path + "/" + file
            position_n = path_n + '/' + file
            if os.path.isfile(position):
                with open(position, encoding='ANSI') as f:
                    with open(position_n, 'w', encoding='utf-8') as f_1:
                        for i in range(0,4000):
                            if i <= 16:
                                i += 1
                                line = f.readline()
                            else:
                                line = f.readline()
                                f_1.write(line)
                                i += 1

    files_n = os.listdir(path_n)
    #寻找光谱峰值
    for file_n in files_n:
        position_n = path_n + "/" + file_n
        df_laman = pd.read_table(position_n, sep='\s+', header=None, error_bad_lines=False)
        df_laman.columns = ['X','Y']
        df_laman_select= df_laman.loc[df_laman['X'] > 35,:]
        a = df_laman_select.iloc[:,0:1]
        b = df_laman_select.iloc[:,1:2]
        a_array = a.values.flatten()
        b_array = b.values.flatten()
        peaks, properties= find_peaks(b_array, prominence=15)
        plt.ion()
        plt.plot(a,b, linewidth = 0.7, c='red')
        for x,y in zip(a_array[peaks].tolist(), b_array[peaks].tolist()):
            plt.text(x, y+10, int(x), ha='center', va = 'top', fontsize=8)
            plt.plot(x, y, marker='o', markersize=2, c='blue')
        plt.xlim(left=35)
        plt.xlabel('rel.1/cm')
        plt.ylabel('CCD cts')
        plt.rcParams['savefig.dpi'] = 300
        plt.rcParams['figure.dpi'] = 300
        portion = os.path.splitext(file_n)
        position_im = path_im + "/" + portion[0] + '.jpg'
        plt.savefig(position_im)
        plt.show()
        plt.close()

    #绘制多曲线拉曼光谱图
    i = 2
    for file_n in files_n:
        position_n = path_n + "/" + file_n
        df_laman = pd.read_table(position_n, sep='\s+', header=None, error_bad_lines=False)
        df_laman.columns = ['X','Y']
        df_laman_select= df_laman.loc[df_laman['X'] > 35,:]
        a = df_laman_select.iloc[:,0:1]
        b = df_laman_select.iloc[:,1:2]
        plt.plot(a,b,linewidth = 0.7)
        plt.xlim(left=35)
        plt.ylim(500,800)
        i += 1
    plt.xlabel('rel. 1/cm')
    plt.ylabel('CCD cts')
    plt.rcParams['savefig.dpi'] = 300
    plt.rcParams['figure.dpi'] = 300
    position_im = path_im + "/" + 'Merge Graphs' + '.jpg'
    plt.savefig(position_im)
except IOError:
    print('Error:没有找到文件或读取失败，请重新输入！')


"""plt.figure(1)
number = 311
for i in range(0,4):
    number += i
    ax = plt.subplot(number)
    ax.plot(x.iloc[:,i:i+1],y.iloc[:,i:i+1])
    plt.ylim(500,800)
plt.show()"""
