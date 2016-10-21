# coding=utf-8
# http://cv4.jikexueyuan.com/c10eea6d8dac017c23b6b23540583aaf/201610031900/course/3201-3300/3234/video/c3234b_01_h264_sd_960_540.mp4

# 下载网页文件到本地文件夹
import os, urllib2, urllib

# 设置下载后存放的存储路径'C:\Users\yinyao\Desktop\Python code'
path = r'C:\temp'
file_name = r'test.gif'  # 文件名，包含文件格式
dest_dir = os.path.join(path, file_name)

# 设置下载链接的路径
# url = "'http://cv4.jikexueyuan.com/c10eea6d8dac017c23b6b23540583aaf/201610031900/course/3201-3300/3234/video/c3234b_01_h264_sd_960_540.mp4"
url="https://misc.360buyimg.com/jdf/1.0.0/unit/globalImages/1.0.0/loading.gif"

# 定义下载函数downLoadPicFromURL（本地文件夹，网页URL）
def downLoadPicFromURL(dest_dir, URL):
    try:
        urllib.urlretrieve(url, dest_dir)
    except:
        print '\tError retrieving the URL:', dest_dir
# 运行
downLoadPicFromURL(dest_dir, url)