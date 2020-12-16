import numpy as np
import os
import shutil

# 读取每张图片按照其分类复制到相应的文件夹中
path_imgs = './Pic/geoPic'



for files in os.listdir(path_imgs):
    print(files)
    img_path = path_imgs + files
    if files[0]=="负":
        shutil.move('./Pic/geoPic/' + files, '/Users/fengyushan/Desktop/tmp/20/' + files)
    elif files[0]=='矩':
        shutil.move('./Pic/geoPic/' + files, '/Users/fengyushan/Desktop/tmp/21/' + files)
    elif files[0]=='正':
        shutil.move('./Pic/geoPic/' + files, '/Users/fengyushan/Desktop/tmp/22/' + files)
    elif files[0]=='Բ':
        shutil.move('./Pic/geoPic/' + files, '/Users/fengyushan/Desktop/tmp/23/' + files)
    elif files[0]=='ㄊ':
        shutil.move('./Pic/geoPic/' + files, '/Users/fengyushan/Desktop/tmp/24/' + files)