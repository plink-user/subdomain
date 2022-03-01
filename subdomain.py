# coding:utf-8
import time
from urllib.request import urlopen
import tldextract

for i in open("webjieguo.txt"):
	i = i.strip("\n")
	headers={
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.5211 SLBChan/23',
		'Refer':'https://rapiddns.io/subdomain'
    }
	ext = tldextract.extract(i)
	main_domain = '.'.join(ext[1:])
	with open("a.txt","a") as f:
		f.write(main_domain+"\n")