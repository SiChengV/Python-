from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self , root_url ):
        count = 1
        self.urls.add_new_url(root_url)        # 将初始页面的url添加进新url列表中
        while self.urls.has_new_url():          # 当新url列表中有带爬取url时
            try:
                new_url = self.urls.get_new_url()       # 取出一条带爬取url赋给new_url
                print('craw %d : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)   # 下载url页面
                new_urls , new_data = self.parser.parse(new_url, html_cont)   # 解析页面并返回 新的url列表 和 新的数据内容 赋给两个变量
                self.urls.add_new_urls(new_urls)   # 过滤新的url列表并加入 带爬取url列表
                self.outputer.collect_data(new_data)    # 将数据内容加入 data列表
                if count == 1000:           # 限制爬取1000次
                    break
                count = count + 1
            except:
                print('craw failed')
        self.outputer.output_html()

if __name__=="__main__":
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)