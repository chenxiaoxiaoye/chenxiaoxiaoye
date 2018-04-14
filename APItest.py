# *coding:utf-8*
import unittest
# from unittest import TestCase

import requests


url="http://www.baidu.com"
result=requests.get(url)
print result