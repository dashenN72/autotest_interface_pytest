#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 14:42
# @Author  : Chris.Ma
#接口测试方法的封装
#method，url， header，data，response
import requests
import json

from common.excelReader import ExcelReader


class SendRequest():
    @staticmethod
    def request_api(method,host,url,header,data):
        test_url = host + url
        if not test_url.startswith("http://"):
            test_url = "http://" + test_url

        try:
            if method == "GET":
               if header is None or header == "":
                   if data is None or data == "":
                       return requests.get(url = test_url)
                   else:
                       return requests.get(url = test_url, data= data)
               else:
                   headerdict = json.loads(header)
                   if data is None or data == "":
                       return requests.get(url = test_url, headers = headerdict)
                   else:
                       return requests.get(url = test_url, headers = headerdict, data= data)

            if method == "POST":
                if header is None or header == "":
                    if data is None or data == "":
                        return requests.post(url=test_url)
                    else:
                        return requests.post(url=test_url, data=data)
                else:
                    headerdict = json.loads(header)
                    if data is None or data == "":
                        return requests.post(url=test_url, headers=header)
                    else:
                        datadict = json.loads(data)
                        if "application/json" in header:
                            return requests.post(url=test_url, headers=headerdict, json=datadict)
                        else:
                            return requests.post(url=test_url, headers=headerdict, data=datadict)

            if method == "PUT":
                if header is None or header == "":
                    if data is None or data == "":
                        return requests.put(url=test_url)
                    else:
                        return requests.put(url=test_url, data=data)
                else:
                    headerdict = json.loads(header)
                    if data is None or data == "":
                        return requests.put(url=test_url, headers=header)
                    else:
                        datadict = json.loads(data)
                        if "application/json" in header:
                            return requests.put(url=test_url, headers=headerdict, json=datadict)
                        else:
                            return requests.put(url=test_url, headers=headerdict, data=datadict)

            if method == "DELETE":
               if header is None or header == "":
                   if data is None or data == "":
                       return requests.delete(url = test_url)
                   else:
                       return requests.delete(url = test_url, data= data)
               else:
                   headerdict = json.loads(header)
                   if data is None or data == "":
                       return requests.delete(url = test_url, headers = headerdict)
                   else:
                       return requests.delete(url = test_url, headers = headerdict, data= data)
        except:
            print("服务器访问失败")


if __name__ == "__main__":
    # file = "test.xlsx"
    # excel = ExcelReader(file,0)
    # testdata = excel.get_excel_data()
    excel = ExcelReader("test.xlsx", "moco测试")
    testdata = excel.get_excel_data_sheet()
    send = SendRequest()
    host = "192.168.0.105:8080"
    for l in testdata:
        print((send.request_api(l["method"],host,l["url"],l["header"],l["data"])).text)