import os
import numpy as np
import tensorflow as tf
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
# tf.compat.v1.enable_resource_variables()
from PIL import Image

index = 0
totalCount = 0
for i in range(0, 20):
    count = 0
    dir = '.\\Pic\\testPicChar\\%s\\' % i
    for rt, dirs, files in os.walk(dir):
        for filename in files:
            filename = dir + filename
            if filename != ".\\Pic\\testPicChar\\%s\\.DS_Store" % i:
                # print(filename)
                count = count + 1
                totalCount = totalCount + 1
    print("class:" + str(i) + "," + "count:" + str(count))

print("totalcount:" + str(totalCount))
