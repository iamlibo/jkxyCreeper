# coding=utf-8
import requests
import os, urllib2, urllib
from lxml import etree

# head = {'User-Agent': \
#             'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'}
#
# page = requests.get('http://www.jikexueyuan.com/course/1287_2.html?ss=1', \
#                         headers=head).content

# 设置下载后存放的存储路径'C:\Users\yinyao\Desktop\Python code'
path = r'C:\temp'
file_name = r'test.mp4'  # 文件名，包含文件格式
dest_dir = os.path.join(path, file_name)


# 定义下载函数downLoadPicFromURL（本地文件夹，网页URL）
def downLoadPicFromURL(dest_dir, URL):
    try:
        urllib.urlretrieve(url, dest_dir)
    except:
        print '\tError retrieving the URL:', dest_dir


# 运行
if __name__ == '__main__':
    # req = urllib2.Request('http://www.jikexueyuan.com/course/2713.html')
    # response = urllib2.urlopen(req)
    # htmlStr = response.read()
    # print htmlStr

    cookies = {
        '_ga': 'GA1.2.1088669291.1475485033',
        'authcode': '03281%2B3YDder4ImrakfyEjsfBYRrqTiwUAAeplZ2GXFKI2cnuPRX3vSKurpFwT%2BwhuL7jzTHRfbmJOsE3P%2BnLB7ST2v%2BwmU2%2F3odMcg12cH3WRvU18h8pI2B',
        'avatar': 'http%3A%2F%2Fassets.jikexueyuan.com%2Fuser%2Favtar%2Fdefault.gif',
        'ca_status': '0',
        'code': 'WMXIDB',
        'gr_cs1_db7abf94-e648-4c82-82d2-258ab3b18cfd': 'uid%3A4166529',
        'gr_session_id_aacd01fff9535e79': 'db7abf94-e648-4c82-82d2-258ab3b18cfd',
        'gr_user_id': '9f0a5c92-3c2f-453e-932e-d5015e48586b',
        'is_expire': '0',
        'level_id': '2',
        'ohterlogin': 'qq',
        'uid': '4166529',
        'uname': 'yodato',
        'vip_status': '1',
        'connect.sid': 's%3AqZz8tPAHdUk-OZxpYaGfS9a_SJnskmg7.ZLzHhp7%2FRGKsjPAbYQQDdxzOpozXqkk8kyMY7fsATcY',
        'kbtipclose': '1',
        'QINGCLOUDELB': '84b10773c6746376c2c7ad1fac354ddfd562b81daa2a899c46d3a1e304c7eb2b|V/I2k|V/IxJ'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    # url = "http://www.baidu.com"
    # url = "http://www.jikexueyuan.com/course/2688.html"
    url = "http://www.jikexueyuan.com/course/61.html"
    htmlStr = requests.get(url, cookies=cookies, headers=headers, ).content
    # htmlStr = requests.get(url, headers=headers, ).content
    print htmlStr

    page = etree.HTML(htmlStr)
    # 查找出课程列表
    course_list = page.xpath(u"//dl[@class='lessonvideo-list']/dd")
    course_index =0
    for course in course_list:
        # print course.attrib
        course_href = course.xpath(u"./h2/a")
        # print "course_href:", course_href
        # 在课程列表中找出当前页正在播放的课时<dd class="playing">
        isPlaying = course.get('class')
        # 正在播放的章节，下载文件名称与链接
        if isPlaying == 'playing':
            for ab in course_href:
                print "章节:", ab.text, ab.get('href'), isPlaying
                file_name = ab.text + ".mp4"
                print file_name
                # print ab.get('href')
        else:
            for ab in course_href:
                print "章节:", ab.text, ab.get('href')
    videos = page.xpath(u"//source")
    print  videos
    for video in videos:
        url = video.get('src')
        # downLoadPicFromURL(dest_dir, url)
        print url
