from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
# from urllib.error import URLError
# try:
# 	html = urlopen('https://google.com')
# 	attr=html.h1.id
# except HTTPError as e:
# 	print(e)
# except URLError as e:
# 	print('The server could not be found!')
# except AttributeError as e:
# 	print('tag not found')
# else:
# 	print('It Worked!')


# try:
# 	bs = urlopen('https://google.com')
# 	# badContent = bs.nonExistingTag.anotherTag
# 	badContent = bs
# except AttributeError as e:
# 	print('Tag was not exist')
# else:
	
# 	if badContent == None:
# 		print ('Tag was not found')
# 	else:
# 		print(badContent)


def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bs = BeautifulSoup(html.read(), 'html.parser')
		# title = bs.body.h1
		title = bs.head.find_all('link')
	except AttributeError as e:
		return None
	return title
# title = getTitle('http://www.pythonscraping.com/pages/page1.html')
title = getTitle('https://www.w3schools.com/')
if title == None:

	print('Title could not be found')
else:
	print(title)