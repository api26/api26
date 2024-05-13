# ！ /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2024/4/26 0026 15:08
# Author    : yang
# @File     : config.py
# @Software : PyCharm

import logging,time
import os
from optparse import OptionParser

now = time.strftime('%Y%m%d_%H%M%S', time.localtime())
today = time.strftime('%Y%m%d', time.localtime())

# 项目路径
# prj_path是当前文件的绝对路径的上一级,__file__指当前文件)
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 项目目录 apitest目录
data_path = os.path.join(prj_path,"data") # 数据目录,暂时在项目目录下
test_path = os.path.join(prj_path,"test") # 用例目录,暂时在项目目录下
test_case_path = os.path.join(prj_path,"test","case") # 用例目录
log_file = os.path.join(prj_path, "log","log_{}.txt".format(today)) # 也可以每天生成新的日志文件
report_file = os.path.join(prj_path, "report","report_{}.html".format(now)) # 也可以每次生成新的报告
data_file = os.path.join(prj_path,"data","test_user_data.xlsx")
test_list_file = os.path.join(prj_path, 'test', 'test_list.txt')
last_fails_file = os.path.join(prj_path, 'last_fails.pickle')

#log文件配置
logging.basicConfig(
     level=logging.DEBUG, # log level
     format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s', # log格式
     datefmt='%Y-%m-%d %H:%M:%S', # 日期格式
     filename=log_file, # 日志输出文件
     # encoding='utf-8',
     filemode='a'
) # 追加模式

# 数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_passwd = 'root'
db = 'xzs'

# 邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '2761978436@qq.com'
smtp_password = 'jbivqrlddibtdcgh'
sender = smtp_user # 发件人
receiver = "2761978436@qq.com" # 收件人
subject = '接口测试报告' # 邮件主题
send_email_after_run = False #发送邮件开关


# 命令行选项
parser = OptionParser()
parser.add_option('--collect_only', action='store_true', dest='collect_only', help='仅列出所有用例')
parser.add_option('--tag',action='store',dest='tag',default='level1',help='根据标签生成测试套件')
parser.add_option('--rerun_fails', action='store_true', dest='rerun_fails', help='运行上次失败的用例')
parser.add_option('--test_list', action='store_true', dest='test_list', help='运行test/testlist.txt列表指定用例')

# 应用选项(使生效)
(options, args) = parser.parse_args()

#测试
if __name__ == '__main__':
 logging.info("接口测试")
