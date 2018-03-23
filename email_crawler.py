import re
from urllib.request import urlopen

def find_all_emails_on_url(url):
    page_html = str(urlopen(url).read())
    return set(re.findall(pattern, page_html))


domain = 'https://www.16personalities.com'
initial_url = 'https://www.16personalities.com/de'
pattern = r'[\w-]+@\w+\.[\w.]+'
#print(find_all_emails_on_url(initial_url))


from bs4 import BeautifulSoup

def find_all_links_on_page(url):
    links=[]
    resp = urlopen(url)
    soup = BeautifulSoup(resp, "html.parser" ,from_encoding=resp.info().get_param('charset'))
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith(domain):
            links.append(href)
    return links

all_links=find_all_links_on_page(initial_url)

step2=set()
for link in all_links:
    step2.update(find_all_links_on_page(link))
print(step2)

#step3=set(step2)
#for link in step2:
#    step3.update(find_all_links_on_page(link))
#print(step3)


emails=set()
for link in step2:
    emails.update(find_all_emails_on_url(link))

print(emails)
