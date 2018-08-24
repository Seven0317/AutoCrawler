# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/24 16:33

# 导入html数据下载器模块
import downloader
# 导入数据结果输出器模块
import outputer


class SpiderMain(object):
    """
    定义一个数据爬取器
    """
    def __init__(self, url, count):
        # 初始化下载地址
        self.url = url
        # 初始化爬取数据总数
        self.count = count
        # 初始化下载器
        self.downloader = downloader.Downloader()
        # 初始化输出器
        self.outputer = outputer.Outputer()

    def craw(self):
        # 下载器根据下载地址和下载数量爬取数据并存入dataa字典中
        datas = self.downloader.download(self.url, self.count)
        # 输出器提取datas字典中数据并保存在txt文件中
        self.outputer.output(datas)


if __name__ == '__main__':
    # 爬取的网址
    root_url = "http://www.iciba.com"
    # 实例化爬取器
    obj_spider = SpiderMain(root_url, 30)
    # 调用爬取方法
    obj_spider.craw()
