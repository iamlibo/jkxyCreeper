# coding=utf-8
import urllib2
import cookielib

# filename ='cookie.txt'
# cookie = cookielib.MozillaCookieJar(filename)
cookie = cookielib.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
req =urllib2.Request('http://www.jikexueyuan.com/course/2688.html')
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response =opener.open(req)
# cookie.save(ignore_expires=True,ignore_discard=True)
print response.read()