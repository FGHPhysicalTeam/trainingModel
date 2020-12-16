import os
path="D:\\pycharmProjects\\test-lenet-5_2\\test-LeNet-5\\Pic\\charPic\\19\\"
filelist=os.listdir(path)
i = 2
for files in filelist:
    if files != ".DS_Store":
        olddir=os.path.join(path,files)
        filename=os.path.splitext(files)[0]
        filetype=os.path.splitext(files)[1]
        newdir=os.path.join(path,"√(" + str(i) + ")" + filetype)
        os.rename(olddir,newdir)
        i = i + 1