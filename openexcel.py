# *coding:utf-8*

import xlrd

def readexceldata(sheetvalue,rowvalue,colvalue):

    #打开工作簿
    datafile=xlrd.open_workbook("E:\\LicenseAPItest\\License-module-para.xls")
    #选择工作页
    sheet=datafile.sheet_by_index(sheetvalue)
    #读取行列数据
    datarow=sheet.row(rowvalue)[colvalue].value
    return datarow