# encoding:utf-8

import os.path
import string
import shutil

file_name = 'Contents.json'

for root, dirs, files in os.walk(os.getcwd()):
    # count = len(os.listdir(os.path.abspath(dd)))
    # print 'dir % count % ',dd,count
    # # print os.path.abspath(dir)
    # for name in files:
    #     print root + '/' + name
    # print dirs
    # print root
    # count = len(os.listdir(root))
    # print count
    
    # for sub_dir in dirs:
    #     print os.path.abspath(sub_dir)
    
    # for sub_root in root:
    count = len(os.listdir(root))
    if count == 1:
        for sub_file in os.listdir(root):
            if (string.find(sub_file, file_name) != -1):
                # print os.path.abspath(sub_file)
                print root
                shutil.rmtree(root)