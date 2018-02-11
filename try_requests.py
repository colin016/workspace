import requests


def getHtmlText(url):
    try:
        print('get_html start')
        r = requests.get(url, timeout=30)
        print('get_html end')
        print(r.content)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.content
    except:
        return "Something Wrong!"


def get_html(url):
    try:
        print('get_html start')
        r = requests.get(url, timeout=30)
        print('get_html end')
        print(r.content)
        r.raise_for_status()

        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.content
    except:
        print('ERROR')
        return " ERROR "


def main(url):
    get_html(url)


url = 'http://www.baidu.com'

if __name__ == '__main__':
    main(url)
