#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 15:26
# @Author  : Chris.Ma
#测试用例封装
import pytest
import allure
from common.config import Config
from common.excelReader import ExcelReader

#初始化config
from common.sendRequest import SendRequest

config = Config()
#读取excel信息
file = config.get_value("run.conf","execution","data")
#javamall
excel = ExcelReader(file,0)
testdata = excel.get_excel_data()

#moco
excel_moco = ExcelReader(file, "moco测试")
testdata_moco = excel_moco.get_excel_data_sheet()

#根据运行环境读取host信息
env = config.get_value("run.conf","execution","env")
host = config.get_value("host.conf", env, "host")

#mocohost信息
env_moco = config.get_value("run.conf","execution","env")
host_moco = config.get_value("host.conf", env, "host")

#组织pytest数据驱动
data = []
for l in testdata:
    data.append(pytest.param(host,l["url"], l["method"],
                             l["header"],l["data"],l["expect"],id=l["name"]))

#组织pytest数据驱动
data_moco = []
for l in testdata_moco:
    data_moco.append(pytest.param(host_moco,l["url"], l["method"],
                             l["header"],l["data"],l["expect"],id=l["name"]))


#测试用例
@allure.story()
@pytest.mark.parametrize("host,url,method,header,data,expect", data)
@pytest.mark.javamall
def testapis(host,url,method,header,data,expect):
    send = SendRequest()
    result = send.request_api(method,host,url,header,data)
    assert expect in result.text


#测试用例
@allure.story()
@pytest.mark.parametrize("host,url,method,header,data,expect", data_moco)
@pytest.mark.moco
def testapis(host,url,method,header,data,expect):
    send = SendRequest()
    result = send.request_api(method,host,url,header,data)
    assert expect in result.text