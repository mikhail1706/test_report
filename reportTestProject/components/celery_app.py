from kombu import Queue, Exchange
import os

# Celery application definition
CELERY_BROKER_URL = os.getenv('BROKER_URL', 'amqp://guest:guest@localhost:5672/')
CELERY_RESULT_BACKEND = 'rpc'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True
CELERY_CREATE_MISSING_QUEUES = True
CELERY_BEAT_SCHEDULE = {}

CELERY_QUEUES = (
    Queue('reports', Exchange('direct'), routing_key='celery'),

)
CELERY_ROUTES = {
    'reports.tasks.*': {
    },
}
