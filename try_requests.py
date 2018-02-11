import io
import sys
import requests

# 我们来吧百度的index页面的html源码抓取到本地，并用r变量保存
# 注意这里，网页前面的 http://一定要写出来，它并不能像真正的浏览器一样帮我们补全http协议

sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

r = requests.get("http://www.baidu.com")

# 将下载到的内容打印一下：
print(r.text)
