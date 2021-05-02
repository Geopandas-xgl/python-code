#导入程序必要的程序包
import numpy as np
import pandas as pd
import os #读取文件、生成文件夹
import matplotlib.pyplot as plt #绘图
from scipy.signal import find_peaks #寻找峰值

#建立文件夹函数
def folder(path, name):
    path_n = path + '/' + str(name)
    folder = os.path.exists(path_n) #检测文件夹是否存在
    if not folder: #如果文件夹不存在，则新建文件夹
        os.makedirs(path_n)
    return path_n

#创建储存数据和保存图片的文件夹，且删除文件中非数据内容
try: #判断输入命令窗口输入的绝对路径是否符合要求
    print("请在下方输入需处理的文件绝对路径：（PS：注意路径中使用‘/’连接文件夹）")
    path = input("绝对路径：") #命令窗口输入绝对路径
    path_n = folder(path, 'new') #调用folder函数，新建New文件夹
    path_im = folder(path, 'imagine') #调用folder函数，新建imagine文件夹
    dirs = os.listdir(path) #遍历path路径中的文件名称及文件后缀，并以列表的类型储存文件名及后缀
    for file in dirs: #依次提取文件名和文件后缀
        if os.path.splitext(file)[1] == '.txt': #将文件名与文件后缀分开，只处理txt格式的文本
            position = path + "/" + file #创建file文件在path下的绝对路径
            position_n = path_n + '/' + file #创建file文件在path_n下的绝对路径
            if os.path.isfile(position): #判断position绝对路径下对应的是否为文件
                with open(position, encoding='ANSI') as f: #读取position下的ANSI编码的文件
                    with open(position_n, 'w', encoding='utf-8') as f_1: #在position_n的路径下创建utf-8的文件
                        for i in range(0,4000): #按行读取文件内容，删除数据之前内容，将数据储存到‘new’文件夹中
                            if i <= 16: #16代表数据之前存在16行内容，具体数值因文件而异。
                                i += 1
                                line = f.readline()
                            else:
                                line = f.readline() #按行读取内容
                                f_1.write(line) #将数据储存在‘new’文件夹中
                                i += 1
    #绘制拉曼光谱图，寻找峰值
    files_n = os.listdir(path_n) #遍历path_n路径下的文件名及后缀，并以列表的类型储存文件名及后缀
    for file_n in files_n: #依次调用列表的文件名及后缀
        position_n = path_n + "/" + file_n #创建path_n路径下的file_n的绝对路径
        df_laman = pd.read_table(position_n, sep='\s+', header=None, error_bad_lines=False) # 读取文件,以dataframe类型储存数据
        df_laman.columns = ['X','Y'] #分别将第一列和第二列的表头赋予X和Y
        df_laman_select= df_laman.loc[df_laman['X'] > 35,:] #提取'X>35'的行数据
        a = df_laman_select.iloc[:,0:1] #提取X列
        b = df_laman_select.iloc[:,1:2] #提取Y列
        a_array = a.values.flatten() #将二维dataframe转变为one dimensional array
        b_array = b.values.flatten()
        peaks, properties= find_peaks(b_array, prominence=15) #调用find_peaks,寻找峰值
        plt.ion() #plt.ion()与plt.close()联用，能够自动关闭图片展示窗口
        plt.plot(a,b, linewidth = 0.7, c='red') #绘制拉曼光谱图
        for x,y in zip(a_array[peaks].tolist(), b_array[peaks].tolist()):
            plt.text(x, y+10, int(x), ha='center', va = 'top', fontsize=8) #使用对应的横坐标标注峰值
            plt.plot(x, y, marker='o', markersize=2, c='blue') #使用‘O’标注峰顶
        plt.xlim(left=35) #横坐标的最小值为35
        plt.xlabel('rel.1/cm') #横坐标的题名为rel.1/cm
        plt.ylabel('CCD cts') #纵坐标的题名为CCD cts
        plt.rcParams['savefig.dpi'] = 300 #图片像素
        plt.rcParams['figure.dpi'] = 300 #图片分辨率
        portion = os.path.splitext(file_n) #将文件名与文件后缀分开，储存为列表
        position_im = path_im + "/" + portion[0] + '.jpg' #用文件名给图片命名
        plt.savefig(position_im) #保存图片
        plt.show() #展示图片
        plt.close() #关闭图片展示窗口

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

except IOError: #如果用户输入绝对路径错误，则执行如下代码
    print('Error:没有找到文件或读取失败，请重新输入！') #提醒用户重新输入数据文件夹所在的绝对路径
