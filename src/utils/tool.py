import time
import settings

# 设置登陆token
def setToken(str):
    global token
    token = str

# 获取请求头[auth: 是否需要登录, extra: 是否携带额外header]
def headers(auth = 0, extra = {}):
    headers = settings.defaultHeaders
    if auth:
        authHeaders = {"Authorization": "Bearer " + token}
        headers = {**headers, **authHeaders}
    if extra:
        headers = {**header, **extra}
    return headers

# 写入日志
def log(content):
    file = open("logs/%s.log" %time.strftime("%Y%m%d"), 'a')
    file.write("[ %s ] " %time.strftime("%Y-%m-%d %H:%M:%S") + str(content) + '\n')
    file.close()
