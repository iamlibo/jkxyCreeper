# coding=utf-8
import requests
import os, urllib2, urllib
import types
from lxml import etree

# 设置下载后存放的存储路径'C:\Users\yinyao\Desktop\Python code'
path = r'C:\temp\\'


# file_name = r'test.mp4'  # 文件名，包含文件格式
# dest_dir = os.path.join(path, file_name)


# 定义下载函数downLoadPicFromURL（本地文件夹，网页URL）
def downLoadFromURL(title, url):
    file_name = title + '.mp4'  # 文件名，包含文件格式
    dest_dir = os.path.join(path, file_name)
    # print file_name, url
    try:
        urllib.urlretrieve(url, dest_dir)
    except:
        print '\tError retrieving the URL:', dest_dir


# 运行
def getHtml(url):
    cookies = {
        '_ga': 'GA1.2.1088669291.1475485033',
        'authcode': '1d69SHomQAle3OqIWAvR6FipRU5DRjKcAM40MWO1jk94JC2zC6GgTIx5lCtfhgLwk3mtCgDNjphaZuzjpf8KtIhyWV4jQ71Xiv23yQVU0%2B56bDYRpt8amoO7',
        'avatar': 'http%3A%2F%2Fassets.jikexueyuan.com%2Fuser%2Favtar%2Fdefault.gif',
        'ca_status': '0',
        'code': 'WMXIDB',
        'gr_cs1_e2be8178-47b9-4991-85e6-678daff13428': 'uid%3A4166529',
        'gr_session_id_aacd01fff9535e79': 'e2be8178-47b9-4991-85e6-678daff13428',
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
    # url = "http://www.jikexueyuan.com/course/61.html"
    htmlStr = requests.get(url, cookies=cookies, headers=headers, ).content
    # htmlStr = requests.get(url, headers=headers, ).content
    # print htmlStr
    return htmlStr


def getCourses(page):
    # 查找出课程列表，存入一个数组
    course_list = page.xpath(u"//dl[@class='lessonvideo-list']/dd/h2/a")
    course_index = 1
    courses = {}
    for course in course_list:
        # print "章节:", course.text, course.get('href')
        courses[course_index] = {'title': course.text, 'href': course.get('href')}
        course_index = course_index + 1
    # print courses
    return courses


# 查找mp4下载地址
def getMp4Url(page):
    videos = page.xpath(u"//source")
    # print  videos
    for video in videos:
        url = video.get('src')
        # downLoadPicFromURL(dest_dir, url)
        print url
        return url


def getTitle(page):
    etitle = page.xpath(u"//div[@id='palyer-box']/h1/span[@class='tit']")
    for et in etitle:
        return et.text


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
    print path

if __name__ == '__main__':
    # req = urllib2.Request('http://www.jikexueyuan.com/course/2713.html')
    # response = urllib2.urlopen(req)
    # htmlStr = response.read()
    # print htmlStr

    # url = "http://www.baidu.com"
    # url = "http://www.jikexueyuan.com/course/2688.html"
    url = "http://www.jikexueyuan.com/course/1860.html"
    htmlStr = getHtml(url)
    page = etree.HTML(htmlStr)
    title = getTitle(page)
    mkdir(path + title)
    # courses = getCourses(page)

    # current_index = 1
    # 按列表读取课程
    # for c in courses:
    #     v = courses.get(c)
    #     url = v.get('href')
    #     title = v.get('title')
    #     print c, title, url
    # if c > 1:
    #     htmlStr = getHtml(url)
    #     page = etree.HTML(htmlStr)
    #
    # mp4Url = getMp4Url(page)
    # downLoadFromURL(title, mp4Url)
    # getHtml(url)
    # print '=======', title, '=========='
    #
    print 'ok'
