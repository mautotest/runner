# -*- coding: utf-8 -*-
# -----------------------------------------------------
# @Software: PyCharm
# @File: job.py
# @Author: majiayang
# @Institution: huawei, China
# @E-mail: 609921831@qq.com.com
# @Site:
# @Time: 12月 21, 2020
# -----------------------------------------------------
from common.status import s
from common.job_tool import jobs
from worker import get_current_app
from common.request_tool import RequestTool
import os

#心跳任务
def heart_job():
    current_app = get_current_app()
    current_app.logger.debug('status:' + s.status)
    server_ip = os.environ.get("MTEST_SERVER_IP", "127.0.0.1")
    server_port = os.environ.get("MTEST_SERVER_PORT", 5021)
    url = "http://{}:{}/heart".format(server_ip, server_port)
    current_app.logger.debug('send heart:{},status:{}'.format(url, s.status))
    RequestTool.request_post(url, json={"status": s.status})

#工作任务
def work_job():
    pass


def start_heart():
    jobs.add_interval_job(heart_job, seconds=10)


def start_work(date, args):
    return jobs.add_date_job(work_job, data=date, args=args)
