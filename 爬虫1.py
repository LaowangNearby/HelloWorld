#encoding:UTF-8
import urllib.request
url='http://www.baidu.com'
page=urllib.request.urlopen(url).read()
data = page.decode('UTF-8')
print(data)
