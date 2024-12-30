import multiprocessing

# 工作进程数
workers = 1  # 设置为 1 避免多进程导致的问题

# 工作模式
worker_class = 'sync'

# 绑定地址
bind = '0.0.0.0:5000'

# 日志级别
loglevel = 'info'

# 访问日志格式
accesslog = '-'
errorlog = '-'

# 超时设置
timeout = 120

# 重载设置
reload = False

# 守护进程设置
daemon = False

# 进程名称
proc_name = 'chopone_backend' 