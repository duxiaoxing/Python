# encoding:utf-8
import os.path
import string

for root, dirs, files in os.walk(os.getcwd()):
    file_name_png = '.png'
    file_name_jpg = '.jpg'
    for file_name in files:
        if (string.find(file_name,file_name_png) != -1):
            file_name_array = file_name.split(file_name_png)
            file_name_string = file_name_array[0]
            file_name_string_lastChar = file_name_string[-1]
            file_name_string_lastNextChar = file_name_string[-2:-1]
            if(file_name_string_lastChar.isdigit() and file_name_string_lastNextChar == '@'):
                  print root + '/' + file_name
        elif string.find(file_name,file_name_jpg)!= -1:
            file_name_array = file_name.split(file_name_jpg)
            file_name_string = file_name_array[0]
            file_name_string_lastChar = file_name_string[-1]
            file_name_string_lastNextChar = file_name_string[-2:-1]
            if(file_name_string_lastChar.isdigit() and file_name_string_lastNextChar == '@'):
                  print root + '/' + file_name
        else:
            continue
        

      