# stock 全局配置
DEBUG = True
VERSION = '0.0.1'


#mysql配置
MYSQL = {
    'user': 'stock',
    'pswd': '123456',
    'host': '127.0.0.1',
    'port': '3306',
}
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{pswd}@{host}:{port}/stock?charset=utf8'.format(**MYSQL)
SQLALCHEMY_TRACK_MODIFICATIONS=True


# redis配置，使用redis作为消息队列，如果必要还要进行设置缓存
CELERY_BROKER_URL='redis://127.0.0.1:6379/0'
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DATABASE = 0
#celery有问题，不再用来作为消息队列使用，废弃
# CELERY_RESULT_BACKEND=''
#http://www.avsc5.com/list/14-10.html


# 功能控制,作为一个开关，用来判断是否展示在前端页面上，True则生效，False则无效
MODULE = {
    'join_us': True,   # 展示加入我们
    'task': False  # 开发中的定时任务
}


# 企业微信配置
WECHAT = {
    'key': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', # 这里是企业微信机器人的key
    'template': {
        'msgtype': 'markdown',
        'markdown': {
            'content': 'Clover平台运行报告！\n'+
            '>类型:<font color=\"comment\">{type}</font>\n' +
            '>团队:<font color=\"comment\">{team}</font>\n' +
            '>项目:<font color=\"comment\">{project}</font>\n' +
            '>名称:<font color=\"comment\">{name}</font>\n' +
            '>接口:<font color=\"comment\">{interface}个</font>\n' +
            '>断言:<font color=\"comment\">{verify}个</font>\n' +
            '>成功率:<font color=\"comment\">{percent}</font>\n' +
            '>开始时间:<font color=\"comment\">{start}</font>\n' +
            '>结束时间:<font color=\"comment\">{end}</font>\n' +
            '[测试报告-{id}](http://www.52clover.cn/report/detail?id={id})'
        }
    }
}


# 邮箱配置
EMAIL = {
    'sender': '12345678@qq.com',
    'receiver': ['12345678@qq.com'],
    'password': '',
    'smtp_host': 'smtp.qq.com',
}

NOTIFY = {
    # 通知的触发事件，成功时通知还是失败时通知
    'event': ['success', 'failed'],
    # 通知的方式，企业微信还是email，或则配置的其它方式
    'channel': ['email'],
}


import os

from app.tasks.task_jobs import job_1

basedir = os.path.abspath(os.path.dirname(__file__))

TEAM_DICT = {
    "3": "基础服务",
    "5": "财商基金",
    "4": "保险服务",
    "6": "保险供应链",
    "7": "数据平台",
    "9": "系统运维",
    "44": "大前端",
    "8": "实例项目",
    "29": "设计"
}

class Config:
    DEBUG=True
    # 如何生成强壮的密钥，首先import os,然后os.urandom(24)即可
    SECRET_KEY = 'jcl_secret_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = 'qa@xiaobangtouzi.com'
    # FLASKY_MAIL_SENDER = 'jcl_send'
    # FLASKY_ADMIN = 'jcl_admin'
    LDAP_HOST = "ldaps://ad01.xiaobang.xyz"
    LDAP_ADMIN = {
        "user": "wechat_sync@xiaobang.xyz",
        "pwd": "JWPRj7pa^J#3NLZ3"
    }
    WECHAT_CONFIG = {
        "corp_id": "wwf1143b4d1547c208",
        "corp_secret": "IyrzR40w1pK2nVWEYIxWCQ9LkOWw7Wrcf45PTEubbV4"
    }
    GIT_SERVER="http://code.xiaobangtouzi.com/"
    JIRA_SERVER="http://jira.xiaobangtouzi.com/"

    #新增一个APS的API的开关
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_ECHO = True

    # 注意：需要定时执行的job只需要在这添加配置！
    JOBS = [
      {
          'id': 'jcl_0109_job001',
          'func': job_1,
          'args': None,
          'trigger': {
              'type': 'cron', # 类型
              'day_of_week': "0-6",	# 可定义具体哪几天要执行
              'hour': '22',	# 小时数
              'minute': '0'
          }
      }
      # {
      #   'id': 'jcl_0109_job002',
      #   'func': job_1,
      #   'args': '',
      #   'trigger': 'interval',
      #   'seconds': 5  # 每隔5秒执行一次
      # },
      # {
      # 	'id': 'jcl_0109_job003',
      # 	'func': 'job_1',
      #   # 一次性任务可以省略trigger
      # 	'args': None,
      # 	'next_run_time': datetime.datetime.now() + datetime.timedelta(seconds=10)
      # }
    ]

    @staticmethod # 可以使用类名直接调用该方法
    def init_app(app): #执行当前需要的环境的初始化
        return u'环境初始化成功'


# 开发环境
class DevelopmentConfig(Config):
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    # MAIL_USERNAME = 'qa@xiaobangtouzi.com'
    # MAIL_PASSWORD = '3fEJS7CcrxQSGALK'
    MAIL_USERNAME = 'jiangchenglong@xiaobangtouzi.com'
    MAIL_PASSWORD = '3fEJS7CcrxQSGALK'
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:123456a@127.0.0.1:3306/quality?charset=utf8"
    SQLALCHEMY_POOL_RECYCLE = 3599
    SQLALCHEMY_MAX_OVERFLOW = 100
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO")
    '''
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = '123456a'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'quality'

    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(
        DIALECT,
        DRIVER,
        USERNAME,
        PASSWORD,
        HOST,
        PORT,
        DATABASE
    )
    # 便于调试
    TEMPLATES_AUTO_RELOAD = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    '''
    JIRA_SERVER="http://jira.xiaobangtouzi.com/"


# 测试环境
class TestingConfig(Config):
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    # MAIL_USERNAME = 'qa@xiaobangtouzi.com'
    # MAIL_PASSWORD = '3fEJS7CcrxQSGALK'
    MAIL_USERNAME = 'jiangchenglong@xiaobangtouzi.com'
    MAIL_PASSWORD = '3fEJS7CcrxQSGALK'
    QUALITY_DATABASE = {
        'host': '172.16.0.115',
        'port': 3306,
        'user': 'quality_qa',
        'pswd': '#UE3a=jBaNnDqtGt',
        'db':'quality',
        'charset': 'utf8'
    }
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{user}:{pswd}@{host}:{port}/{db}?charset={charset}".format(**QUALITY_DATABASE)
    # 需要关联其他数据库表，在下方添加
    SQLALCHEMY_BINDS = {
        'xb':'mysql+mysqlconnector://{user}:{pswd}@{host}:{port}/{db}?charset={charset}'.format(**QUALITY_DATABASE)
    }
    SQLALCHEMY_POOL_RECYCLE = 3599
    SQLALCHEMY_MAX_OVERFLOW = 100
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO")
    # 这个是莞羚的验证码业务
    CATPCHA = {
      'host': '172.16.0.115',
      'port': 3306,
      'user': 'app',
      'password': 'Yc)E7aqYU6)AjW',
      'database': 'user_center',
      'charset': 'utf8'
    }
    JIRA_SERVER = "http://jira.xiaobangtouzi.com:8080/"


# 生产环境
class ProductionConfig(Config):
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'jiangchenglong@xiaobangtouzi.com'
    MAIL_PASSWORD = '3fEJS7CcrxQSGALK'
    QUALITY_DATABASE = {
        'host': '172.16.236.11',
        'port': 3306,
        'user': 'quality',
        'pswd': '6A5mK232t17w',
        'db':'quality',
        'charset': 'utf8'
    }
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{user}:{pswd}@{host}:{port}/{db}?charset={charset}".format(**QUALITY_DATABASE)
    # 需要关联其他数据库表，在下方添加
    SQLALCHEMY_BINDS = {
        'xb':'mysql+mysqlconnector://{user}:{pswd}@{host}:{port}/{db}?charset={charset}'.format(**QUALITY_DATABASE)
    }
    SQLALCHEMY_POOL_RECYCLE = 3599
    SQLALCHEMY_MAX_OVERFLOW = 100
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO")
    # 这个是莞羚的验证码业务
    CATPCHA = {
      'host': '172.16.16.49',
      'port': 3306,
      'user': 'user_center_read',
      'password': 'V@C^jJfdJe9FLhtV',
      'database': 'user_center',
      'charset': 'utf8'
    }


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': TestingConfig
}
