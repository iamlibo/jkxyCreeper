import urllib2
import HTMLParser


# from HTMLParser import HTMLParser

class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.f = open('htmldata.txt', 'w')

    def __del__(self):
        self.f.close()
        # HTMLParser.HTMLParser.__del__(self)

    def handle_starttag(self, tag, attrs):
        # print  "Start tag:", tag
        if tag == "a":
            if len(attrs) == 0:
                pass
            else:
                for (variable,value) in attrs:
                    if variable == "href":
                        if value.endswith("ss=1"):
                            print  "     attr:", value

    # def handle_endtag(self, tag):
    #     print  "End tag  :", tag
    #
    # def handle_data(self, data):
    #     print  "Data     :", data
    #
    # def handle_comment(self, data):
    #     print  "Comment  :", data

        # def handle_entityref(self, name):

    #   c = unichr(name2codepoint[name])
    #   print  "Named ent:", c

    # def handle_charref(self, name):
    #     if name.startswith('x'):
    #         c = unichr(int(name[1:], 16))
    #     else:
    #         c = unichr(int(name))
    #     print  "Num ent  :", c
    #
    # def handle_decl(self, data):
    #     print  "Decl     :", data


if __name__ == '__main__':
    req = urllib2.Request('http://www.jikexueyuan.com/course/2625.html')
    response = urllib2.urlopen(req)
    htmlStr = response.read()
    print htmlStr
    my = MyParser()
    # htmlStr = '<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>'
    my.feed(htmlStr)