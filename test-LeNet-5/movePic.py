import numpy as np
import os
import shutil

# 读取每张图片按照其分类复制到相应的文件夹中
path_imgs = './Pic/charPic'

# i = 1
# #创建文件夹
# for i in range(20):
#     os.mkdir('./Pic/charPic/tmp/' + str(i))

for files in os.listdir(path_imgs):
    print(files)
    img_path = path_imgs + files
    if files[0]=="+":
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/0/' + files)
    elif files[0]=='-':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/1/' + files)
    elif files[0]=='.':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/2/' + files)
    elif files[0]=='0':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/3/' + files)
    elif files[0]=='1':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/4/' + files)
    elif files[0]=='2':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/5/' + files)
    elif files[0]=='3':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/6/' + files)
    elif files[0]=='4':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/7/' + files)
    elif files[0]=='5':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/8/' + files)
    elif files[0]=='6':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/9/' + files)
    elif files[0]=='7':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/10/' + files)
    elif files[0]=='8':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/11/' + files)
    elif files[0]=='9':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/12/' + files)
    elif files[0]=='=':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/13/' + files)
    elif files[0]=='B':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/14/' + files)
    elif files[0]=='E':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/15/' + files)
    elif files[0]=='q':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/16/' + files)
    elif files[0]=='v':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/17/' + files)
    elif files[0]=='θ':
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/18/' + files)
    else:
        shutil.move('./Pic/charPic/' + files, '/Users/fengyushan/Desktop/tmp/19/' + files)