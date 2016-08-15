#!/bin/bash
# 记录一下开始时间
echo `date` >> /Users/duxiaoxing/shell/log.txt
`python /Users/duxiaoxing/shell/autoupdatesvn.py`
# 运行完成
echo 'finish' >> /Users/duxiaoxing/shell/log.txt
