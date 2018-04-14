# *coding:utf-8*
import os

# os.getcwd()
def read_json_data(file):
    path = "C:\\Users\\Thinkpad\\PycharmProjects\\APItest\\"+file+".json"
    with open(path) as f:
        data=f.read()
    return data

# print read_json_data("createA")
def get_all_json(path):
    files=os.listdir(path)
    jsondic={}
    for file in files:
         if (os.path.splitext(file)[1]==".json"):
            jsondic[os.path.splitext(file)[0]] =read_json_data(os.path.splitext(file)[0])

    return jsondic

# print get_all_json("C:\\Users\\Thinkpad\\PycharmProjects\\APItest")
