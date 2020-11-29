#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 16:10
# @Author  : Chris.Ma
import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        outputs, errors = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        return outputs