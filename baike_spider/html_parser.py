"""
解析网页，找出网页中所有的超链接，存储下来，并且解析出本网页百科的词条与摘要
"""

import re
import urllib
import bs4


class HtmlParser(object):

    # 获取页面中的所有链接并返回
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/.+"))   # 为什么这里的正则表达式用\" 匹配不到"  ???????
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)  # 此处为parse而不是urlparse
            new_urls.add(new_full_url)
        return new_urls

    # 执行另外两个方法获得url和数据 并返回
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = bs4.BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    # 获取百科网页中的词条和摘要 并返回
    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_ = 'lemma-summary')

        res_data['summary'] = summary_node.get_text()   # 如果没有摘要这个属性就会报错，因此加一个异常捕捉

        return res_data