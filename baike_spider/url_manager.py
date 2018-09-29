"""
    爬虫的url管理器类
"""

class UrlManager(object):
    # 初始化存储网页url的列表
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    # 添加一条新的url到未使用过的url列表中
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:  # 检查url是否已存在
            self.new_urls.add(url)

    # 添加N个新的url到未使用的url列表中
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 检查是否有url待爬取
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 取出一条待爬取的url并且将它加入已爬取的url列表
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
