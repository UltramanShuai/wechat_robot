# _*_coding:utf-8_*_
# Author   : Leo
# Time     : 23/12/2018


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import MiniBatchKMeans


def zip_pic(file):
    pic = mpimg.imread(file, 0)  # 将图片加载为 ndarray 数组

    #plt.imshow(pic)

    n = pic.shape[0]

    data = pic.reshape(-1, 3)

    # train
    model = MiniBatchKMeans(n_clusters=5).fit(data)
    predict = model.predict(data)
    # 新图片数组
    new_colors = model.cluster_centers_[predict]

    #plt.imshow(new_colors.reshape(n, -1, 3).astype(int))
    # 修改名字
    new_name = file.split(".")[0] + "_return." + file.split(".")[1]

    mpimg.imsave(fname=new_name, arr=new_colors.reshape(n, -1, 3).astype(int))

    return new_name

