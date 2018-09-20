# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/9/20 11:43


from selenium import webdriver
import multiprocessing
import os
import time

groups = ['唯美', '插画', '可爱']


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("running time of {} is {} s".format(func.__name__, end - start))
    return wrapper


def spider(group, count):
    try:
        url = "https://image.baidu.com"
        pic_path = os.path.abspath(os.path.join(os.getcwd(), group))
        if not os.path.exists(pic_path):
            os.mkdir(pic_path)
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        pref_path = {'profile.default_content_settings.popups': 0, 'download.default_directory': pic_path}
        options.add_experimental_option('prefs', pref_path)
        driver = webdriver.Chrome(chrome_options=options)

        driver.get(url)
        driver.refresh()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element_by_link_text("壁纸").click()
        time.sleep(1)
        driver.find_element_by_link_text(group).click()
        time.sleep(1)
        driver.find_element_by_class_name("pcct").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='pc_container pccb']/div[1]").click()
        driver.find_element_by_class_name("imgbox").click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        while count >= 0:
            count = count - 1
            time.sleep(1)
            driver.find_element_by_xpath("//span[@class='bar-btn btn-download']").click()
            time.sleep(1)
            driver.find_element_by_class_name("img-next").click()
            time.sleep(1)
        time.sleep(2)
    finally:
        driver.quit()


@timing
def multi_spider():
    threads = []
    files = range(len(groups))
    for file in groups:
        t = multiprocessing.Process(target=spider, args=(file, 10))
        threads.append(t)
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()


if __name__ == "__main__":
    multi_spider()


