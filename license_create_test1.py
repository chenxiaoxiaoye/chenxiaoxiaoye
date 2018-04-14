# *coding:utf-8*
import ast
import unittest
from distutils import file_util
from unittest import TestCase
import openexcel
import requests
import json
import readjson


class LicenseCreateTest(TestCase):
    def setUp(self):
        print "starttest"


    def test1(self):
        url="http://47.92.88.246:8999/it-license/it/query/license"
        # data=openexcel.readexceldata(0,1,5)
        # data2 = ast.literal_eval(data)
        header = {"Content-Type":"application/json"}
        # datas=readjson.get_all_json("C:\\Users\\Thinkpad\\PycharmProjects\\APItest")
        # for data in datas:
        #     result=requests.post(url=url,data=datas[data],headers=header)
        #     resobj=result.text
        #     print "testcase:"+data,resobj
        data=readjson.read_json_data("createA")
        print data["objectProperties"]["productVersion"]
        result = requests.post(url=url, data=data, headers=header)
        resobj = result.json()
        print result.text
        # curver=resobj["result"][8]["currentVersion"]
        # print type(str(curver))
        # self.assertEqual(curver,"basic_edition  A")

    def tearDown(self):
        print "endtest"



