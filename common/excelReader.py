#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 14:08
# @Author  : Chris.Ma
# 将excel读取出来
import xlrd
import os


class ExcelReader():
    def __init__(self,filename,sheet):
        self.filename = filename
        self.sheet = sheet

    #sheetindex
    def get_excel_data(self):
        #路径参数化
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))
        base_dir = base_dir.replace('\\', '/')
        file_path = base_dir + '/data/' + self.filename
        #最终返回的列表
        result = []
        #读取excel
        excel = xlrd.open_workbook(file_path)
        #获取特定的sheet
        worksheet = excel.sheet_by_index(self.sheet)

        #获取sheet行数
        nrows = worksheet.nrows
        ncols = worksheet.ncols
        #读表头
        keys = []
        for l in range(ncols):
            keys.append(str(worksheet.cell(0,l).value))

        # print(keys)
        #读表体
        for i in range(1,nrows):
            tmp = {}
            #按照column取值
            for l in range(ncols):
                tmp[keys[l]] = worksheet.cell(i,l).value
            result.append(tmp)
        return result

    # 用sheet名字来读取
    def get_excel_data_sheet(self):
        # 路径参数化
        base_dir = str(os.path.dirname(os.path.dirname(__file__)))
        base_dir = base_dir.replace('\\', '/')
        file_path = base_dir + '/data/' + self.filename
        # 最终返回的列表
        result = []
        # 读取excel
        excel = xlrd.open_workbook(file_path)
        # 获取特定的sheet，sheet名字
        worksheet = excel.sheet_by_name(self.sheet)

        # 获取sheet行数
        nrows = worksheet.nrows
        ncols = worksheet.ncols
        # 读表头
        keys = []
        for l in range(ncols):
            keys.append(str(worksheet.cell(0,l).value))

        # print(keys)
        # 读表体
        for i in range(1,nrows):
            tmp = {}
            #按照column取值
            for l in range(ncols):
                tmp[keys[l]] = worksheet.cell(i,l).value
            result.append(tmp)
        return result


if __name__ == "__main__":
    # excel = ExcelReader("test.xlsx",2)
    # op = excel.get_excel_data()
    # print(op)
    excel = ExcelReader("test.xlsx","moco测试")
    op = excel.get_excel_data_sheet()
    print(op)

