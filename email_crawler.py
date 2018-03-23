import re
from urllib.request import urlopen

domain = 'www.tum.de'
url = 'https://www.tum.de/wirtschaft/kontakt/'

web_page = urlopen(url)
page_html = str(web_page.read())
pattern = r'[\w-]+@\w+\.[\w.]+'
matches = set(re.findall(pattern, page_html))
if matches:
    print (matches)
