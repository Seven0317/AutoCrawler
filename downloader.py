# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/24 16:34

import time
from selenium import webdriver


class Downloader(object):
    """
    定义一个下载器
    """
    def __init__(self):
        # 初始chrome浏览器驱动参数
        self.option = webdriver.ChromeOptions()
        # 禁掉消息提示条功能
        self.option.add_argument('disable-infobars')
        # 开启浏览器无头模式
        self.option.add_argument('--headless')
        # 驱动浏览器
        self.driver = webdriver.Chrome(chrome_options=self.option)

    def download(self, url, count):
        # 如果爬取网址为空则返回None
        if url is None:
            print("Downloading url is None.")
            return None
        # 否则开始定位数据并下载目标内容
        try:
            # 浏览器发起请求
            self.driver.get(url)
            # 最大化浏览器窗口
            self.driver.maximize_window()
            # 刷新
            self.driver.refresh()
            # 设置隐性等待时间为30s
            self.driver.implicitly_wait(30)
            # 定位元素并点击
            self.driver.find_element_by_xpath("/html/body/div[4]/div[9]/div[1]/div[1]/div[1]/div/div[4]/span/a").click()
            # 获取浏览器打开页面
            windows = self.driver.window_handles
            # 定位到最新打开的页面
            self.driver.switch_to.window(windows[-1])
            # 定位元素并点击
            # <dt class="nav-item-label">
            # /html/body/div[2]/div[3]/div[2]/div/dl[5]/dt/a
            self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div/dl[5]/dt/a").click()
            # 初始化空字典用于存储爬取数据
            datas = {}
            # 循环爬取目标直到爬取到规定数量为止
            while count > 0:
                time.sleep(1)
                # <div class="detail-content-en"> Don't let yourself get busy all day and end up doing nothing
                data_key = self.driver.find_element_by_class_name("detail-content-en").text
                data_value = self.driver.find_element_by_class_name("detail-content-zh").text
                datas[data_key] = data_value
                # <a class="detail-banner-left"
                self.driver.find_element_by_class_name("detail-banner-left").click()
                count = count - 1
            # 关闭浏览器
            self.driver.quit()
            return datas
        except Exception as e:
            print(e, '\n'"Download failed.")
