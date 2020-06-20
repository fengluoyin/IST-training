#coding: utf-8
import socket

HOST = "http://testphp.vulnweb.com/listproducts.php"
PORT = 80

API_IP="222.186.57.204"
API_PORT= 3306

# 测试邮件发送功能case
EMAIL_ADDR='fengluoyin@126.com'
EMAIL_PASSWD='fengluoyin123'

#导入资产
domain_asset = ["testphp.vulnweb.com/listproducts.php"]
ip_asset = ["192.168.199.2", "192.168.199.145"]
url_asset = ["http://192.168.1.86/"]    #第一个url资产会添加高级监控

local_ip = socket.gethostbyname(socket.gethostname())

#网站可用性监控
alive_monitor_data = [
    {
        "target": "testphp.vulnweb.com/listproducts.php?cat=1",
        "period": 1,
        "resp_time": 30
    },
    {
        "target": "www.yahoo.com",
        "period": 5,
        "resp_time": 110
    }
]
