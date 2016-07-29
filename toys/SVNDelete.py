# encoding:utf-8

import commands
import string
status  =  commands.getoutput('svn status')

for single_status in status.split('\n'):
    if (string.find(single_status,'!') != -1):
        # print single_status
        svn_command = 'svn delete' + '' + single_status.lstrip('!')
        # print 'svn_command '+svn_command
        print commands.getoutput(svn_command)