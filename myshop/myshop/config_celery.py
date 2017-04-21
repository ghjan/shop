# CELERY
# BROKER_URL = 'pyamqp://guest@localhost//'
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
# BROKER_URL = 'amqp://jian.zhang:jian.zhang@localhost:5672//'
#BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Shanghai'