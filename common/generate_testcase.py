# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 23:20
# @Author  : dashenN72
"""
自动生成测试用例，依据接口文档得到的请求参数组合
"""

from itertools import product

params_module = {'name': ['petty', ' ', '!', 111], 'age': [123, 'test', ' ']}


class GenerateCase(object):

    def get_case_from_module(self, params):
        """
        通过给定的参数及其值的情况下，自动组合成请求参数
        :param params: 请求参数为字典，key是参数名，value是参数名对应值的可能情况组成的列表
        :return: 包含多个字典型请求参数组成的列表 [{'a': 1, 'b': 2},{'a': 'test', 'b': ''}]
        """
        params_request = list(params.keys())  # 获取请求参数名组成的list
        temp_values_request = list(params.values())  # 获取请求参数值组成的list
        values_request = [list(value) for value in product(*temp_values_request)]  # 值的自由组合
        param_value_request = [dict(zip(params_request, value_request)) for value_request in values_request]
        return param_value_request


if __name__ == '__main__':
    gc = GenerateCase()
    print(gc.get_case_from_module(params=params_module))


