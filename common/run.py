#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 16:15
# @Author  : Chris.Ma
from common.config import Config
from common.shellUtil import Shell
import pytest
import os

if __name__ == "__main__":
    config = Config()
    shell = Shell()

    xml_path = config.xml_report_path
    html_path = config.html_report_path

    #删除xml下面的残留报告
    ls = os.listdir(xml_path)
    for l in ls:
        file = os.path.join(xml_path,l)
        os.remove(file)

    #运行pytest测试用例
    args = ["-m","moco","--alluredir", xml_path]
    pytest.main(args)

    cmd = "allure generate "+xml_path+" -o "+html_path+" --clean"

    print(cmd)
    shell.invoke(cmd)
    try:
        shell.invoke(cmd)
    except:
        print("运行失败")

