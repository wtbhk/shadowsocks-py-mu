# Please edit this file and rename it as config.py

import logging

# Config
MYSQL_HOST = 'mengsky.net'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASS = 'root'
MYSQL_DB = 'shadowsocks'
MYSQL_USER_TABLE = 'user'
MYSQL_TIMEOUT = 30

MANAGE_PASS = 'passwd'
# if you want manage in other server you should set this value to global ip
MANAGE_BIND_IP = '127.0.0.1'
# make sure this port is idle
MANAGE_PORT = 23333

# BIND IP
# if you want bind ipv4 and ipv6 '::'
# if you want bind all of ipv4 if '0.0.0.0'
# if you want bind a specific IP you may use something like '4.4.4.4'
SS_BIND_IP = '::'
# This default method will be replaced by database record if applicable
SS_METHOD = 'aes-256-cfb'
# Shadowsocks One Time Auth (OTA)
SS_OTA = 'true'
# Skip listening these ports
SS_SKIP_PORTS = ['443']
# Shadowsocks Time Out
# It should > 180s as some protocol keepalive packet 3 min, Eg.: bt
SS_TIMEOUT = 185
# Shadowsocks TCP Fastopen (Some OS may not support this)
SS_FASTOPEN = False
# Shadowsocks verbose
SS_VERBOSE = 1
# Banned IP List
SS_FORBIDDEN_IP = []

# LOG CONFIG
LOG_ENABLE = False
# Available Log Level: logging.NOTSET|DEBUG|INFO|WARNING|ERROR|CRITICAL
LOG_LEVEL = logging.DEBUG
LOG_FILE = 'shadowsocks.log'
# The following format is the one suggested for debugging
# LOG_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
LOG_FORMAT = '%(asctime)s %(levelname)s %(message)s'
LOG_DATE_FORMAT = '%b %d %H:%M:%S'
