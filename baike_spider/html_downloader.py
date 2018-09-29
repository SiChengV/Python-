"""
url下载器
"""

import urllib.request


class HtmlDownloader(object):

    # 根据url下载网页并返回
    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()