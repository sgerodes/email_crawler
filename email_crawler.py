from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def find_all_links_on_page(url):
    links=[]
    resp = urlopen(url)
    soup = BeautifulSoup(resp, "html.parser" ,from_encoding=resp.info().get_param('charset'))
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith(domain):
            links.append(href)
    return links

class Crawler():
    extractions=set()
    re_pattern=""
    def set_email_pattern(self):
        self.re_pattern = r'[\w\.-]+@[\w\.-]+\.[\w\.]+'
        #self.re_pattern = r"(^[a-zA-Z0-9_\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    def search_for_extractions(self, str_url):
        page_html = str(urlopen(str_url).read())
        findings = re.findall(self.re_pattern, page_html)
        self.extractions.update(findings)
    def get_extractions(self):
        return self.extractions




domain = 'https://www.tum.de'
initial_url = 'https://www.tum.de'
LIMIT_URLS=30

crawled_urls=[]
to_be_crawled_urls=[initial_url]
email_crawler=Crawler()
email_crawler.set_email_pattern()


while to_be_crawled_urls:
    current_url=to_be_crawled_urls.pop()
    if len(to_be_crawled_urls) + len(crawled_urls) < LIMIT_URLS:
        urls_on_page=find_all_links_on_page(current_url)
        to_be_crawled_urls+=urls_on_page
    else:
        to_be_crawled_urls=to_be_crawled_urls[:LIMIT_URLS]
    email_crawler.search_for_extractions(current_url)
    crawled_urls.append(current_url)


#[print(url) for url in crawled_urls]
#print(email_crawler.get_extractions())
#print()
#print("emails found:")
[print(email) for email in email_crawler.get_extractions()]


