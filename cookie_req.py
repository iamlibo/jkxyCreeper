import requests

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
url="http://www.jikexueyuan.com/course/2688.html"
res = requests.get(url, cookies=cookies, headers=headers, ).content
print res