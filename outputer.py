# -*- coding: utf-8 -*-
# Version : V1.0
# Author  : Seven
# Date    : 2018/8/24 16:34

import re
import time


class Outputer(object):
    """
    定义一个输出器
    """
    def output(self, datas):
        # 如果爬取的内容为空则返回空
        if len(datas) is None:
            print("Content of data is None.")
            return
        # 否则按照下面定义格式输出到目标文件中
        try:
            # 格式化当前时间
            t = time.strftime("%Y_%m_%d %H %M %S", time.localtime())
            # 根据当前时间命名目标文件
            file_name = "out_%s.txt" % t
            # 循环将爬取数据写入目标文件中
            with open(file_name, "w", encoding="utf-8") as f_out:
                count = 1
                for data in datas.items():
                    f_out.write("%d: %s\n" % (count, re.sub("[()]", '', str(data))))
                    count = count + 1
        except Exception as e:
            print(e, '\n'"Output failed.")
