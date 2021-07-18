

#resp = request.urlopen(req)
#print(resp.read().decode("utf-8"))
import ssl
import urllib.request

context = ssl._create_unverified_context()
urllib.urlopen(context=context)

req = request.Request("http://www.baidu.com")
req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
resp =urllib.request.urlopen(req)


print(resp.read().decode("utf-8"))

