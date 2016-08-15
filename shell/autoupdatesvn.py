# encoding:utf-8
import os
import commands
import time

root_dir = '/Users/duxiaoxing/Documents/zproduct/SVN/'
log_file_dir = root_dir + 'log.txt'

svn_server_doc = root_dir +'协议文档'
svn_product_doc = root_dir + 'product/tags'
svn_ui = root_dir + 'ui/IOS '
svn_yeemiao_trunk = root_dir + 'yeemiao/trunk'
svn_yeemiao_tags = root_dir + 'yeemiao/tags'
svn_yeemiao_branches = root_dir + 'yeemiao/branches'
svn_yeemiao_android = root_dir + 'yeemiao'


svn_dirs = [svn_server_doc,svn_product_doc,svn_ui,svn_yeemiao_trunk,svn_yeemiao_tags,svn_yeemiao_branches,svn_yeemiao_android]
for svn_dir in svn_dirs:
    svn_update_command = 'cd ' + svn_dir + ';' + 'svn update'
    command_output =  commands.getoutput(svn_update_command)
    with open(log_file_dir,'a ') as log_file_open:
        time_stamp = time.localtime(time.time())
        time_string = time.strftime('%Y-%m-%d %H:%M:%S',time_stamp)
        log = '更新时间:' + time_string + '\n命令行:' + svn_update_command + '\n输出:' + command_output + '\n'
        log_file_open.write(log)

with open(log_file_dir,'a') as log_file_open:
        log_file_open.write('------------------------------------------------\n')
